"""
Compute the live P2 index from 12-hour topic/sentiment aggregation.

P2 combines relative topic volume and aggregated sentiment to identify live
topic windows with strong semantic momentum. This script does not rerun LDA,
does not rerun VADER, and does not modify previous live datasets.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "06_live_temporal_aggregation_12h.csv"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "07_live_p2_index_12h.csv"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "live" / "live_p2_index_report.md"

REQUIRED_COLUMNS = [
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

ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")
METHODOLOGICAL_NOTE = (
    "P2 live combina volume e sentiment aggregati per identificare finestre "
    "temporali in cui un topic cyber mostra forte momentum semantico. Non "
    "rappresenta la conferma di un incidente reale."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compute live P2 index from 12-hour aggregation.")
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
                dtype={"time_window": "string", "topic_label": "string", "topic_confidence": "string"},
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


def classify_p2_direction(p2_index: float) -> str:
    if p2_index < 0:
        return "negative"
    if p2_index > 0:
        return "positive"
    return "neutral"


def classify_severity(p2_abs: float) -> str:
    if p2_abs >= 30:
        return "critical"
    if p2_abs >= 15:
        return "high"
    if p2_abs >= 8:
        return "elevated"
    if p2_abs >= 3:
        return "watch"
    return "low"


def classify_cybercon_level(p2_abs: float) -> int:
    if p2_abs >= 30:
        return 1
    if p2_abs >= 15:
        return 2
    if p2_abs >= 8:
        return 3
    if p2_abs >= 3:
        return 4
    return 5


def compute_p2_index(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df)

    p2_df = df.copy()
    p2_df["time_window"] = pd.to_datetime(p2_df["time_window"], errors="coerce", utc=True)

    numeric_columns = [
        "dominant_topic",
        "topic_volume",
        "topic_sentiment_sum",
        "topic_sentiment_mean",
        "avg_topic_probability",
        "total_window_volume",
        "topic_volume_share",
    ]
    for column in numeric_columns:
        p2_df[column] = pd.to_numeric(p2_df[column], errors="coerce")

    invalid_rows = (
        p2_df["time_window"].isna()
        | p2_df["dominant_topic"].isna()
        | p2_df["topic_volume"].isna()
        | p2_df["topic_sentiment_sum"].isna()
        | p2_df["topic_sentiment_mean"].isna()
    )
    if invalid_rows.any():
        print(f"Warning: dropping {int(invalid_rows.sum())} row(s) with invalid P2 inputs.")
    p2_df = p2_df.loc[~invalid_rows].copy()

    if p2_df.empty:
        raise ValueError("No valid rows left after parsing P2 inputs.")

    p2_df["dominant_topic"] = p2_df["dominant_topic"].astype(int)

    topic_baselines = (
        p2_df.assign(abs_topic_sentiment_sum=p2_df["topic_sentiment_sum"].abs())
        .groupby("dominant_topic", as_index=False)
        .agg(
            avg_topic_volume=("topic_volume", "mean"),
            avg_abs_topic_sentiment_sum=("abs_topic_sentiment_sum", "mean"),
        )
    )
    p2_df = p2_df.merge(topic_baselines, on="dominant_topic", how="left")

    volume_denominator = p2_df["avg_topic_volume"].replace(0, np.nan)
    sentiment_denominator = p2_df["avg_abs_topic_sentiment_sum"].replace(0, np.nan)

    p2_df["volume_factor"] = (p2_df["topic_volume"] / volume_denominator).replace(
        [np.inf, -np.inf], np.nan
    )
    p2_df["sentiment_factor"] = (
        p2_df["topic_sentiment_sum"] / sentiment_denominator
    ).replace([np.inf, -np.inf], np.nan)
    p2_df["p2_index"] = p2_df["volume_factor"] * p2_df["sentiment_factor"]

    p2_df[["volume_factor", "sentiment_factor", "p2_index"]] = p2_df[
        ["volume_factor", "sentiment_factor", "p2_index"]
    ].fillna(0)
    p2_df["p2_abs"] = p2_df["p2_index"].abs()
    p2_df["p2_direction"] = p2_df["p2_index"].map(classify_p2_direction)
    p2_df["severity"] = p2_df["p2_abs"].map(classify_severity)
    p2_df["cybercon_level"] = p2_df["p2_abs"].map(classify_cybercon_level).astype(int)

    return p2_df.sort_values(["time_window", "dominant_topic"]).reset_index(drop=True)


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


def distribution_rows(df: pd.DataFrame, column: str) -> list[list[object]]:
    counts = (
        df[column]
        .fillna("UNKNOWN")
        .astype("string")
        .value_counts()
        .rename_axis(column)
        .reset_index(name="rows")
    )
    total = int(counts["rows"].sum())
    return [
        [getattr(row, column), int(row.rows), f"{percentage(row.rows, total):.2f}%"]
        for row in counts.itertuples(index=False)
    ]


def single_hot_topic_row(row: pd.Series | None) -> list[list[object]]:
    if row is None:
        return []
    columns = [
        "time_window",
        "dominant_topic",
        "topic_label",
        "topic_confidence",
        "topic_volume",
        "topic_sentiment_sum",
        "p2_index",
        "p2_abs",
        "severity",
        "cybercon_level",
    ]
    return [[format_value(row[column]) for column in columns]]


def build_report(p2_df: pd.DataFrame, input_rows: int, encoding_used: str) -> str:
    display_columns = [
        "time_window",
        "dominant_topic",
        "topic_label",
        "topic_confidence",
        "topic_volume",
        "topic_sentiment_sum",
        "volume_factor",
        "sentiment_factor",
        "p2_index",
        "p2_abs",
        "severity",
        "cybercon_level",
    ]

    negative_rows = p2_df.loc[p2_df["p2_index"] < 0]
    positive_rows = p2_df.loc[p2_df["p2_index"] > 0]
    strongest_negative = (
        negative_rows.sort_values("p2_index", ascending=True).iloc[0]
        if not negative_rows.empty
        else None
    )
    strongest_positive = (
        positive_rows.sort_values("p2_index", ascending=False).iloc[0]
        if not positive_rows.empty
        else None
    )

    return "\n\n".join(
        [
            "# Live P2 Index Report",
            "## Summary",
            markdown_table(
                ["Metric", "Value"],
                [
                    ["Input rows", input_rows],
                    ["Output rows", len(p2_df)],
                    ["Number of topics", p2_df["dominant_topic"].nunique()],
                    ["Number of time windows", p2_df["time_window"].nunique()],
                    ["Min time_window", p2_df["time_window"].min().isoformat()],
                    ["Max time_window", p2_df["time_window"].max().isoformat()],
                    ["Encoding used", encoding_used],
                ],
            ),
            "## Strongest Negative Hot Topic",
            markdown_table(
                [
                    "time_window",
                    "dominant_topic",
                    "topic_label",
                    "topic_confidence",
                    "topic_volume",
                    "topic_sentiment_sum",
                    "p2_index",
                    "p2_abs",
                    "severity",
                    "cybercon_level",
                ],
                single_hot_topic_row(strongest_negative),
            ),
            "## Strongest Positive Hot Topic",
            markdown_table(
                [
                    "time_window",
                    "dominant_topic",
                    "topic_label",
                    "topic_confidence",
                    "topic_volume",
                    "topic_sentiment_sum",
                    "p2_index",
                    "p2_abs",
                    "severity",
                    "cybercon_level",
                ],
                single_hot_topic_row(strongest_positive),
            ),
            "## Top 10 Negative Hot Topics by P2 Index",
            markdown_table(
                display_columns,
                dataframe_rows(p2_df.sort_values("p2_index", ascending=True).head(10), display_columns),
            ),
            "## Top 10 Positive Hot Topics by P2 Index",
            markdown_table(
                display_columns,
                dataframe_rows(p2_df.sort_values("p2_index", ascending=False).head(10), display_columns),
            ),
            "## Top 10 Absolute Hot Topics by P2 Abs",
            markdown_table(
                display_columns,
                dataframe_rows(p2_df.sort_values("p2_abs", ascending=False).head(10), display_columns),
            ),
            "## Severity Distribution",
            markdown_table(["severity", "rows", "percent_dataset"], distribution_rows(p2_df, "severity")),
            "## P2 Direction Distribution",
            markdown_table(
                ["p2_direction", "rows", "percent_dataset"],
                distribution_rows(p2_df, "p2_direction"),
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


def print_summary(p2_df: pd.DataFrame, input_rows: int, output_path: Path, report_path: Path) -> None:
    negative_rows = p2_df.loc[p2_df["p2_index"] < 0]
    positive_rows = p2_df.loc[p2_df["p2_index"] > 0]
    strongest_negative = negative_rows.sort_values("p2_index", ascending=True).head(1)
    strongest_positive = positive_rows.sort_values("p2_index", ascending=False).head(1)

    print("Live P2 index 12h")
    print("=================")
    print(f"Input rows: {input_rows}")
    print(f"Output rows: {len(p2_df)}")
    print(f"Topics: {p2_df['dominant_topic'].nunique()}")
    print(f"Time windows: {p2_df['time_window'].nunique()}")
    print(f"Time range: {p2_df['time_window'].min()} to {p2_df['time_window'].max()}")
    if not strongest_negative.empty:
        row = strongest_negative.iloc[0]
        print(
            "Strongest negative: "
            f"{row['time_window']} | T{int(row['dominant_topic'])} | "
            f"p2={row['p2_index']:.4f} | {row['severity']}"
        )
    if not strongest_positive.empty:
        row = strongest_positive.iloc[0]
        print(
            "Strongest positive: "
            f"{row['time_window']} | T{int(row['dominant_topic'])} | "
            f"p2={row['p2_index']:.4f} | {row['severity']}"
        )
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
        p2_df = compute_p2_index(df)
        report = build_report(p2_df, input_rows=len(df), encoding_used=encoding_used)
        write_outputs(p2_df, report, output_path, report_path)
        print_summary(p2_df, len(df), output_path, report_path)
    except Exception as exc:
        print(f"Live P2 index error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
