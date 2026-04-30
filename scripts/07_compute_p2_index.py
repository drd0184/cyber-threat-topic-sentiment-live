"""
Compute a P2-style index from aggregated topic volume and sentiment.

The P2 index uses only aggregated volume and aggregated sentiment per
time-window/topic pair. Manual metadata such as original_type, annotation, and
relevant is not used.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
DEFAULT_INPUT_PATH = PROCESSED_DIR / "06_temporal_aggregation_12h.csv"
DEFAULT_OUTPUT_PATH = PROCESSED_DIR / "07_p2_index_12h.csv"

REQUIRED_COLUMNS = {
    "time_window",
    "dominant_topic",
    "topic_volume",
    "topic_sentiment_sum",
    "topic_sentiment_mean",
}
ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compute a P2-style topic index from 12-hour aggregation data."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="Path to the 12-hour temporal aggregation CSV.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Path where the P2 index CSV will be saved.",
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


def classify_p2_direction(p2_index: float) -> str:
    if p2_index < 0:
        return "negative"
    if p2_index > 0:
        return "positive"
    return "neutral"


def compute_p2_index(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df)

    p2_df = df.copy()
    p2_df["time_window"] = pd.to_datetime(p2_df["time_window"], errors="coerce", utc=True)
    p2_df["dominant_topic"] = pd.to_numeric(p2_df["dominant_topic"], errors="coerce")
    p2_df["topic_volume"] = pd.to_numeric(p2_df["topic_volume"], errors="coerce")
    p2_df["topic_sentiment_sum"] = pd.to_numeric(
        p2_df["topic_sentiment_sum"], errors="coerce"
    )
    p2_df["topic_sentiment_mean"] = pd.to_numeric(
        p2_df["topic_sentiment_mean"], errors="coerce"
    )

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

    p2_df["volume_factor"] = p2_df["topic_volume"] / volume_denominator
    p2_df["sentiment_factor"] = p2_df["topic_sentiment_sum"] / sentiment_denominator
    p2_df["p2_index"] = (p2_df["volume_factor"] * p2_df["sentiment_factor"]).fillna(0)
    p2_df["p2_abs"] = p2_df["p2_index"].abs()
    p2_df["p2_direction"] = p2_df["p2_index"].map(classify_p2_direction)

    return p2_df.sort_values(["time_window", "dominant_topic"]).reset_index(drop=True)


def print_table(df: pd.DataFrame, title: str) -> None:
    print(f"\n{title}")
    print("-" * len(title))
    print(df.to_string(index=False))


def print_final_report(input_rows: int, p2_df: pd.DataFrame, output_path: Path, encoding_used: str) -> None:
    print("\nP2 index report")
    print("---------------")
    print(f"Encoding used: {encoding_used}")
    print(f"Input rows: {input_rows}")
    print(f"Number of topics: {p2_df['dominant_topic'].nunique()}")
    print(f"Number of time windows: {p2_df['time_window'].nunique()}")
    print(f"Output file: {output_path}")

    display_columns = [
        "time_window",
        "dominant_topic",
        "topic_volume",
        "topic_sentiment_sum",
        "volume_factor",
        "sentiment_factor",
        "p2_index",
        "p2_abs",
        "p2_direction",
    ]
    print_table(
        p2_df.sort_values("p2_index", ascending=True).head(10)[display_columns],
        "Top 10 negative hot topics by p2_index",
    )
    print_table(
        p2_df.sort_values("p2_index", ascending=False).head(10)[display_columns],
        "Top 10 positive hot topics by p2_index",
    )
    print_table(
        p2_df.sort_values("p2_abs", ascending=False).head(10)[display_columns],
        "Top 10 absolute hot topics by p2_abs",
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

        p2_df = compute_p2_index(df)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        p2_df.to_csv(output_path, index=False)
        print_final_report(len(df), p2_df, output_path, encoding_used)

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
