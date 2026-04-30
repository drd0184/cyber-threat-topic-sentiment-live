"""
Normalize the static Twitter cybersecurity dataset.

The columns original_type, annotation, relevant, and urls are preserved only as
metadata for later qualitative checks. They should not be used as model
features in downstream topic modeling or sentiment analysis steps.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
DEFAULT_OUTPUT_PATH = PROCESSED_DIR / "01_static_dataset_normalized.csv"

REQUIRED_COLUMNS = {
    "id",
    "date",
    "text",
    "type",
    "annotation",
    "relevant",
    "urls",
}

OUTPUT_COLUMNS = [
    "id",
    "source",
    "created_at",
    "text_raw",
    "original_type",
    "annotation",
    "relevant",
    "urls",
]

ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")


@dataclass(frozen=True)
class NormalizationReport:
    input_rows: int
    output_rows: int
    missing_text_rows: int
    missing_timestamp_rows: int
    missing_id_rows: int
    duplicate_id_rows: int
    encoding_used: str

    @property
    def dropped_rows(self) -> int:
        return self.input_rows - self.output_rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize the raw static Twitter dataset for NLP analysis."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=None,
        help=(
            "Path to the raw CSV. If omitted, the script uses the only CSV found "
            "in data/raw/."
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Path where the normalized CSV will be saved.",
    )
    return parser.parse_args()


def resolve_project_path(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


def resolve_input_path(input_path: Path | None) -> Path:
    if input_path is not None:
        path = resolve_project_path(input_path)
        if not path.exists():
            raise FileNotFoundError(f"Input CSV not found: {path}")
        if not path.is_file():
            raise FileNotFoundError(f"Input path is not a file: {path}")
        if path.suffix.lower() != ".csv":
            raise ValueError(f"Input file must be a CSV: {path}")
        return path

    csv_files = sorted(RAW_DIR.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {RAW_DIR}")
    if len(csv_files) > 1:
        file_list = "\n  - ".join(str(path) for path in csv_files)
        raise ValueError(
            "Multiple CSV files found in data/raw/. Please pass --input explicitly:\n"
            f"  - {file_list}"
        )
    return csv_files[0]


def read_csv_with_encoding_fallback(input_path: Path) -> tuple[pd.DataFrame, str]:
    last_error: UnicodeDecodeError | None = None

    # Social datasets are often exported from mixed environments, so try a
    # conservative list of encodings before giving up.
    for encoding in ENCODINGS_TO_TRY:
        try:
            df = pd.read_csv(
                input_path,
                dtype={"id": "string"},
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

    blank_columns = [column for column in df.columns if not str(column).strip()]
    if blank_columns:
        raise ValueError("CSV contains blank column name(s).")

    missing_columns = sorted(REQUIRED_COLUMNS.difference(df.columns))
    if missing_columns:
        available = ", ".join(df.columns)
        missing = ", ".join(missing_columns)
        raise ValueError(
            f"Missing required column(s): {missing}\nAvailable columns: {available}"
        )


def normalize_dataset(df: pd.DataFrame, encoding_used: str) -> tuple[pd.DataFrame, NormalizationReport]:
    validate_columns(df)

    # Only map the agreed raw fields into the modeling-ready schema. The
    # qualitative metadata is retained, but never derived into model features.
    normalized = pd.DataFrame(
        {
            "id": df["id"].astype("string").str.strip(),
            "source": "twitter_static_dataset",
            "created_at": pd.to_datetime(df["date"], errors="coerce", utc=True),
            "text_raw": df["text"].astype("string").str.strip(),
            "original_type": df["type"],
            "annotation": df["annotation"],
            "relevant": df["relevant"],
            "urls": df["urls"],
        }
    )

    rows_before_cleaning = len(normalized)
    invalid_text = normalized["text_raw"].isna() | normalized["text_raw"].eq("")
    invalid_timestamp = normalized["created_at"].isna()
    invalid_id = normalized["id"].isna() | normalized["id"].eq("")

    if invalid_timestamp.any():
        print(f"Warning: dropping {invalid_timestamp.sum()} row(s) with unparsable dates.")
    if invalid_text.any():
        print(f"Warning: dropping {invalid_text.sum()} row(s) without text.")
    if invalid_id.any():
        print(f"Warning: dropping {invalid_id.sum()} row(s) without id.")

    # Drop incomplete records before de-duplication so duplicate counts only
    # describe otherwise usable rows.
    normalized = normalized.loc[
        ~(invalid_text | invalid_timestamp | invalid_id), OUTPUT_COLUMNS
    ].copy()

    rows_before_dedup = len(normalized)
    normalized = normalized.drop_duplicates(subset="id", keep="first")
    duplicates_removed = rows_before_dedup - len(normalized)
    if duplicates_removed:
        print(f"Warning: removed {duplicates_removed} duplicate row(s) by id.")

    normalized = normalized.sort_values("created_at").reset_index(drop=True)

    report = NormalizationReport(
        input_rows=rows_before_cleaning,
        output_rows=len(normalized),
        missing_text_rows=int(invalid_text.sum()),
        missing_timestamp_rows=int(invalid_timestamp.sum()),
        missing_id_rows=int(invalid_id.sum()),
        duplicate_id_rows=int(duplicates_removed),
        encoding_used=encoding_used,
    )

    return normalized, report


def print_final_report(report: NormalizationReport, output_path: Path) -> None:
    print("\nNormalization report")
    print("--------------------")
    print(f"Encoding used: {report.encoding_used}")
    print(f"Rows loaded: {report.input_rows}")
    print(f"Rows dropped - missing text: {report.missing_text_rows}")
    print(f"Rows dropped - missing/unparsable timestamp: {report.missing_timestamp_rows}")
    print(f"Rows dropped - missing id: {report.missing_id_rows}")
    print(f"Duplicate ids removed: {report.duplicate_id_rows}")
    print(f"Rows saved: {report.output_rows}")
    print(f"Total rows not saved: {report.dropped_rows}")
    print(f"Output file: {output_path}")


def main() -> int:
    args = parse_args()

    try:
        input_path = resolve_input_path(args.input)
        output_path = resolve_project_path(args.output)

        print(f"Loading CSV: {input_path}")
        df, encoding_used = read_csv_with_encoding_fallback(input_path)

        print(f"Available columns: {', '.join(df.columns)}")
        print(f"Raw rows: {len(df)}")

        normalized, report = normalize_dataset(df, encoding_used)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        normalized.to_csv(output_path, index=False)
        print_final_report(report, output_path)

    except FileNotFoundError as exc:
        print(f"File error: {exc}", file=sys.stderr)
        return 1
    except UnicodeDecodeError as exc:
        print(f"Encoding error: {exc}", file=sys.stderr)
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
