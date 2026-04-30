"""
Prepare a sentiment-oriented live dataset from raw online collection.

This script selects and balances raw live records for later sentiment analysis.
It does not run NLP preprocessing, LDA/topic modeling, VADER, P2, dashboard
export, or any mutation of data/live/raw/live_items_raw.csv.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import re
import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "raw" / "live_items_raw.csv"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "01_live_sentiment_dataset.csv"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "live" / "live_sentiment_dataset_report.md"

MAX_CVE_ITEMS = 200
MAX_CVE_SHARE = 0.33

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

FINAL_COLUMNS = [
    *REQUIRED_COLUMNS,
    "analysis_included",
    "analysis_role",
]

METHODOLOGY_NOTE = (
    "Il raw dataset conserva tutti i record raccolti. Il sentiment dataset "
    "privilegia social/news perché il progetto è centrato sul sentiment e sul "
    "semantic momentum. I CVE/NVD sono mantenuti come contesto tecnico, ma "
    "limitati per evitare che testi standardizzati dominino l’analisi."
)


@dataclass(frozen=True)
class PreparationSummary:
    raw_rows: int
    valid_rows: int
    invalid_created_at_rows: int
    empty_text_rows: int
    duplicate_text_rows_removed: int
    social_news_kept: int
    cve_kept: int
    cve_excluded: int
    final_rows: int
    final_cve_percent: float
    final_created_min: str
    final_created_max: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare a sentiment-oriented live dataset from raw live collection."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="Path to data/live/raw/live_items_raw.csv.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Path to the prepared sentiment dataset CSV.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=DEFAULT_REPORT_PATH,
        help="Path to the Markdown preparation report.",
    )
    return parser.parse_args()


def resolve_project_path(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


def load_raw_dataset(path: Path) -> pd.DataFrame:
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


def clean_string(series: pd.Series) -> pd.Series:
    return series.fillna("").astype("string").str.strip()


def normalize_text_for_dedup(text: object) -> str:
    value = "" if pd.isna(text) else str(text)
    value = value.lower()
    value = re.sub(r"https?://\S+|www\.\S+", " ", value)
    value = re.sub(r"[^\w\s]", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def parse_datetime_column(df: pd.DataFrame, column: str) -> pd.Series:
    return pd.to_datetime(df[column], errors="coerce", utc=True)


def iso_or_na(value: pd.Timestamp | None) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return value.to_pydatetime().replace(microsecond=0).isoformat().replace("+00:00", "Z")


def percentage(part: int | float, total: int | float) -> float:
    if not total:
        return 0.0
    return round((float(part) / float(total)) * 100.0, 2)


def source_type_distribution(df: pd.DataFrame) -> pd.DataFrame:
    total = len(df)
    if "source_type" not in df.columns:
        return pd.DataFrame(columns=["source_type", "rows", "percent_dataset"])
    counts = (
        clean_string(df["source_type"])
        .replace("", "UNKNOWN")
        .value_counts()
        .rename_axis("source_type")
        .reset_index(name="rows")
    )
    counts["percent_dataset"] = counts["rows"].apply(lambda rows: percentage(rows, total))
    return counts


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(value) for value in row) + " |")
    return "\n".join(lines)


def distribution_rows(distribution: pd.DataFrame) -> list[list[object]]:
    return [
        [row.source_type, int(row.rows), f"{float(row.percent_dataset):.2f}%"]
        for row in distribution.itertuples(index=False)
    ]


def prepare_sentiment_dataset(raw_df: pd.DataFrame) -> tuple[pd.DataFrame, PreparationSummary, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    validate_columns(raw_df)
    raw_df = raw_df[REQUIRED_COLUMNS].copy()
    raw_rows = len(raw_df)
    raw_distribution = source_type_distribution(raw_df)

    working = raw_df.copy()
    working["created_at"] = parse_datetime_column(working, "created_at")
    working["collected_at"] = parse_datetime_column(working, "collected_at")
    working["text_raw"] = clean_string(working["text_raw"])

    invalid_created_at = working["created_at"].isna()
    empty_text = working["text_raw"].eq("")
    valid = working.loc[~invalid_created_at & ~empty_text].copy()
    valid_rows = len(valid)

    valid["text_normalized_for_dedup"] = valid["text_raw"].apply(normalize_text_for_dedup)
    valid = valid.sort_values("created_at", ascending=False)
    before_dedup_rows = len(valid)
    deduped = valid.drop_duplicates(subset=["text_normalized_for_dedup"], keep="first").copy()
    duplicate_text_rows_removed = before_dedup_rows - len(deduped)
    before_balance_distribution = source_type_distribution(deduped)

    social_items = deduped.loc[deduped["source_type"].eq("reddit_rss")].copy()
    news_items = deduped.loc[deduped["source_type"].eq("news_rss")].copy()
    cve_items = deduped.loc[deduped["source_type"].eq("cve")].copy()

    non_cve_count = len(social_items) + len(news_items)
    max_cve_by_share = int((MAX_CVE_SHARE / (1 - MAX_CVE_SHARE)) * non_cve_count) if non_cve_count else 0
    cve_cap = min(MAX_CVE_ITEMS, max_cve_by_share)
    cve_kept = cve_items.sort_values("created_at", ascending=False).head(cve_cap).copy()
    cve_excluded = max(0, len(cve_items) - len(cve_kept))

    final_df = pd.concat([social_items, news_items, cve_kept], ignore_index=True)
    final_df["analysis_included"] = True
    final_df["analysis_role"] = final_df["source_type"].map(
        {
            "reddit_rss": "sentiment_primary",
            "news_rss": "sentiment_primary",
            "cve": "technical_context",
        }
    ).fillna("sentiment_primary")

    final_df = final_df.sort_values("created_at", ascending=True).reset_index(drop=True)
    final_df = final_df.drop(columns=["text_normalized_for_dedup"], errors="ignore")
    final_distribution = source_type_distribution(final_df)

    final_created = pd.to_datetime(final_df["created_at"], errors="coerce", utc=True)
    final_rows = len(final_df)
    final_cve_count = int(final_df["source_type"].eq("cve").sum()) if final_rows else 0
    summary = PreparationSummary(
        raw_rows=raw_rows,
        valid_rows=valid_rows,
        invalid_created_at_rows=int(invalid_created_at.sum()),
        empty_text_rows=int(empty_text.sum()),
        duplicate_text_rows_removed=duplicate_text_rows_removed,
        social_news_kept=non_cve_count,
        cve_kept=len(cve_kept),
        cve_excluded=cve_excluded,
        final_rows=final_rows,
        final_cve_percent=percentage(final_cve_count, final_rows),
        final_created_min=iso_or_na(final_created.min()),
        final_created_max=iso_or_na(final_created.max()),
    )

    return final_df[FINAL_COLUMNS], summary, raw_distribution, before_balance_distribution, final_distribution


def format_datetime_columns_for_csv(df: pd.DataFrame) -> pd.DataFrame:
    output = df.copy()
    for column in ("created_at", "collected_at"):
        parsed = pd.to_datetime(output[column], errors="coerce", utc=True)
        output[column] = parsed.dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    return output


def build_report(
    summary: PreparationSummary,
    raw_distribution: pd.DataFrame,
    before_balance_distribution: pd.DataFrame,
    final_distribution: pd.DataFrame,
) -> str:
    return "\n\n".join(
        [
            "# Live Sentiment Dataset Report",
            "Dataset derived from `data/live/raw/live_items_raw.csv` for later sentiment analysis. No NLP preprocessing, LDA/topic modeling, VADER, P2, or dashboard export is performed here.",
            "## Summary",
            markdown_table(
                ["Metric", "Value"],
                [
                    ["Raw initial rows", summary.raw_rows],
                    ["Rows after invalid removal", summary.valid_rows],
                    ["Rows with unparsable created_at removed", summary.invalid_created_at_rows],
                    ["Rows with null/empty text_raw removed", summary.empty_text_rows],
                    ["Normalized text duplicates removed", summary.duplicate_text_rows_removed],
                    ["Social/news items kept", summary.social_news_kept],
                    ["CVE items kept", summary.cve_kept],
                    ["CVE items excluded from analysis dataset only", summary.cve_excluded],
                    ["Final rows", summary.final_rows],
                    ["Final CVE percent", f"{summary.final_cve_percent:.2f}%"],
                    ["Final created_at range", f"{summary.final_created_min} -> {summary.final_created_max}"],
                    ["MAX_CVE_ITEMS", MAX_CVE_ITEMS],
                    ["MAX_CVE_SHARE", f"{MAX_CVE_SHARE:.2f}"],
                ],
            ),
            "## Source Type Distribution Before",
            markdown_table(["source_type", "rows", "percent_dataset"], distribution_rows(raw_distribution)),
            "## Source Type Distribution After Dedup Before CVE Cap",
            markdown_table(["source_type", "rows", "percent_dataset"], distribution_rows(before_balance_distribution)),
            "## Source Type Distribution After",
            markdown_table(["source_type", "rows", "percent_dataset"], distribution_rows(final_distribution)),
            "## Methodological Note",
            METHODOLOGY_NOTE,
        ]
    ) + "\n"


def write_outputs(final_df: pd.DataFrame, report: str, output_path: Path, report_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    format_datetime_columns_for_csv(final_df).to_csv(output_path, index=False, encoding="utf-8")
    report_path.write_text(report, encoding="utf-8")


def print_summary(summary: PreparationSummary, output_path: Path, report_path: Path) -> None:
    print("Live sentiment dataset preparation")
    print("==================================")
    print(f"Raw initial rows: {summary.raw_rows}")
    print(f"Rows after invalid removal: {summary.valid_rows}")
    print(f"Normalized text duplicates removed: {summary.duplicate_text_rows_removed}")
    print(f"Social/news items kept: {summary.social_news_kept}")
    print(f"CVE kept/excluded: {summary.cve_kept}/{summary.cve_excluded}")
    print(f"Final rows: {summary.final_rows}")
    print(f"Final CVE percent: {summary.final_cve_percent:.2f}%")
    print(f"Final created_at range: {summary.final_created_min} -> {summary.final_created_max}")
    print(f"Output CSV: {output_path}")
    print(f"Report: {report_path}")


def main() -> int:
    args = parse_args()
    input_path = resolve_project_path(args.input)
    output_path = resolve_project_path(args.output)
    report_path = resolve_project_path(args.report)

    try:
        raw_df = load_raw_dataset(input_path)
        final_df, summary, raw_distribution, before_balance_distribution, final_distribution = prepare_sentiment_dataset(raw_df)
        report = build_report(summary, raw_distribution, before_balance_distribution, final_distribution)
        write_outputs(final_df, report, output_path, report_path)
        print_summary(summary, output_path, report_path)
    except Exception as exc:
        print(f"Preparation error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
