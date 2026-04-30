"""
Inspect the raw live dataset collected by 00_collect_live_sources.py.

This script is diagnostic only. It does not modify the live dataset and does
not run preprocessing, topic modeling, sentiment analysis, P2, or dashboard
export.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import re
import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "raw" / "live_items_raw.csv"
REPORTS_LIVE_DIR = PROJECT_ROOT / "reports" / "live"
DEFAULT_MARKDOWN_OUTPUT = REPORTS_LIVE_DIR / "live_dataset_inspection.md"
DEFAULT_DISTRIBUTION_OUTPUT = REPORTS_LIVE_DIR / "live_source_distribution.csv"

REQUIRED_COLUMNS = [
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

BASE_STOPWORDS = {
    "a",
    "about",
    "above",
    "after",
    "again",
    "against",
    "all",
    "am",
    "an",
    "and",
    "any",
    "are",
    "as",
    "at",
    "be",
    "because",
    "been",
    "before",
    "being",
    "below",
    "between",
    "both",
    "but",
    "by",
    "can",
    "could",
    "did",
    "do",
    "does",
    "doing",
    "down",
    "during",
    "each",
    "few",
    "for",
    "from",
    "further",
    "had",
    "has",
    "have",
    "having",
    "he",
    "her",
    "here",
    "hers",
    "herself",
    "him",
    "himself",
    "his",
    "how",
    "i",
    "if",
    "in",
    "into",
    "is",
    "it",
    "its",
    "itself",
    "just",
    "me",
    "more",
    "most",
    "my",
    "myself",
    "no",
    "nor",
    "not",
    "now",
    "of",
    "off",
    "on",
    "once",
    "only",
    "or",
    "other",
    "our",
    "ours",
    "ourselves",
    "out",
    "over",
    "own",
    "same",
    "she",
    "should",
    "so",
    "some",
    "such",
    "than",
    "that",
    "the",
    "their",
    "theirs",
    "them",
    "themselves",
    "then",
    "there",
    "these",
    "they",
    "this",
    "those",
    "through",
    "to",
    "too",
    "under",
    "until",
    "up",
    "very",
    "was",
    "we",
    "were",
    "what",
    "when",
    "where",
    "which",
    "while",
    "who",
    "whom",
    "why",
    "will",
    "with",
    "you",
    "your",
    "yours",
    "yourself",
    "yourselves",
    "via",
}


@dataclass(frozen=True)
class DuplicateStats:
    duplicate_rows: int
    duplicate_values: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect quality of the raw live cybersecurity dataset."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="Path to data/live/raw/live_items_raw.csv.",
    )
    parser.add_argument(
        "--markdown-output",
        type=Path,
        default=DEFAULT_MARKDOWN_OUTPUT,
        help="Path to the Markdown inspection report.",
    )
    parser.add_argument(
        "--distribution-output",
        type=Path,
        default=DEFAULT_DISTRIBUTION_OUTPUT,
        help="Path to the source distribution CSV.",
    )
    return parser.parse_args()


def resolve_project_path(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


def load_live_dataset(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Input CSV not found: {path}")
    if path.suffix.lower() != ".csv":
        raise ValueError(f"Input file must be a CSV: {path}")
    return pd.read_csv(path, dtype="string")


def validate_columns(df: pd.DataFrame) -> None:
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        missing = ", ".join(missing_columns)
        available = ", ".join(df.columns)
        raise ValueError(f"Missing required column(s): {missing}\nAvailable columns: {available}")


def as_clean_string(series: pd.Series) -> pd.Series:
    return series.fillna("").astype("string").str.strip()


def parse_utc_dates(series: pd.Series) -> pd.Series:
    return pd.to_datetime(series, errors="coerce", utc=True)


def iso_or_na(value: pd.Timestamp | None) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return value.to_pydatetime().replace(microsecond=0).isoformat().replace("+00:00", "Z")


def duplicate_stats(series: pd.Series, normalize: bool = False) -> DuplicateStats:
    cleaned = as_clean_string(series)
    if normalize:
        cleaned = cleaned.str.lower().str.replace(r"\s+", " ", regex=True)
    non_empty = cleaned[cleaned.ne("")]
    duplicated = non_empty.duplicated(keep=False)
    duplicate_rows = int(duplicated.sum())
    duplicate_values = int(non_empty[duplicated].nunique()) if duplicate_rows else 0
    return DuplicateStats(duplicate_rows=duplicate_rows, duplicate_values=duplicate_values)


def source_type_distribution(df: pd.DataFrame) -> pd.DataFrame:
    total_rows = len(df)
    counts = (
        as_clean_string(df["source_type"])
        .replace("", "UNKNOWN")
        .value_counts()
        .rename_axis("source_type")
        .reset_index(name="rows")
    )
    counts["percent_dataset"] = counts["rows"].apply(lambda count: percentage(count, total_rows))
    return counts


def source_distribution(df: pd.DataFrame) -> pd.DataFrame:
    total_rows = len(df)
    working = df[["source_type", "source_name"]].copy()
    working["source_type"] = as_clean_string(working["source_type"]).replace("", "UNKNOWN")
    working["source_name"] = as_clean_string(working["source_name"]).replace("", "UNKNOWN")

    grouped = (
        working.groupby(["source_type", "source_name"], dropna=False)
        .size()
        .reset_index(name="rows")
        .sort_values(["rows", "source_type", "source_name"], ascending=[False, True, True])
    )
    grouped["percent_dataset"] = grouped["rows"].apply(lambda count: percentage(count, total_rows))

    source_type_totals = working.groupby("source_type", dropna=False).size().rename("source_type_rows")
    grouped = grouped.merge(source_type_totals, on="source_type", how="left")
    grouped["percent_source_type"] = grouped.apply(
        lambda row: percentage(row["rows"], row["source_type_rows"]),
        axis=1,
    )
    return grouped[["source_type", "source_name", "rows", "percent_dataset", "percent_source_type"]]


def percentage(part: int | float, total: int | float) -> float:
    if not total:
        return 0.0
    return round((float(part) / float(total)) * 100.0, 2)


def tokens_for_inspection(text: str) -> list[str]:
    tokens = re.findall(r"[a-z][a-z0-9_-]{2,}", text.lower())
    return [token for token in tokens if token not in BASE_STOPWORDS and not token.isdigit()]


def top_words_by_source_type(df: pd.DataFrame, top_n: int = 30) -> dict[str, list[tuple[str, int]]]:
    results: dict[str, list[tuple[str, int]]] = {}
    working = df[["source_type", "text_raw"]].copy()
    working["source_type"] = as_clean_string(working["source_type"]).replace("", "UNKNOWN")
    working["text_raw"] = working["text_raw"].fillna("").astype(str)

    for source_type, rows in working.groupby("source_type", dropna=False):
        counter: Counter[str] = Counter()
        for text in rows["text_raw"]:
            counter.update(tokens_for_inspection(text))
        results[str(source_type)] = counter.most_common(top_n)
    return results


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(value) for value in row) + " |")
    return "\n".join(lines)


def build_warnings(
    source_type_dist: pd.DataFrame,
    total_rows: int,
    short_lt_30: int,
    duplicate_id: DuplicateStats,
    duplicate_url: DuplicateStats,
    duplicate_text: DuplicateStats,
    invalid_created_at: int,
) -> list[str]:
    warnings: list[str] = []
    for row in source_type_dist.itertuples(index=False):
        if float(row.percent_dataset) > 70.0:
            warnings.append(
                f"source_type `{row.source_type}` represents {row.percent_dataset:.2f}% of the dataset."
            )

    short_pct = percentage(short_lt_30, total_rows)
    if short_pct > 10.0:
        warnings.append(f"text_raw shorter than 30 chars is {short_pct:.2f}% of rows.")

    if duplicate_id.duplicate_rows:
        warnings.append(f"Duplicate id rows found: {duplicate_id.duplicate_rows}.")
    if duplicate_url.duplicate_rows:
        warnings.append(f"Duplicate url rows found: {duplicate_url.duplicate_rows}.")
    if duplicate_text.duplicate_rows:
        warnings.append(f"Duplicate normalized text_raw rows found: {duplicate_text.duplicate_rows}.")

    invalid_created_pct = percentage(invalid_created_at, total_rows)
    if invalid_created_pct > 5.0:
        warnings.append(f"Unparsable created_at rows are {invalid_created_pct:.2f}% of the dataset.")

    return warnings


def describe_dataset(df: pd.DataFrame) -> dict[str, object]:
    total_rows = len(df)
    created_at = parse_utc_dates(df["created_at"])
    collected_at = parse_utc_dates(df["collected_at"])
    text = as_clean_string(df["text_raw"])
    text_lengths = text.str.len()

    duplicate_id = duplicate_stats(df["id"])
    duplicate_url = duplicate_stats(df["url"])
    duplicate_text = duplicate_stats(df["text_raw"], normalize=True)
    source_type_dist = source_type_distribution(df)

    invalid_created_at = int(created_at.isna().sum())
    invalid_collected_at = int(collected_at.isna().sum())
    short_lt_30 = int(text_lengths.lt(30).sum())
    short_lt_100 = int(text_lengths.lt(100).sum())
    empty_texts = int(text.eq("").sum())

    return {
        "total_rows": total_rows,
        "source_type_dist": source_type_dist,
        "source_name_counts": as_clean_string(df["source_name"]).replace("", "UNKNOWN").value_counts(),
        "created_min": iso_or_na(created_at.min()),
        "created_max": iso_or_na(created_at.max()),
        "collected_min": iso_or_na(collected_at.min()),
        "collected_max": iso_or_na(collected_at.max()),
        "invalid_created_at": invalid_created_at,
        "invalid_collected_at": invalid_collected_at,
        "empty_texts": empty_texts,
        "mean_text_length": round(float(text_lengths.mean()), 2) if total_rows else 0.0,
        "median_text_length": round(float(text_lengths.median()), 2) if total_rows else 0.0,
        "min_text_length": int(text_lengths.min()) if total_rows else 0,
        "max_text_length": int(text_lengths.max()) if total_rows else 0,
        "short_lt_30": short_lt_30,
        "short_lt_100": short_lt_100,
        "duplicate_id": duplicate_id,
        "duplicate_url": duplicate_url,
        "duplicate_text": duplicate_text,
        "top_words": top_words_by_source_type(df),
    }


def build_markdown_report(summary: dict[str, object], distribution: pd.DataFrame) -> str:
    total_rows = int(summary["total_rows"])
    duplicate_id: DuplicateStats = summary["duplicate_id"]  # type: ignore[assignment]
    duplicate_url: DuplicateStats = summary["duplicate_url"]  # type: ignore[assignment]
    duplicate_text: DuplicateStats = summary["duplicate_text"]  # type: ignore[assignment]
    source_type_dist: pd.DataFrame = summary["source_type_dist"]  # type: ignore[assignment]

    warnings = build_warnings(
        source_type_dist=source_type_dist,
        total_rows=total_rows,
        short_lt_30=int(summary["short_lt_30"]),
        duplicate_id=duplicate_id,
        duplicate_url=duplicate_url,
        duplicate_text=duplicate_text,
        invalid_created_at=int(summary["invalid_created_at"]),
    )

    source_type_rows = [
        [row.source_type, int(row.rows), f"{float(row.percent_dataset):.2f}%"]
        for row in source_type_dist.itertuples(index=False)
    ]
    source_name_counts: pd.Series = summary["source_name_counts"]  # type: ignore[assignment]
    source_name_rows = [
        [source_name, int(count), f"{percentage(count, total_rows):.2f}%"]
        for source_name, count in source_name_counts.items()
    ]
    distribution_rows = [
        [
            row.source_type,
            row.source_name,
            int(row.rows),
            f"{float(row.percent_dataset):.2f}%",
            f"{float(row.percent_source_type):.2f}%",
        ]
        for row in distribution.itertuples(index=False)
    ]

    top_words_lines: list[str] = []
    top_words: dict[str, list[tuple[str, int]]] = summary["top_words"]  # type: ignore[assignment]
    for source_type in sorted(top_words):
        pairs = top_words[source_type]
        formatted = ", ".join(f"{word} ({count})" for word, count in pairs) or "n/a"
        top_words_lines.append(f"### {source_type}\n\n{formatted}")

    warning_lines = "\n".join(f"- WARNING: {warning}" for warning in warnings) if warnings else "- No warning triggered."

    return "\n\n".join(
        [
            "# Live Dataset Inspection",
            "Diagnostic report for `data/live/raw/live_items_raw.csv`. This report does not modify the dataset and does not run NLP preprocessing, topic modeling, sentiment analysis, P2, or dashboard export.",
            "## Summary",
            markdown_table(
                ["Metric", "Value"],
                [
                    ["Total rows", total_rows],
                    ["created_at min", summary["created_min"]],
                    ["created_at max", summary["created_max"]],
                    ["collected_at min", summary["collected_min"]],
                    ["collected_at max", summary["collected_max"]],
                    ["Unparsable created_at", f"{summary['invalid_created_at']} ({percentage(int(summary['invalid_created_at']), total_rows):.2f}%)"],
                    ["Unparsable collected_at", f"{summary['invalid_collected_at']} ({percentage(int(summary['invalid_collected_at']), total_rows):.2f}%)"],
                    ["Null/empty text_raw", f"{summary['empty_texts']} ({percentage(int(summary['empty_texts']), total_rows):.2f}%)"],
                    ["Mean text_raw length", summary["mean_text_length"]],
                    ["Median text_raw length", summary["median_text_length"]],
                    ["Min text_raw length", summary["min_text_length"]],
                    ["Max text_raw length", summary["max_text_length"]],
                    ["text_raw < 30 chars", f"{summary['short_lt_30']} ({percentage(int(summary['short_lt_30']), total_rows):.2f}%)"],
                    ["text_raw < 100 chars", f"{summary['short_lt_100']} ({percentage(int(summary['short_lt_100']), total_rows):.2f}%)"],
                    ["Duplicate id rows", f"{duplicate_id.duplicate_rows} rows / {duplicate_id.duplicate_values} values"],
                    ["Duplicate url rows", f"{duplicate_url.duplicate_rows} rows / {duplicate_url.duplicate_values} values"],
                    ["Duplicate normalized text_raw rows", f"{duplicate_text.duplicate_rows} rows / {duplicate_text.duplicate_values} values"],
                ],
            ),
            "## Warnings",
            warning_lines,
            "## Rows By source_type",
            markdown_table(["source_type", "rows", "percent_dataset"], source_type_rows),
            "## Rows By source_name",
            markdown_table(["source_name", "rows", "percent_dataset"], source_name_rows),
            "## Source Distribution",
            markdown_table(
                ["source_type", "source_name", "rows", "percent_dataset", "percent_source_type"],
                distribution_rows,
            ),
            "## Top 30 Inspection Words By source_type",
            "\n\n".join(top_words_lines),
        ]
    ) + "\n"


def write_reports(markdown: str, distribution: pd.DataFrame, markdown_output: Path, distribution_output: Path) -> None:
    markdown_output.parent.mkdir(parents=True, exist_ok=True)
    distribution_output.parent.mkdir(parents=True, exist_ok=True)
    markdown_output.write_text(markdown, encoding="utf-8")
    distribution.to_csv(distribution_output, index=False, encoding="utf-8")


def print_console_summary(summary: dict[str, object], markdown_output: Path, distribution_output: Path) -> None:
    total_rows = int(summary["total_rows"])
    duplicate_id: DuplicateStats = summary["duplicate_id"]  # type: ignore[assignment]
    duplicate_url: DuplicateStats = summary["duplicate_url"]  # type: ignore[assignment]
    duplicate_text: DuplicateStats = summary["duplicate_text"]  # type: ignore[assignment]
    source_type_dist: pd.DataFrame = summary["source_type_dist"]  # type: ignore[assignment]
    warnings = build_warnings(
        source_type_dist=source_type_dist,
        total_rows=total_rows,
        short_lt_30=int(summary["short_lt_30"]),
        duplicate_id=duplicate_id,
        duplicate_url=duplicate_url,
        duplicate_text=duplicate_text,
        invalid_created_at=int(summary["invalid_created_at"]),
    )

    print("Live dataset inspection")
    print("=======================")
    print(f"Rows: {total_rows}")
    print(f"created_at: {summary['created_min']} -> {summary['created_max']}")
    print(f"collected_at: {summary['collected_min']} -> {summary['collected_max']}")
    print(f"Empty text_raw: {summary['empty_texts']}")
    print(f"text_raw < 30 chars: {summary['short_lt_30']}")
    print(f"text_raw < 100 chars: {summary['short_lt_100']}")
    print(f"Duplicate id/url/text rows: {duplicate_id.duplicate_rows}/{duplicate_url.duplicate_rows}/{duplicate_text.duplicate_rows}")
    print("Rows by source_type:")
    for row in source_type_dist.itertuples(index=False):
        print(f"  - {row.source_type}: {int(row.rows)} ({float(row.percent_dataset):.2f}%)")
    print(f"Warnings: {len(warnings)}")
    for warning in warnings:
        print(f"  - {warning}")
    print(f"Markdown report: {markdown_output}")
    print(f"Source distribution CSV: {distribution_output}")


def main() -> int:
    args = parse_args()
    input_path = resolve_project_path(args.input)
    markdown_output = resolve_project_path(args.markdown_output)
    distribution_output = resolve_project_path(args.distribution_output)

    try:
        df = load_live_dataset(input_path)
        validate_columns(df)
        df = df[REQUIRED_COLUMNS].copy()
        summary = describe_dataset(df)
        distribution = source_distribution(df)
        markdown = build_markdown_report(summary, distribution)
        write_reports(markdown, distribution, markdown_output, distribution_output)
        print_console_summary(summary, markdown_output, distribution_output)
    except Exception as exc:
        print(f"Inspection error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
