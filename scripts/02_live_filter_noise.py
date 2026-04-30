"""
Filter obvious noise from the live social/news P2 dataset.

This script keeps the raw live dataset intact. It does not run NLP
preprocessing, LDA/topic modeling, VADER, P2, or dashboard export.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import re
import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "01_live_social_news_dataset.csv"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "02_live_filtered_dataset.csv"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "live" / "live_filter_noise_report.md"

MIN_TEXT_LENGTH = 30
MAX_URL_RATIO = 0.20

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
    "analysis_role",
]

URL_PATTERN = re.compile(
    r"""
    \b
    (?:
        https?://
        |
        www\.
    )
    [^\s<>"')\]}]+
    """,
    flags=re.IGNORECASE | re.VERBOSE,
)


@dataclass(frozen=True)
class FilterSummary:
    initial_rows: int
    short_text_rows: int
    high_url_ratio_rows: int
    final_rows: int

    @property
    def kept_percent(self) -> float:
        if self.initial_rows == 0:
            return 0.0
        return (self.final_rows / self.initial_rows) * 100.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Filter short and URL-heavy records from the live social/news P2 dataset."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="Path to data/live/processed/01_live_social_news_dataset.csv.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Path to data/live/processed/02_live_filtered_dataset.csv.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=DEFAULT_REPORT_PATH,
        help="Path to reports/live/live_filter_noise_report.md.",
    )
    return parser.parse_args()


def resolve_project_path(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


def load_dataset(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Input CSV not found: {path}")
    if path.suffix.lower() != ".csv":
        raise ValueError(f"Input file must be a CSV: {path}")
    return pd.read_csv(path, dtype="string")


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


def clean_string(series: pd.Series) -> pd.Series:
    return series.fillna("").astype("string")


def find_urls(text: object) -> list[str]:
    value = "" if pd.isna(text) else str(text)
    return [match.group(0).rstrip(".,;:!?") for match in URL_PATTERN.finditer(value)]


def add_noise_metrics(df: pd.DataFrame) -> pd.DataFrame:
    enriched = df.copy()
    text = clean_string(enriched["text_raw"])
    enriched["text_length"] = text.str.len()
    url_matches = text.map(find_urls)
    enriched["url_count"] = url_matches.map(len)
    enriched["url_chars"] = url_matches.map(lambda urls: sum(len(url) for url in urls))
    enriched["url_ratio"] = enriched["url_chars"] / enriched["text_length"].replace(0, pd.NA)
    enriched["url_ratio"] = enriched["url_ratio"].fillna(0.0)
    return enriched


def source_distribution(df: pd.DataFrame, column: str) -> pd.DataFrame:
    total = len(df)
    counts = (
        df[column]
        .fillna("UNKNOWN")
        .astype("string")
        .replace("", "UNKNOWN")
        .value_counts()
        .rename_axis(column)
        .reset_index(name="rows")
    )
    counts["percent_dataset"] = counts["rows"].apply(lambda rows: percentage(rows, total))
    return counts


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


def distribution_rows(distribution: pd.DataFrame, label_column: str) -> list[list[object]]:
    return [
        [getattr(row, label_column), int(row.rows), f"{float(row.percent_dataset):.2f}%"]
        for row in distribution.itertuples(index=False)
    ]


def filter_noise(df: pd.DataFrame) -> tuple[pd.DataFrame, FilterSummary, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    validate_columns(df)
    before_source_type = source_distribution(df, "source_type")
    before_analysis_role = source_distribution(df, "analysis_role")

    enriched = add_noise_metrics(df)
    short_text_mask = enriched["text_length"] < MIN_TEXT_LENGTH
    high_url_ratio_mask = enriched["url_ratio"] > MAX_URL_RATIO
    keep_mask = ~short_text_mask & ~high_url_ratio_mask

    filtered = enriched.loc[keep_mask].copy().reset_index(drop=True)
    after_source_type = source_distribution(filtered, "source_type")
    after_analysis_role = source_distribution(filtered, "analysis_role")

    summary = FilterSummary(
        initial_rows=len(df),
        short_text_rows=int(short_text_mask.sum()),
        high_url_ratio_rows=int(high_url_ratio_mask.sum()),
        final_rows=len(filtered),
    )
    return filtered, summary, before_source_type, after_source_type, before_analysis_role, after_analysis_role


def build_report(
    summary: FilterSummary,
    before_source_type: pd.DataFrame,
    after_source_type: pd.DataFrame,
    before_analysis_role: pd.DataFrame,
    after_analysis_role: pd.DataFrame,
) -> str:
    return "\n\n".join(
        [
            "# Live Noise Filter Report",
            "Diagnostic filtering report for `data/live/processed/01_live_social_news_dataset.csv`. This step keeps `text_raw` intact and does not run NLP preprocessing, LDA/topic modeling, VADER, P2, or dashboard export.",
            "## Summary",
            markdown_table(
                ["Metric", "Value"],
                [
                    ["Initial rows", summary.initial_rows],
                    [f"Rows removed: text_length < {MIN_TEXT_LENGTH}", summary.short_text_rows],
                    [f"Rows removed: url_ratio > {MAX_URL_RATIO:.2f}", summary.high_url_ratio_rows],
                    ["Final rows", summary.final_rows],
                    ["Percent kept", f"{summary.kept_percent:.2f}%"],
                ],
            ),
            "## Source Type Distribution Before",
            markdown_table(["source_type", "rows", "percent_dataset"], distribution_rows(before_source_type, "source_type")),
            "## Source Type Distribution After",
            markdown_table(["source_type", "rows", "percent_dataset"], distribution_rows(after_source_type, "source_type")),
            "## Analysis Role Distribution Before",
            markdown_table(["analysis_role", "rows", "percent_dataset"], distribution_rows(before_analysis_role, "analysis_role")),
            "## Analysis Role Distribution After",
            markdown_table(["analysis_role", "rows", "percent_dataset"], distribution_rows(after_analysis_role, "analysis_role")),
        ]
    ) + "\n"


def write_outputs(filtered: pd.DataFrame, report: str, output_path: Path, report_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    filtered.to_csv(output_path, index=False, encoding="utf-8")
    report_path.write_text(report, encoding="utf-8")


def print_summary(summary: FilterSummary, output_path: Path, report_path: Path) -> None:
    print("Live noise filter")
    print("=================")
    print(f"Initial rows: {summary.initial_rows}")
    print(f"Rows removed - text_length < {MIN_TEXT_LENGTH}: {summary.short_text_rows}")
    print(f"Rows removed - url_ratio > {MAX_URL_RATIO:.2f}: {summary.high_url_ratio_rows}")
    print(f"Final rows: {summary.final_rows}")
    print(f"Percent kept: {summary.kept_percent:.2f}%")
    print(f"Output CSV: {output_path}")
    print(f"Report: {report_path}")


def main() -> int:
    args = parse_args()
    input_path = resolve_project_path(args.input)
    output_path = resolve_project_path(args.output)
    report_path = resolve_project_path(args.report)

    try:
        df = load_dataset(input_path)
        filtered, summary, before_source_type, after_source_type, before_analysis_role, after_analysis_role = filter_noise(df)
        report = build_report(
            summary,
            before_source_type,
            after_source_type,
            before_analysis_role,
            after_analysis_role,
        )
        write_outputs(filtered, report, output_path, report_path)
        print_summary(summary, output_path, report_path)
    except Exception as exc:
        print(f"Noise filter error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
