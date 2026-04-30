"""
Prepare the live social/news dataset used by the P2 replication pipeline.

The P2 live pipeline follows the paper-style setup based on social/news
aggregation. CVE/NVD records remain available in the raw collection as future
technical context, but they are excluded from sentiment, temporal aggregation,
P2, CYBERCON, and dashboard inputs.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "raw" / "live_items_raw.csv"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "01_live_social_news_dataset.csv"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "live" / "live_social_news_dataset_report.md"

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

P2_SOURCE_TYPES = {"reddit_rss", "news_rss", "news_api", "social_news_api"}
ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")
WHITESPACE_PATTERN = re.compile(r"\s+")
METHODOLOGICAL_NOTE = (
    "Il dataset P2 live usa solo social/news sources per coerenza con il paper. "
    "CVE/NVD è escluso perché fonte tecnico-descrittiva e non sentiment-bearing."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare live social/news records for the P2 replication pipeline."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT_PATH)
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


def normalize_text_for_dedupe(value: object) -> str:
    text = "" if pd.isna(value) else str(value)
    text = text.lower().strip()
    return WHITESPACE_PATTERN.sub(" ", text)


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


def distribution_rows(df: pd.DataFrame, column: str) -> list[list[object]]:
    counts = (
        df[column]
        .fillna("UNKNOWN")
        .astype("string")
        .replace("", "UNKNOWN")
        .value_counts()
        .rename_axis(column)
        .reset_index(name="rows")
    )
    total = int(counts["rows"].sum())
    return [
        [getattr(row, column), int(row.rows), f"{percentage(row.rows, total):.2f}%"]
        for row in counts.itertuples(index=False)
    ]


def prepare_social_news_dataset(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, int]]:
    validate_columns(df)

    raw_rows = len(df)
    cve_excluded = int(df["source_type"].fillna("").astype("string").eq("cve").sum())

    social_news = df.loc[df["source_type"].isin(P2_SOURCE_TYPES)].copy()

    social_news["created_at"] = pd.to_datetime(social_news["created_at"], errors="coerce", utc=True)
    invalid_created_at = int(social_news["created_at"].isna().sum())
    social_news = social_news.loc[social_news["created_at"].notna()].copy()

    text_raw = social_news["text_raw"].fillna("").astype("string").str.strip()
    empty_text_raw = int(text_raw.eq("").sum())
    social_news = social_news.loc[text_raw.ne("")].copy()

    social_news["_dedupe_text"] = social_news["text_raw"].map(normalize_text_for_dedupe)
    before_dedupe = len(social_news)
    social_news = (
        social_news.sort_values("created_at", ascending=False)
        .drop_duplicates(subset=["_dedupe_text"], keep="first")
        .drop(columns=["_dedupe_text"])
    )
    duplicates_removed = before_dedupe - len(social_news)

    social_news["analysis_role"] = "p2_primary_source"
    social_news = social_news.sort_values("created_at", ascending=True).reset_index(drop=True)
    social_news["created_at"] = social_news["created_at"].dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    stats = {
        "raw_rows": raw_rows,
        "social_news_kept": len(social_news),
        "cve_excluded": cve_excluded,
        "invalid_created_at_removed": invalid_created_at,
        "empty_text_raw_removed": empty_text_raw,
        "duplicates_removed": duplicates_removed,
    }
    return social_news, stats


def build_report(df: pd.DataFrame, stats: dict[str, int], encoding_used: str) -> str:
    created_at = pd.to_datetime(df["created_at"], errors="coerce", utc=True)
    return "\n\n".join(
        [
            "# Live Social/News Dataset Report",
            "## Summary",
            markdown_table(
                ["Metric", "Value"],
                [
                    ["Raw initial rows", stats["raw_rows"]],
                    ["Social/news rows kept", stats["social_news_kept"]],
                    ["CVE rows excluded", stats["cve_excluded"]],
                    ["Rows removed: unparseable created_at", stats["invalid_created_at_removed"]],
                    ["Rows removed: empty text_raw", stats["empty_text_raw_removed"]],
                    ["Duplicate normalized texts removed", stats["duplicates_removed"]],
                    ["Min created_at", created_at.min().isoformat() if len(df) else ""],
                    ["Max created_at", created_at.max().isoformat() if len(df) else ""],
                    ["Encoding used", encoding_used],
                ],
            ),
            "## Source Type Distribution",
            markdown_table(["source_type", "rows", "percent_dataset"], distribution_rows(df, "source_type")),
            "## Source Name Distribution",
            markdown_table(["source_name", "rows", "percent_dataset"], distribution_rows(df, "source_name")),
            "## Methodological Note",
            METHODOLOGICAL_NOTE,
        ]
    ) + "\n"


def write_outputs(df: pd.DataFrame, report: str, output_path: Path, report_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8")
    report_path.write_text(report, encoding="utf-8")


def print_summary(stats: dict[str, int], output_path: Path, report_path: Path) -> None:
    print("Live social/news P2 dataset")
    print("===========================")
    print(f"Raw initial rows: {stats['raw_rows']}")
    print(f"Social/news rows kept: {stats['social_news_kept']}")
    print(f"CVE rows excluded: {stats['cve_excluded']}")
    print(f"Duplicate normalized texts removed: {stats['duplicates_removed']}")
    print(f"Output CSV: {output_path}")
    print(f"Report: {report_path}")


def main() -> int:
    args = parse_args()
    input_path = resolve_project_path(args.input)
    output_path = resolve_project_path(args.output)
    report_path = resolve_project_path(args.report)

    try:
        validate_file(input_path, "Input CSV")
        df, encoding_used = read_csv_with_encoding_fallback(input_path)
        social_news, stats = prepare_social_news_dataset(df)
        report = build_report(social_news, stats, encoding_used)
        write_outputs(social_news, report, output_path, report_path)
        print_summary(stats, output_path, report_path)
    except Exception as exc:
        print(f"Live social/news dataset error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
