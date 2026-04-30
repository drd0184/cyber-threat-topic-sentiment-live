"""
Collect recent live cybersecurity items from public free sources.

This script only performs source collection and raw normalization. It does not
run preprocessing, topic modeling, sentiment analysis, P2, dashboard export, or
scheduled automation.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
import hashlib
import html
import re
import sys
import time
from pathlib import Path
from typing import Any

import feedparser
import pandas as pd
import requests
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "config" / "live_sources.yml"
RAW_DIR = PROJECT_ROOT / "data" / "live" / "raw"
ARCHIVE_DIR = PROJECT_ROOT / "data" / "live" / "archive"
DEFAULT_OUTPUT_PATH = RAW_DIR / "live_items_raw.csv"

USER_AGENT = "CyberThreatHotTopicIndex/0.1 academic local demo"
REQUEST_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "application/rss+xml, application/atom+xml, application/json;q=0.9, */*;q=0.8",
}
GDELT_KEYWORD_DELAY_SECONDS = 1.0

SOURCE_GROUPS = ("reddit_rss", "news_rss", "nvd_api")
RSS_GROUPS = ("reddit_rss", "news_rss")
GDELT_CONFIG_GROUP = "gdelt_doc_api"
OUTPUT_COLUMNS = [
    "id",
    "created_at",
    "source",
    "source_name",
    "source_type",
    "title",
    "text_raw",
    "url",
    "collected_at",
]


@dataclass(frozen=True)
class SourceConfig:
    group: str
    name: str
    url: str
    source: str
    source_name: str
    source_type: str
    enabled: bool


@dataclass(frozen=True)
class GdeltDocApiConfig:
    enabled: bool
    url: str
    source: str
    source_name: str
    source_type: str
    mode: str
    output_format: str
    sort: str
    max_records_per_keyword: int
    startdatetime: str
    enddatetime: str
    keywords: list[str]


@dataclass
class CollectionReport:
    enabled_sources: list[str] = field(default_factory=list)
    source_counts: dict[str, int] = field(default_factory=dict)
    source_name_counts: dict[str, int] = field(default_factory=dict)
    source_type_counts: dict[str, int] = field(default_factory=dict)
    failed_sources: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    gdelt_keyword_counts: dict[str, int] = field(default_factory=dict)
    gdelt_failed_keywords: list[str] = field(default_factory=list)
    collected_this_run: int = 0
    new_items_added: int = 0
    duplicates_discarded: int = 0
    final_rows: int = 0
    min_created_at: str = ""
    max_created_at: str = ""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Collect recent raw cybersecurity items from public live sources."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to config/live_sources.yml.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Path to the cumulative raw live CSV.",
    )
    parser.add_argument(
        "--archive-dir",
        type=Path,
        default=ARCHIVE_DIR,
        help="Directory where timestamped raw CSV snapshots are written.",
    )
    parser.add_argument(
        "--nvd-days",
        type=int,
        default=7,
        help="Number of recent days to request from NVD CVE API.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="Network timeout in seconds per request.",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=2,
        help="Retries for transient network errors per request.",
    )
    return parser.parse_args()


def resolve_project_path(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


def ensure_live_dirs(output_path: Path, archive_dir: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    archive_dir.mkdir(parents=True, exist_ok=True)


def load_config(config_path: Path) -> dict[str, Any]:
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle) or {}

    if not isinstance(loaded, dict):
        raise ValueError("Config root must be a mapping.")

    for group in SOURCE_GROUPS:
        loaded.setdefault(group, [])
        if not isinstance(loaded[group], list):
            raise ValueError(f"Config group must be a list: {group}")

    loaded.setdefault(GDELT_CONFIG_GROUP, {"enabled": False})
    if not isinstance(loaded[GDELT_CONFIG_GROUP], dict):
        raise ValueError(f"Config group must be a mapping: {GDELT_CONFIG_GROUP}")

    return loaded


def iter_enabled_sources(config: dict[str, Any]) -> list[SourceConfig]:
    sources: list[SourceConfig] = []
    required_keys = {"name", "url", "source", "source_name", "source_type", "enabled"}

    for group in SOURCE_GROUPS:
        for index, raw_source in enumerate(config.get(group, []), start=1):
            if not isinstance(raw_source, dict):
                raise ValueError(f"Invalid source entry in {group} at index {index}.")
            missing = required_keys.difference(raw_source)
            if missing:
                missing_list = ", ".join(sorted(missing))
                raise ValueError(f"Missing key(s) in {group}/{index}: {missing_list}")
            if not bool(raw_source["enabled"]):
                continue
            sources.append(
                SourceConfig(
                    group=group,
                    name=str(raw_source["name"]).strip(),
                    url=str(raw_source["url"]).strip(),
                    source=str(raw_source["source"]).strip(),
                    source_name=str(raw_source["source_name"]).strip(),
                    source_type=str(raw_source["source_type"]).strip(),
                    enabled=True,
                )
            )

    return sources


def load_gdelt_config(config: dict[str, Any]) -> GdeltDocApiConfig | None:
    raw_config = config.get(GDELT_CONFIG_GROUP) or {}
    if not isinstance(raw_config, dict):
        raise ValueError(f"Config group must be a mapping: {GDELT_CONFIG_GROUP}")
    if not bool(raw_config.get("enabled", False)):
        return None

    required_keys = {
        "url",
        "source",
        "source_name",
        "source_type",
        "keywords",
    }
    missing = required_keys.difference(raw_config)
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise ValueError(f"Missing key(s) in {GDELT_CONFIG_GROUP}: {missing_list}")

    keywords = raw_config.get("keywords")
    if not isinstance(keywords, list) or not keywords:
        raise ValueError("gdelt_doc_api.keywords must be a non-empty list.")

    max_records = int(raw_config.get("max_records_per_keyword", 50) or 50)
    if max_records <= 0:
        raise ValueError("gdelt_doc_api.max_records_per_keyword must be positive.")

    return GdeltDocApiConfig(
        enabled=True,
        url=str(raw_config["url"]).strip(),
        source=str(raw_config["source"]).strip(),
        source_name=str(raw_config["source_name"]).strip(),
        source_type=str(raw_config["source_type"]).strip(),
        mode=str(raw_config.get("mode") or "ArtList").strip(),
        output_format=str(raw_config.get("format") or "json").strip(),
        sort=str(raw_config.get("sort") or "HybridRel").strip(),
        max_records_per_keyword=max_records,
        startdatetime=str(raw_config.get("startdatetime") or "").strip(),
        enddatetime=str(raw_config.get("enddatetime") or "").strip(),
        keywords=[str(keyword).strip() for keyword in keywords if str(keyword).strip()],
    )


def clean_html_text(value: Any) -> str:
    if value is None:
        return ""
    text = html.unescape(str(value))
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def compact_text(parts: list[Any]) -> str:
    cleaned_parts: list[str] = []
    seen: set[str] = set()
    for part in parts:
        cleaned = clean_html_text(part)
        if not cleaned:
            continue
        fingerprint = cleaned.casefold()
        if fingerprint in seen:
            continue
        seen.add(fingerprint)
        cleaned_parts.append(cleaned)
    return " ".join(cleaned_parts).strip()


def parse_datetime_to_utc(value: Any) -> datetime | None:
    if value is None or value == "":
        return None
    parsed = pd.to_datetime(value, errors="coerce", utc=True)
    if pd.isna(parsed):
        return None
    return parsed.to_pydatetime()


def isoformat_utc(value: datetime | None) -> str:
    if value is None:
        return ""
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    value = value.astimezone(timezone.utc).replace(microsecond=0)
    return value.isoformat().replace("+00:00", "Z")


def feed_time_to_utc(entry: Any, collected_at: datetime) -> datetime:
    for key in ("published_parsed", "updated_parsed", "created_parsed"):
        parsed_tuple = entry.get(key)
        if parsed_tuple:
            return datetime(*parsed_tuple[:6], tzinfo=timezone.utc)

    for key in ("published", "updated", "created"):
        parsed = parse_datetime_to_utc(entry.get(key))
        if parsed is not None:
            return parsed

    return collected_at


def stable_hash_id(*parts: Any) -> str:
    raw = "|".join(str(part or "").strip() for part in parts)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def gdelt_item_id(url: str, title: str) -> str:
    return stable_hash_id("gdelt", url, title)


def rss_item_id(entry: Any, source_config: SourceConfig, title: str, url: str) -> str:
    raw_id = entry.get("guid") or entry.get("id") or entry.get("link")
    if raw_id:
        return str(raw_id).strip()
    return stable_hash_id(source_config.source, source_config.source_name, title, url)


def entry_content_values(entry: Any) -> list[str]:
    values: list[str] = []
    content = entry.get("content")
    if isinstance(content, list):
        for item in content:
            if isinstance(item, dict) and item.get("value"):
                values.append(str(item["value"]))
    return values


def normalize_rss_entry(entry: Any, source_config: SourceConfig, collected_at: datetime) -> dict[str, str]:
    title = clean_html_text(entry.get("title"))
    url = str(entry.get("link") or "").strip()
    summary = entry.get("summary") or entry.get("description") or ""
    content_values = entry_content_values(entry)
    text_raw = compact_text([title, summary, *content_values])
    created_at = feed_time_to_utc(entry, collected_at)

    return {
        "id": rss_item_id(entry, source_config, title, url),
        "created_at": isoformat_utc(created_at),
        "source": source_config.source,
        "source_name": source_config.source_name,
        "source_type": source_config.source_type,
        "title": title,
        "text_raw": text_raw,
        "url": url,
        "collected_at": isoformat_utc(collected_at),
    }


def get_with_retries(url: str, timeout: int, retries: int, params: dict[str, Any] | None = None) -> requests.Response:
    retry_statuses = {429, 500, 502, 503, 504}
    last_error: Exception | None = None

    for attempt in range(retries + 1):
        try:
            response = requests.get(
                url,
                headers=REQUEST_HEADERS,
                params=params,
                timeout=timeout,
            )
            if response.status_code in retry_statuses and attempt < retries:
                time.sleep(1.5 * (attempt + 1))
                continue
            response.raise_for_status()
            return response
        except requests.RequestException as exc:
            last_error = exc
            if attempt >= retries:
                raise
            time.sleep(1.5 * (attempt + 1))

    raise RuntimeError(f"Request failed after retries: {last_error}")


def collect_rss(source_config: SourceConfig, timeout: int, retries: int, collected_at: datetime) -> list[dict[str, str]]:
    response = get_with_retries(source_config.url, timeout=timeout, retries=retries)

    parsed = feedparser.parse(response.content)
    entries = getattr(parsed, "entries", [])
    if getattr(parsed, "bozo", False):
        exception = getattr(parsed, "bozo_exception", None)
        if not entries:
            raise ValueError(f"Invalid RSS/Atom feed: {exception}")
        print(f"Warning: feed parser issue for {source_config.name}: {exception}", file=sys.stderr)

    items = [
        normalize_rss_entry(entry, source_config, collected_at)
        for entry in entries
    ]
    return [item for item in items if item["id"] and item["text_raw"]]


def nvd_datetime(value: datetime) -> str:
    value = value.astimezone(timezone.utc)
    return value.strftime("%Y-%m-%dT%H:%M:%S.000")


def english_cve_description(cve: dict[str, Any]) -> str:
    descriptions = cve.get("descriptions") or []
    for description in descriptions:
        if description.get("lang") == "en":
            return clean_html_text(description.get("value"))
    return ""


def normalize_nvd_vulnerability(vulnerability: dict[str, Any], source_config: SourceConfig, collected_at: datetime) -> dict[str, str] | None:
    cve = vulnerability.get("cve") or {}
    cve_id = str(cve.get("id") or "").strip()
    if not cve_id:
        return None

    description = english_cve_description(cve)
    published = parse_datetime_to_utc(cve.get("published")) or collected_at
    return {
        "id": cve_id,
        "created_at": isoformat_utc(published),
        "source": source_config.source,
        "source_name": source_config.source_name,
        "source_type": source_config.source_type,
        "title": cve_id,
        "text_raw": description,
        "url": f"https://nvd.nist.gov/vuln/detail/{cve_id}",
        "collected_at": isoformat_utc(collected_at),
    }


def collect_nvd(source_config: SourceConfig, days: int, timeout: int, retries: int, collected_at: datetime) -> list[dict[str, str]]:
    end_date = collected_at
    start_date = end_date - timedelta(days=days)
    base_params = {
        "pubStartDate": nvd_datetime(start_date),
        "pubEndDate": nvd_datetime(end_date),
        "resultsPerPage": 2000,
    }

    all_items: list[dict[str, str]] = []
    start_index = 0
    total_results: int | None = None

    while True:
        params = {**base_params, "startIndex": start_index}
        response = get_with_retries(
            source_config.url,
            timeout=timeout,
            retries=retries,
            params=params,
        )
        payload = response.json()

        vulnerabilities = payload.get("vulnerabilities") or []
        for vulnerability in vulnerabilities:
            item = normalize_nvd_vulnerability(vulnerability, source_config, collected_at)
            if item and item["text_raw"]:
                all_items.append(item)

        total_results = int(payload.get("totalResults") or len(vulnerabilities))
        if not vulnerabilities or start_index + len(vulnerabilities) >= total_results:
            break

        start_index += len(vulnerabilities)
        time.sleep(0.6)

    return all_items


def parse_gdelt_datetime(value: Any) -> datetime | None:
    text = str(value or "").strip()
    if not text:
        return None
    if re.fullmatch(r"\d{14}", text):
        parsed = datetime.strptime(text, "%Y%m%d%H%M%S")
        return parsed.replace(tzinfo=timezone.utc)
    return parse_datetime_to_utc(text)


def normalize_gdelt_article(
    article: dict[str, Any],
    gdelt_config: GdeltDocApiConfig,
    collected_at: datetime,
) -> dict[str, str] | None:
    title = clean_html_text(article.get("title"))
    url = str(article.get("url") or article.get("url_mobile") or "").strip()
    if not title and not url:
        return None

    description = (
        article.get("snippet")
        or article.get("description")
        or article.get("summary")
        or article.get("seendescription")
        or ""
    )
    text_raw = compact_text([title, description]) or title
    if not text_raw:
        return None

    created_at = parse_gdelt_datetime(article.get("seendate")) or collected_at
    domain = str(article.get("domain") or "").strip()
    source_name = domain or gdelt_config.source_name or "gdelt"

    return {
        "id": gdelt_item_id(url, title),
        "created_at": isoformat_utc(created_at),
        "source": gdelt_config.source,
        "source_name": source_name,
        "source_type": gdelt_config.source_type,
        "title": title,
        "text_raw": text_raw,
        "url": url,
        "collected_at": isoformat_utc(collected_at),
    }


def gdelt_query_text(keyword: str) -> str:
    cleaned = keyword.strip()
    if not cleaned:
        return cleaned
    if cleaned.startswith('"') and cleaned.endswith('"'):
        return cleaned
    if " " in cleaned or "-" in cleaned:
        return f'"{cleaned}"'
    return cleaned


def gdelt_params(gdelt_config: GdeltDocApiConfig, keyword: str) -> dict[str, Any]:
    params: dict[str, Any] = {
        "query": gdelt_query_text(keyword),
        "mode": gdelt_config.mode,
        "format": gdelt_config.output_format,
        "sort": gdelt_config.sort,
        "maxrecords": gdelt_config.max_records_per_keyword,
    }
    if gdelt_config.startdatetime:
        params["startdatetime"] = gdelt_config.startdatetime
    if gdelt_config.enddatetime:
        params["enddatetime"] = gdelt_config.enddatetime
    return params


def collect_gdelt_keyword(
    gdelt_config: GdeltDocApiConfig,
    keyword: str,
    timeout: int,
    retries: int,
    collected_at: datetime,
) -> list[dict[str, str]]:
    params = gdelt_params(gdelt_config, keyword)
    try:
        response = get_with_retries(
            gdelt_config.url,
            timeout=timeout,
            retries=retries,
            params=params,
        )
    except requests.HTTPError:
        if str(params.get("sort") or "").lower() == "datedesc":
            raise
        fallback_params = {**params, "sort": "DateDesc"}
        response = get_with_retries(
            gdelt_config.url,
            timeout=timeout,
            retries=retries,
            params=fallback_params,
        )
    payload = response.json()
    articles = payload.get("articles") or []
    items = [
        normalize_gdelt_article(article, gdelt_config, collected_at)
        for article in articles
        if isinstance(article, dict)
    ]
    return [item for item in items if item and item["id"] and item["text_raw"]]


def collect_gdelt(
    gdelt_config: GdeltDocApiConfig,
    timeout: int,
    retries: int,
    collected_at: datetime,
    report: CollectionReport,
) -> list[dict[str, str]]:
    all_items: list[dict[str, str]] = []
    for keyword in gdelt_config.keywords:
        try:
            items = collect_gdelt_keyword(
                gdelt_config,
                keyword,
                timeout=timeout,
                retries=retries,
                collected_at=collected_at,
            )
            report.gdelt_keyword_counts[keyword] = len(items)
            if not items:
                report.warnings.append(f"gdelt_doc_api keyword produced no results: {keyword}")
            all_items.extend(items)
            time.sleep(GDELT_KEYWORD_DELAY_SECONDS)
        except Exception as exc:
            report.gdelt_keyword_counts[keyword] = 0
            report.gdelt_failed_keywords.append(keyword)
            warning = f"gdelt_doc_api keyword failed: {keyword}: {exc}"
            report.warnings.append(warning)
            print(f"Warning: {warning}", file=sys.stderr)
            continue
    return all_items


def read_existing_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame(columns=OUTPUT_COLUMNS)

    df = pd.read_csv(path, dtype="string", keep_default_na=False)
    for column in OUTPUT_COLUMNS:
        if column not in df.columns:
            df[column] = ""
    return df[OUTPUT_COLUMNS].copy()


def item_duplicate(item: dict[str, str], seen_ids: set[str], seen_urls: set[str]) -> bool:
    item_id = str(item.get("id") or "").strip()
    item_url = str(item.get("url") or "").strip()
    return bool(item_id and item_id in seen_ids) or bool(item_url and item_url in seen_urls)


def register_item(item: dict[str, str], seen_ids: set[str], seen_urls: set[str]) -> None:
    item_id = str(item.get("id") or "").strip()
    item_url = str(item.get("url") or "").strip()
    if item_id:
        seen_ids.add(item_id)
    if item_url:
        seen_urls.add(item_url)


def dedupe_new_items(existing: pd.DataFrame, collected_items: list[dict[str, str]]) -> tuple[list[dict[str, str]], int]:
    seen_ids = {str(value).strip() for value in existing["id"].dropna().tolist() if str(value).strip()}
    seen_urls = {str(value).strip() for value in existing["url"].dropna().tolist() if str(value).strip()}
    new_items: list[dict[str, str]] = []
    duplicates = 0

    for item in collected_items:
        normalized_item = {column: str(item.get(column) or "").strip() for column in OUTPUT_COLUMNS}
        if item_duplicate(normalized_item, seen_ids, seen_urls):
            duplicates += 1
            continue
        register_item(normalized_item, seen_ids, seen_urls)
        new_items.append(normalized_item)

    return new_items, duplicates


def write_outputs(final_df: pd.DataFrame, output_path: Path, archive_dir: Path, collected_at: datetime) -> Path:
    final_df.to_csv(output_path, index=False, encoding="utf-8")
    timestamp = collected_at.strftime("%Y%m%d_%H%M%S")
    archive_path = archive_dir / f"live_items_raw_{timestamp}.csv"
    final_df.to_csv(archive_path, index=False, encoding="utf-8")
    return archive_path


def created_at_range(df: pd.DataFrame) -> tuple[str, str]:
    if df.empty or "created_at" not in df.columns:
        return "", ""
    dates = pd.to_datetime(df["created_at"], errors="coerce", utc=True).dropna()
    if dates.empty:
        return "", ""
    return isoformat_utc(dates.min().to_pydatetime()), isoformat_utc(dates.max().to_pydatetime())


def print_report(report: CollectionReport, output_path: Path, archive_path: Path) -> None:
    print("\nLive collection report")
    print("======================")
    print(f"User-Agent: {USER_AGENT}")
    print(f"Fonti abilitate: {len(report.enabled_sources)}")
    for source_name in report.enabled_sources:
        print(f"  - {source_name}")
    print("Item raccolti per source_name:")
    for source_name, count in sorted(report.source_name_counts.items(), key=lambda item: (-item[1], item[0])):
        print(f"  - {source_name}: {count}")
    print("Item raccolti per source_type:")
    for source_type, count in sorted(report.source_type_counts.items(), key=lambda item: (-item[1], item[0])):
        print(f"  - {source_type}: {count}")
    print("Item raccolti per config source:")
    for source_name, count in report.source_counts.items():
        print(f"  - {source_name}: {count}")
    if report.gdelt_keyword_counts:
        print("Item raccolti da GDELT per keyword:")
        for keyword, count in report.gdelt_keyword_counts.items():
            print(f"  - {keyword}: {count}")
    print(f"Item totali raccolti in questa run: {report.collected_this_run}")
    print(f"Nuovi item aggiunti: {report.new_items_added}")
    print(f"Duplicati scartati: {report.duplicates_discarded}")
    print(f"Righe totali nel CSV finale: {report.final_rows}")
    print(f"Range created_at minimo/massimo: {report.min_created_at or 'n/a'} -> {report.max_created_at or 'n/a'}")
    print(f"CSV finale: {output_path}")
    print(f"Copia archive: {archive_path}")
    print(f"Fonti fallite: {len(report.failed_sources)}")
    for failed_source in report.failed_sources:
        print(f"  - {failed_source}")
    if report.gdelt_failed_keywords:
        print("Keyword GDELT fallite:")
        for keyword in report.gdelt_failed_keywords:
            print(f"  - {keyword}")
    if report.warnings:
        print("Warning:")
        for warning in report.warnings:
            print(f"  - {warning}")


def add_count(target: dict[str, int], key: str, count: int) -> None:
    target[key] = target.get(key, 0) + count


def main() -> int:
    args = parse_args()
    config_path = resolve_project_path(args.config)
    output_path = resolve_project_path(args.output)
    archive_dir = resolve_project_path(args.archive_dir)
    ensure_live_dirs(output_path, archive_dir)

    collected_at = datetime.now(timezone.utc)
    report = CollectionReport()

    try:
        config = load_config(config_path)
        enabled_sources = iter_enabled_sources(config)
        gdelt_config = load_gdelt_config(config)
    except Exception as exc:
        print(f"Config error: {exc}", file=sys.stderr)
        return 1

    report.enabled_sources = [f"{source.group}:{source.name}" for source in enabled_sources]
    if gdelt_config is not None:
        report.enabled_sources.append("gdelt_doc_api")

    collected_items: list[dict[str, str]] = []
    for source_config in enabled_sources:
        try:
            if source_config.group in RSS_GROUPS:
                items = collect_rss(source_config, args.timeout, args.retries, collected_at)
            elif source_config.group == "nvd_api":
                items = collect_nvd(source_config, args.nvd_days, args.timeout, args.retries, collected_at)
            else:
                items = []
            report.source_counts[source_config.name] = len(items)
            add_count(report.source_name_counts, source_config.source_name, len(items))
            add_count(report.source_type_counts, source_config.source_type, len(items))
            collected_items.extend(items)
        except Exception as exc:
            report.source_counts[source_config.name] = 0
            add_count(report.source_name_counts, source_config.source_name, 0)
            add_count(report.source_type_counts, source_config.source_type, 0)
            failed_source = (
                f"{source_config.group}:{source_config.name} "
                f"({source_config.source_name}, {source_config.source_type})"
            )
            report.failed_sources.append(failed_source)
            warning = f"{failed_source} failed: {exc}"
            report.warnings.append(warning)
            print(f"Warning: {warning}", file=sys.stderr)
            continue

    if gdelt_config is not None:
        try:
            gdelt_items = collect_gdelt(gdelt_config, args.timeout, args.retries, collected_at, report)
            report.source_counts["gdelt_doc_api"] = len(gdelt_items)
            for gdelt_item in gdelt_items:
                add_count(report.source_name_counts, gdelt_item["source_name"], 1)
            add_count(report.source_type_counts, gdelt_config.source_type, len(gdelt_items))
            collected_items.extend(gdelt_items)
        except Exception as exc:
            report.source_counts["gdelt_doc_api"] = 0
            add_count(report.source_name_counts, gdelt_config.source_name, 0)
            add_count(report.source_type_counts, gdelt_config.source_type, 0)
            failed_source = f"gdelt_doc_api ({gdelt_config.source_name}, {gdelt_config.source_type})"
            report.failed_sources.append(failed_source)
            warning = f"{failed_source} failed: {exc}"
            report.warnings.append(warning)
            print(f"Warning: {warning}", file=sys.stderr)

    report.collected_this_run = len(collected_items)

    existing = read_existing_csv(output_path)
    new_items, duplicates = dedupe_new_items(existing, collected_items)
    report.new_items_added = len(new_items)
    report.duplicates_discarded = duplicates

    new_df = pd.DataFrame(new_items, columns=OUTPUT_COLUMNS)
    final_df = pd.concat([existing, new_df], ignore_index=True)
    final_df = final_df[OUTPUT_COLUMNS].fillna("")
    archive_path = write_outputs(final_df, output_path, archive_dir, collected_at)

    report.final_rows = len(final_df)
    report.min_created_at, report.max_created_at = created_at_range(final_df)
    print_report(report, output_path, archive_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
