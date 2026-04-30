"""
Check the quality of the live social/news preprocessed corpus before live LDA.

This diagnostic script is read-only: it does not modify datasets and does not
run LDA, VADER, temporal aggregation, P2, or dashboard export.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "03_live_preprocessed_dataset.csv"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "live" / "live_corpus_quality_check.md"
DEFAULT_SAMPLES_PATH = PROJECT_ROOT / "reports" / "live" / "live_corpus_samples.csv"

REQUIRED_COLUMNS = [
    "id",
    "created_at",
    "source_type",
    "source_name",
    "title",
    "text_raw",
    "text_clean",
]

SAMPLE_COLUMNS = [
    "id",
    "created_at",
    "source_type",
    "source_name",
    "title",
    "text_raw",
    "text_clean",
]

KEYWORDS = [
    "cve",
    "vulnerability",
    "ransomware",
    "malware",
    "phishing",
    "breach",
    "exploit",
    "ddos",
    "botnet",
    "zeroday",
    "zero-day",
    "data leak",
]

SAMPLE_SOURCE_TYPES = ["reddit_rss", "news_rss", "news_api"]
ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")
RANDOM_STATE = 42


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Quality-check the live social/news preprocessed corpus before LDA."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_PATH)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT_PATH)
    parser.add_argument("--samples-output", type=Path, default=DEFAULT_SAMPLES_PATH)
    return parser.parse_args()


def resolve_project_path(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


def validate_file(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"{label} not found: {path}")
    if not path.is_file():
        raise FileNotFoundError(f"{label} is not a file: {path}")


def read_csv_with_encoding_fallback(input_path: Path) -> tuple[pd.DataFrame, str]:
    last_error: UnicodeDecodeError | None = None

    for encoding in ENCODINGS_TO_TRY:
        try:
            df = pd.read_csv(input_path, dtype="string", encoding=encoding, low_memory=False)
            return df, encoding
        except UnicodeDecodeError as exc:
            last_error = exc

    raise UnicodeDecodeError(
        last_error.encoding if last_error else "unknown",
        last_error.object if last_error else b"",
        last_error.start if last_error else 0,
        last_error.end if last_error else 1,
        f"Could not decode CSV with encodings: {', '.join(ENCODINGS_TO_TRY)}",
    )


def validate_columns(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("Input CSV is empty.")

    duplicate_columns = sorted(df.columns[df.columns.duplicated()].unique())
    if duplicate_columns:
        duplicates = ", ".join(duplicate_columns)
        raise ValueError(f"Duplicate column name(s) found in CSV: {duplicates}")

    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        missing = ", ".join(missing_columns)
        available = ", ".join(df.columns)
        raise ValueError(f"Missing required column(s): {missing}\nAvailable columns: {available}")


def percentage(part: int | float, total: int | float) -> float:
    if not total:
        return 0.0
    return round((float(part) / float(total)) * 100.0, 2)


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(value) for value in row) + " |")
    return "\n".join(lines)


def token_lengths(series: pd.Series) -> pd.Series:
    return series.fillna("").astype("string").map(lambda value: len(str(value).split()))


def text_lengths(series: pd.Series) -> pd.Series:
    return series.fillna("").astype("string").map(lambda value: len(str(value)))


def distribution_rows(df: pd.DataFrame, column: str, top_n: int | None = None) -> list[list[object]]:
    counts = (
        df[column]
        .fillna("UNKNOWN")
        .astype("string")
        .replace("", "UNKNOWN")
        .value_counts()
        .rename_axis(column)
        .reset_index(name="rows")
    )
    if top_n is not None:
        counts = counts.head(top_n)
    total = len(df)
    return [
        [getattr(row, column), int(row.rows), f"{percentage(row.rows, total):.2f}%"]
        for row in counts.itertuples(index=False)
    ]


def keyword_pattern(keyword: str) -> re.Pattern[str]:
    escaped = re.escape(keyword)
    if " " in keyword:
        escaped = escaped.replace(r"\ ", r"\s+")
    return re.compile(rf"(?<![a-z0-9]){escaped}(?![a-z0-9])", flags=re.IGNORECASE)


def keyword_coverage_rows(df: pd.DataFrame) -> list[list[object]]:
    text = (
        df["text_raw"].fillna("").astype("string")
        + " "
        + df["text_clean"].fillna("").astype("string")
        + " "
        + df["title"].fillna("").astype("string")
    )
    rows = []
    total = len(df)
    for keyword in KEYWORDS:
        pattern = keyword_pattern(keyword)
        count = int(text.map(lambda value: bool(pattern.search(str(value)))).sum())
        rows.append([keyword, count, f"{percentage(count, total):.2f}%"])
    return rows


def top_tokens(series: pd.Series, top_n: int) -> list[tuple[str, int]]:
    counter: Counter[str] = Counter()
    for text in series.fillna("").astype(str):
        counter.update(text.split())
    return counter.most_common(top_n)


def token_rows(tokens: list[tuple[str, int]]) -> list[list[object]]:
    return [[token, int(count)] for token, count in tokens]


def top_tokens_by_source_type_rows(df: pd.DataFrame, top_n: int = 30) -> list[list[object]]:
    rows = []
    for source_type, group in df.groupby("source_type", dropna=False):
        label = "UNKNOWN" if pd.isna(source_type) else str(source_type)
        for rank, (token, count) in enumerate(top_tokens(group["text_clean"], top_n), start=1):
            rows.append([label, rank, token, int(count)])
    return rows


def build_samples(df: pd.DataFrame) -> pd.DataFrame:
    samples = []
    for source_type in SAMPLE_SOURCE_TYPES:
        group = df.loc[df["source_type"].fillna("").astype("string").eq(source_type)]
        if group.empty:
            continue
        sample_size = min(20, len(group))
        samples.append(group.sample(n=sample_size, random_state=RANDOM_STATE)[SAMPLE_COLUMNS])
    if not samples:
        return pd.DataFrame(columns=SAMPLE_COLUMNS)
    return pd.concat(samples, ignore_index=True)


def build_warnings(df: pd.DataFrame, mean_clean_tokens: float, keyword_rows: list[list[object]]) -> list[str]:
    warnings: list[str] = []
    total = len(df)
    source_type_share = df["source_type"].fillna("UNKNOWN").astype("string").value_counts(normalize=True)
    if float(source_type_share.get("news_api", 0.0)) > 0.70:
        warnings.append("news_api supera il 70% del corpus preprocessato.")

    keyword_counts = {str(row[0]): int(row[1]) for row in keyword_rows}
    cve_vulnerability_docs = max(
        keyword_counts.get("cve", 0),
        keyword_counts.get("vulnerability", 0),
    )
    if percentage(cve_vulnerability_docs, total) > 50:
        warnings.append("Piu del 50% dei documenti contiene cve o vulnerability.")

    source_name_share = df["source_name"].fillna("UNKNOWN").astype("string").value_counts(normalize=True)
    if not source_name_share.empty and float(source_name_share.iloc[0]) > 0.20:
        source_name = source_name_share.index[0]
        warnings.append(f"Una singola source_name supera il 20% del corpus: {source_name}.")

    if mean_clean_tokens < 5:
        warnings.append("La lunghezza media di text_clean e sotto 5 token.")

    return warnings


def build_report(df: pd.DataFrame, encoding_used: str) -> str:
    created_at = pd.to_datetime(df["created_at"], errors="coerce", utc=True)
    raw_lengths = text_lengths(df["text_raw"])
    clean_lengths = token_lengths(df["text_clean"])
    keyword_rows = keyword_coverage_rows(df)
    warnings = build_warnings(df, float(clean_lengths.mean()), keyword_rows)

    sections = [
        "# Live Corpus Quality Check",
        "Diagnostic report for `data/live/processed/03_live_preprocessed_dataset.csv`. This report does not modify the dataset and does not run LDA, VADER, P2, or dashboard export.",
        "## Summary",
        markdown_table(
            ["Metric", "Value"],
            [
                ["Total rows", len(df)],
                ["created_at min", created_at.min().isoformat() if created_at.notna().any() else ""],
                ["created_at max", created_at.max().isoformat() if created_at.notna().any() else ""],
                ["Mean text_raw length", f"{float(raw_lengths.mean()):.2f}"],
                ["Median text_raw length", f"{float(raw_lengths.median()):.2f}"],
                ["Mean text_clean tokens", f"{float(clean_lengths.mean()):.2f}"],
                ["Median text_clean tokens", f"{float(clean_lengths.median()):.2f}"],
                ["Encoding used", encoding_used],
            ],
        ),
    ]

    if warnings:
        sections.extend(
            [
                "## Warnings",
                "\n".join(f"- WARNING: {warning}" for warning in warnings),
            ]
        )
    else:
        sections.extend(["## Warnings", "No warning thresholds triggered."])

    sections.extend(
        [
            "## Source Type Distribution",
            markdown_table(["source_type", "rows", "percent_dataset"], distribution_rows(df, "source_type")),
            "## Source Name Distribution Top 30",
            markdown_table(["source_name", "rows", "percent_dataset"], distribution_rows(df, "source_name", top_n=30)),
            "## Keyword Coverage",
            markdown_table(["keyword", "documents", "percent_dataset"], keyword_rows),
            "## Top 50 Global Tokens",
            markdown_table(["token", "count"], token_rows(top_tokens(df["text_clean"], 50))),
            "## Top 30 Tokens by Source Type",
            markdown_table(
                ["source_type", "rank", "token", "count"],
                top_tokens_by_source_type_rows(df, top_n=30),
            ),
            "## Methodological Note",
            "Questo controllo valuta il corpus social/news preprocessato prima di un eventuale nuovo LDA live. Non usa CVE/NVD come fonte primaria e non calcola sentiment o P2.",
        ]
    )
    return "\n\n".join(sections) + "\n"


def write_outputs(samples: pd.DataFrame, report: str, samples_path: Path, report_path: Path) -> None:
    samples_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    samples.to_csv(samples_path, index=False, encoding="utf-8")
    report_path.write_text(report, encoding="utf-8")


def print_summary(df: pd.DataFrame, samples: pd.DataFrame, report_path: Path, samples_path: Path) -> None:
    print("Live corpus quality check")
    print("=========================")
    print(f"Rows: {len(df)}")
    print(f"Source types: {df['source_type'].value_counts().to_dict()}")
    print(f"Samples exported: {len(samples)}")
    print(f"Report: {report_path}")
    print(f"Samples CSV: {samples_path}")


def main() -> int:
    args = parse_args()
    input_path = resolve_project_path(args.input)
    report_path = resolve_project_path(args.report)
    samples_path = resolve_project_path(args.samples_output)

    try:
        validate_file(input_path, "Input CSV")
        df, encoding_used = read_csv_with_encoding_fallback(input_path)
        validate_columns(df)
        samples = build_samples(df)
        report = build_report(df, encoding_used)
        write_outputs(samples, report, samples_path, report_path)
        print_summary(df, samples, report_path, samples_path)
    except Exception as exc:
        print(f"Live corpus quality check error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
