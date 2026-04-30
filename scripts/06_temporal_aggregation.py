"""
Aggregate cybersecurity topic volume and VADER sentiment over 12-hour windows.

Only created_at, dominant_topic, dominant_topic_probability, and vader_compound
are used for the aggregation. Manual metadata such as original_type,
annotation, and relevant is not used in this calculation.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
DEFAULT_INPUT_PATH = PROCESSED_DIR / "05_sentiment_dataset.csv"
DEFAULT_OUTPUT_PATH = PROCESSED_DIR / "06_temporal_aggregation_12h.csv"

REQUIRED_COLUMNS = {"created_at", "dominant_topic", "vader_compound"}
OPTIONAL_PROBABILITY_COLUMN = "dominant_topic_probability"
ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")


@dataclass(frozen=True)
class AggregationReport:
    input_rows: int
    output_rows: int
    time_windows: int
    min_time_window: pd.Timestamp
    max_time_window: pd.Timestamp
    topic_count: int
    encoding_used: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Aggregate topic volume and sentiment over 12-hour windows."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="Path to the sentiment dataset.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Path where the temporal aggregation CSV will be saved.",
    )
    return parser.parse_args()


def resolve_project_path(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


def validate_input_path(input_path: Path) -> None:
    if not input_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {input_path}")
    if not input_path.is_file():
        raise FileNotFoundError(f"Input path is not a file: {input_path}")
    if input_path.suffix.lower() != ".csv":
        raise ValueError(f"Input file must be a CSV: {input_path}")


def read_csv_with_encoding_fallback(input_path: Path) -> tuple[pd.DataFrame, str]:
    last_error: UnicodeDecodeError | None = None

    for encoding in ENCODINGS_TO_TRY:
        try:
            df = pd.read_csv(input_path, encoding=encoding, low_memory=False)
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

    missing_columns = sorted(REQUIRED_COLUMNS.difference(df.columns))
    if missing_columns:
        available = ", ".join(df.columns)
        missing = ", ".join(missing_columns)
        raise ValueError(
            f"Missing required column(s): {missing}\nAvailable columns: {available}"
        )


def aggregate_temporally(df: pd.DataFrame, encoding_used: str) -> tuple[pd.DataFrame, AggregationReport]:
    validate_columns(df)

    working = df.copy()
    working["created_at"] = pd.to_datetime(working["created_at"], errors="coerce", utc=True)
    working["dominant_topic"] = pd.to_numeric(working["dominant_topic"], errors="coerce")
    working["vader_compound"] = pd.to_numeric(working["vader_compound"], errors="coerce")

    invalid_rows = (
        working["created_at"].isna()
        | working["dominant_topic"].isna()
        | working["vader_compound"].isna()
    )
    if invalid_rows.any():
        print(
            "Warning: dropping "
            f"{int(invalid_rows.sum())} row(s) with invalid timestamp, topic, or sentiment."
        )
    working = working.loc[~invalid_rows].copy()

    if working.empty:
        raise ValueError("No valid rows left after parsing created_at, dominant_topic, and vader_compound.")

    working["dominant_topic"] = working["dominant_topic"].astype(int)
    working["time_window"] = working["created_at"].dt.floor("12h")

    aggregations = {
        "topic_volume": ("vader_compound", "size"),
        "topic_sentiment_sum": ("vader_compound", "sum"),
        "topic_sentiment_mean": ("vader_compound", "mean"),
    }
    if OPTIONAL_PROBABILITY_COLUMN in working.columns:
        working[OPTIONAL_PROBABILITY_COLUMN] = pd.to_numeric(
            working[OPTIONAL_PROBABILITY_COLUMN], errors="coerce"
        )
        aggregations["avg_topic_probability"] = (OPTIONAL_PROBABILITY_COLUMN, "mean")

    aggregated = (
        working.groupby(["time_window", "dominant_topic"], as_index=False)
        .agg(**aggregations)
        .sort_values(["time_window", "dominant_topic"])
        .reset_index(drop=True)
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

    report = AggregationReport(
        input_rows=len(df),
        output_rows=len(aggregated),
        time_windows=aggregated["time_window"].nunique(),
        min_time_window=aggregated["time_window"].min(),
        max_time_window=aggregated["time_window"].max(),
        topic_count=aggregated["dominant_topic"].nunique(),
        encoding_used=encoding_used,
    )

    return aggregated, report


def print_table(df: pd.DataFrame, title: str) -> None:
    print(f"\n{title}")
    print("-" * len(title))
    print(df.to_string(index=False))


def print_final_report(report: AggregationReport, aggregated: pd.DataFrame, output_path: Path) -> None:
    print("\nTemporal aggregation report")
    print("---------------------------")
    print(f"Encoding used: {report.encoding_used}")
    print(f"Input rows: {report.input_rows}")
    print(f"Aggregated rows: {report.output_rows}")
    print(f"Number of time windows: {report.time_windows}")
    print(f"Time range: {report.min_time_window} to {report.max_time_window}")
    print(f"Number of topics present: {report.topic_count}")
    print(f"Output file: {output_path}")

    print_table(aggregated.head(10), "First 10 aggregated rows")
    print_table(
        aggregated.sort_values("topic_volume", ascending=False).head(10),
        "Top 10 time_window/topic by topic_volume",
    )
    print_table(
        aggregated.sort_values("topic_sentiment_sum", ascending=True).head(10),
        "Top 10 time_window/topic by strongest negative sentiment sum",
    )


def main() -> int:
    args = parse_args()

    try:
        input_path = resolve_project_path(args.input)
        output_path = resolve_project_path(args.output)

        validate_input_path(input_path)

        print(f"Loading CSV: {input_path}")
        df, encoding_used = read_csv_with_encoding_fallback(input_path)
        print(f"Available columns: {', '.join(df.columns)}")
        print(f"Input rows: {len(df)}")

        aggregated, report = aggregate_temporally(df, encoding_used)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        aggregated.to_csv(output_path, index=False)
        print_final_report(report, aggregated, output_path)

    except FileNotFoundError as exc:
        print(f"File error: {exc}", file=sys.stderr)
        return 1
    except UnicodeDecodeError as exc:
        print(f"Encoding error: {exc}", file=sys.stderr)
        return 1
    except pd.errors.EmptyDataError:
        print("Data validation error: Input CSV is empty.", file=sys.stderr)
        return 1
    except pd.errors.ParserError as exc:
        print(f"CSV parsing error: {exc}", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"Data validation error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
