"""
Aggregate live topic and sentiment signals over 12-hour time windows.

This step prepares topic-level live signals for the later P2 calculation. It
does not compute P2 and does not modify the input sentiment dataset.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "05_live_sentiment_dataset.csv"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "06_live_temporal_aggregation_12h.csv"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "live" / "live_temporal_aggregation_report.md"

REQUIRED_COLUMNS = [
    "id",
    "created_at",
    "source",
    "source_name",
    "source_type",
    "analysis_role",
    "dominant_topic",
    "dominant_topic_probability",
    "topic_label",
    "topic_confidence",
    "vader_compound",
    "sentiment_class",
]

ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")
METHODOLOGICAL_NOTE = (
    "L’aggregazione temporale trasforma i singoli documenti live in segnali "
    "topic-level su finestre da 12 ore, combinando volume e sentiment."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Aggregate live topic and sentiment data over 12-hour windows."
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
            df = pd.read_csv(
                input_path,
                dtype={
                    "id": "string",
                    "created_at": "string",
                    "source": "string",
                    "source_name": "string",
                    "source_type": "string",
                    "analysis_role": "string",
                    "topic_label": "string",
                    "topic_confidence": "string",
                    "sentiment_class": "string",
                },
                encoding=encoding,
                low_memory=False,
            )
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


def count_equals(series: pd.Series, value: str) -> int:
    return int(series.fillna("").astype("string").eq(value).sum())


def prepare_aggregation_dataset(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    validate_columns(df)

    working = df.copy()
    working["created_at"] = pd.to_datetime(working["created_at"], errors="coerce", utc=True)
    working["dominant_topic"] = pd.to_numeric(working["dominant_topic"], errors="coerce")
    working["dominant_topic_probability"] = pd.to_numeric(
        working["dominant_topic_probability"], errors="coerce"
    )
    working["vader_compound"] = pd.to_numeric(working["vader_compound"], errors="coerce")

    invalid_rows = (
        working["created_at"].isna()
        | working["dominant_topic"].isna()
        | working["dominant_topic"].eq(-1)
        | working["vader_compound"].isna()
    )
    discarded_rows = int(invalid_rows.sum())
    working = working.loc[~invalid_rows].copy()

    if working.empty:
        raise ValueError("No valid rows left for temporal aggregation.")

    working["dominant_topic"] = working["dominant_topic"].astype(int)
    working["time_window"] = working["created_at"].dt.floor("12h")
    return working, discarded_rows


def aggregate_temporally(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    working, discarded_rows = prepare_aggregation_dataset(df)

    grouped = working.groupby(["time_window", "dominant_topic", "topic_label", "topic_confidence"], as_index=False)
    aggregated = grouped.agg(
        topic_volume=("id", "size"),
        topic_sentiment_sum=("vader_compound", "sum"),
        topic_sentiment_mean=("vader_compound", "mean"),
        avg_topic_probability=("dominant_topic_probability", "mean"),
        negative_count=("sentiment_class", lambda values: count_equals(values, "negative")),
        neutral_count=("sentiment_class", lambda values: count_equals(values, "neutral")),
        positive_count=("sentiment_class", lambda values: count_equals(values, "positive")),
        sentiment_primary_count=("analysis_role", lambda values: count_equals(values, "sentiment_primary")),
        technical_context_count=("analysis_role", lambda values: count_equals(values, "technical_context")),
        reddit_count=("source_type", lambda values: count_equals(values, "reddit_rss")),
        news_count=("source_type", lambda values: count_equals(values, "news_rss")),
        cve_count=("source_type", lambda values: count_equals(values, "cve")),
    )

    window_volume = (
        working.groupby("time_window")
        .size()
        .rename("total_window_volume")
        .reset_index()
    )
    aggregated = aggregated.merge(window_volume, on="time_window", how="left")
    aggregated["topic_volume_share"] = (
        aggregated["topic_volume"] / aggregated["total_window_volume"]
    )

    aggregated = aggregated.sort_values(["time_window", "dominant_topic"]).reset_index(drop=True)
    return aggregated, discarded_rows


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


def format_value(value: object) -> object:
    if isinstance(value, float):
        return f"{value:.4f}"
    if isinstance(value, pd.Timestamp):
        return value.isoformat()
    if pd.isna(value):
        return ""
    return value


def dataframe_rows(df: pd.DataFrame, columns: list[str]) -> list[list[object]]:
    rows = []
    for row in df[columns].itertuples(index=False):
        rows.append([format_value(value) for value in row])
    return rows


def topic_distribution_rows(aggregated: pd.DataFrame) -> list[list[object]]:
    distribution = (
        aggregated.groupby(["dominant_topic", "topic_label", "topic_confidence"], as_index=False)
        .agg(topic_volume=("topic_volume", "sum"))
        .sort_values("topic_volume", ascending=False)
    )
    total = int(distribution["topic_volume"].sum())
    return [
        [
            int(row.dominant_topic),
            row.topic_label,
            row.topic_confidence,
            int(row.topic_volume),
            f"{percentage(row.topic_volume, total):.2f}%",
        ]
        for row in distribution.itertuples(index=False)
    ]


def build_report(
    aggregated: pd.DataFrame,
    input_rows: int,
    discarded_rows: int,
    encoding_used: str,
) -> str:
    used_rows = input_rows - discarded_rows
    display_columns = [
        "time_window",
        "dominant_topic",
        "topic_label",
        "topic_confidence",
        "topic_volume",
        "topic_sentiment_sum",
        "topic_sentiment_mean",
        "avg_topic_probability",
        "total_window_volume",
        "topic_volume_share",
    ]

    return "\n\n".join(
        [
            "# Live Temporal Aggregation Report",
            "## Summary",
            markdown_table(
                ["Metric", "Value"],
                [
                    ["Input rows", input_rows],
                    ["Rows used", used_rows],
                    ["Rows discarded", discarded_rows],
                    ["Number of time windows", aggregated["time_window"].nunique()],
                    ["Min time_window", aggregated["time_window"].min().isoformat()],
                    ["Max time_window", aggregated["time_window"].max().isoformat()],
                    ["Number of topics present", aggregated["dominant_topic"].nunique()],
                    ["Encoding used", encoding_used],
                ],
            ),
            "## First 10 Aggregated Rows",
            markdown_table(display_columns, dataframe_rows(aggregated.head(10), display_columns)),
            "## Top 10 Time Window / Topic by Volume",
            markdown_table(
                display_columns,
                dataframe_rows(
                    aggregated.sort_values("topic_volume", ascending=False).head(10),
                    display_columns,
                ),
            ),
            "## Top 10 Time Window / Topic by Strongest Negative Sentiment Sum",
            markdown_table(
                display_columns,
                dataframe_rows(
                    aggregated.sort_values("topic_sentiment_sum", ascending=True).head(10),
                    display_columns,
                ),
            ),
            "## Total Distribution by Topic Label",
            markdown_table(
                ["dominant_topic", "topic_label", "topic_confidence", "topic_volume", "percent_used_rows"],
                topic_distribution_rows(aggregated),
            ),
            "## Methodological Note",
            METHODOLOGICAL_NOTE,
        ]
    ) + "\n"


def write_outputs(df: pd.DataFrame, report: str, output_path: Path, report_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8")
    report_path.write_text(report, encoding="utf-8")


def print_summary(
    aggregated: pd.DataFrame,
    input_rows: int,
    discarded_rows: int,
    output_path: Path,
    report_path: Path,
) -> None:
    print("Live temporal aggregation 12h")
    print("=============================")
    print(f"Input rows: {input_rows}")
    print(f"Rows used: {input_rows - discarded_rows}")
    print(f"Rows discarded: {discarded_rows}")
    print(f"Aggregated rows: {len(aggregated)}")
    print(f"Time windows: {aggregated['time_window'].nunique()}")
    print(f"Time range: {aggregated['time_window'].min()} to {aggregated['time_window'].max()}")
    print(f"Topics present: {aggregated['dominant_topic'].nunique()}")
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
        aggregated, discarded_rows = aggregate_temporally(df)
        report = build_report(
            aggregated,
            input_rows=len(df),
            discarded_rows=discarded_rows,
            encoding_used=encoding_used,
        )
        write_outputs(aggregated, report, output_path, report_path)
        print_summary(aggregated, len(df), discarded_rows, output_path, report_path)
    except Exception as exc:
        print(f"Live temporal aggregation error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
