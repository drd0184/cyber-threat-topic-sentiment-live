"""
Filter noisy records from the normalized cybersecurity social dataset.

The original text is kept intact for sentiment analysis. Columns such as
original_type, annotation, and relevant are preserved when present, but they are
not used as modeling features.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import re
import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
DEFAULT_INPUT_PATH = PROCESSED_DIR / "01_static_dataset_normalized.csv"
DEFAULT_OUTPUT_PATH = PROCESSED_DIR / "02_filtered_dataset.csv"

REQUIRED_COLUMNS = {"id", "created_at", "text_raw"}
MIN_TEXT_LENGTH = 30
MAX_URL_RATIO = 0.20
ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")

# Matches http://, https://, and www. URLs while avoiding trailing punctuation
# that commonly appears after links in social posts.
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
class FilterReport:
    input_rows: int
    short_text_rows: int
    high_url_ratio_rows: int
    output_rows: int
    encoding_used: str

    @property
    def kept_percentage(self) -> float:
        if self.input_rows == 0:
            return 0.0
        return (self.output_rows / self.input_rows) * 100


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Filter short and URL-heavy records from the normalized dataset."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="Path to the normalized CSV.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Path where the filtered CSV will be saved.",
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
            df = pd.read_csv(
                input_path,
                dtype={"id": "string", "text_raw": "string"},
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


def count_url_chars(text: str) -> int:
    return sum(len(match.group(0).rstrip(".,;:!?")) for match in URL_PATTERN.finditer(text))


def filter_noise(df: pd.DataFrame, encoding_used: str) -> tuple[pd.DataFrame, FilterReport]:
    validate_columns(df)

    filtered = df.copy()
    filtered["text_raw"] = filtered["text_raw"].astype("string")

    # text_raw remains unchanged; the derived columns only support transparent
    # filtering decisions and can be inspected downstream.
    filtered["text_length"] = filtered["text_raw"].str.len()

    short_text_mask = filtered["text_length"].isna() | (
        filtered["text_length"] < MIN_TEXT_LENGTH
    )
    short_text_rows = int(short_text_mask.sum())
    filtered = filtered.loc[~short_text_mask].copy()

    filtered["url_chars"] = filtered["text_raw"].map(count_url_chars)
    filtered["url_ratio"] = filtered["url_chars"] / filtered["text_length"]

    high_url_ratio_mask = filtered["url_ratio"] > MAX_URL_RATIO
    high_url_ratio_rows = int(high_url_ratio_mask.sum())
    filtered = filtered.loc[~high_url_ratio_mask].copy()

    report = FilterReport(
        input_rows=len(df),
        short_text_rows=short_text_rows,
        high_url_ratio_rows=high_url_ratio_rows,
        output_rows=len(filtered),
        encoding_used=encoding_used,
    )

    return filtered.reset_index(drop=True), report


def print_final_report(report: FilterReport, output_path: Path) -> None:
    print("\nNoise filtering report")
    print("----------------------")
    print(f"Encoding used: {report.encoding_used}")
    print(f"Initial rows: {report.input_rows}")
    print(f"Rows removed - short text (< {MIN_TEXT_LENGTH} chars): {report.short_text_rows}")
    print(
        f"Rows removed - too many URL chars (> {MAX_URL_RATIO:.0%}): "
        f"{report.high_url_ratio_rows}"
    )
    print(f"Final rows: {report.output_rows}")
    print(f"Dataset kept: {report.kept_percentage:.2f}%")
    print(f"Output file: {output_path}")


def main() -> int:
    args = parse_args()

    try:
        input_path = resolve_project_path(args.input)
        output_path = resolve_project_path(args.output)

        validate_input_path(input_path)

        print(f"Loading CSV: {input_path}")
        df, encoding_used = read_csv_with_encoding_fallback(input_path)
        print(f"Available columns: {', '.join(df.columns)}")
        print(f"Initial rows: {len(df)}")

        filtered, report = filter_noise(df, encoding_used)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        filtered.to_csv(output_path, index=False)
        print_final_report(report, output_path)

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
