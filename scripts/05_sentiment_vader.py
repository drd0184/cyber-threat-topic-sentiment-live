"""
Apply VADER sentiment analysis to the topic-modeled cybersecurity dataset.

VADER is intentionally applied to text_raw, not text_clean, because punctuation,
capitalization, negations, hashtags, and other social-text cues are useful for
sentiment scoring.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import sys
from pathlib import Path

import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
NLTK_DATA_DIR = PROJECT_ROOT / "data" / "nltk_data"
DEFAULT_INPUT_PATH = PROCESSED_DIR / "04_lda_topics_dataset.csv"
DEFAULT_OUTPUT_PATH = PROCESSED_DIR / "05_sentiment_dataset.csv"

REQUIRED_COLUMNS = {"id", "created_at", "text_raw", "dominant_topic"}
ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")
VADER_RESOURCE = "sentiment/vader_lexicon.zip"


@dataclass(frozen=True)
class SentimentReport:
    input_rows: int
    output_rows: int
    mean_compound: float
    min_compound: float
    max_compound: float
    encoding_used: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Apply NLTK/VADER sentiment analysis to text_raw."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="Path to the LDA topic dataset.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Path where the sentiment-enriched CSV will be saved.",
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

    missing_columns = sorted(REQUIRED_COLUMNS.difference(df.columns))
    if missing_columns:
        available = ", ".join(df.columns)
        missing = ", ".join(missing_columns)
        raise ValueError(
            f"Missing required column(s): {missing}\nAvailable columns: {available}"
        )


def ensure_vader_resource() -> None:
    NLTK_DATA_DIR.mkdir(parents=True, exist_ok=True)
    nltk_data_path = str(NLTK_DATA_DIR)
    if nltk_data_path not in nltk.data.path:
        nltk.data.path.insert(0, nltk_data_path)

    try:
        nltk.data.find(VADER_RESOURCE)
    except LookupError:
        print("Downloading missing NLTK resource: vader_lexicon")
        if not nltk.download("vader_lexicon", download_dir=nltk_data_path, quiet=True):
            raise RuntimeError("Could not download NLTK resource: vader_lexicon")


def classify_sentiment(compound: float) -> str:
    if compound <= -0.05:
        return "negative"
    if compound >= 0.05:
        return "positive"
    return "neutral"


def safe_console_text(value: object) -> str:
    text = str(value).replace("\n", " ")
    return text.encode(sys.stdout.encoding or "utf-8", errors="replace").decode(
        sys.stdout.encoding or "utf-8"
    )


def apply_vader_sentiment(df: pd.DataFrame, encoding_used: str) -> tuple[pd.DataFrame, SentimentReport]:
    validate_columns(df)
    ensure_vader_resource()

    analyzer = SentimentIntensityAnalyzer()
    sentiment_df = df.copy()

    # Do not mutate text_raw. VADER needs the original social text surface form.
    scores = sentiment_df["text_raw"].fillna("").map(analyzer.polarity_scores)
    sentiment_df["vader_neg"] = scores.map(lambda score: score["neg"])
    sentiment_df["vader_neu"] = scores.map(lambda score: score["neu"])
    sentiment_df["vader_pos"] = scores.map(lambda score: score["pos"])
    sentiment_df["vader_compound"] = scores.map(lambda score: score["compound"])
    sentiment_df["sentiment_class"] = sentiment_df["vader_compound"].map(classify_sentiment)

    report = SentimentReport(
        input_rows=len(df),
        output_rows=len(sentiment_df),
        mean_compound=float(sentiment_df["vader_compound"].mean()),
        min_compound=float(sentiment_df["vader_compound"].min()),
        max_compound=float(sentiment_df["vader_compound"].max()),
        encoding_used=encoding_used,
    )

    return sentiment_df, report


def print_examples(df: pd.DataFrame, ascending: bool, label: str) -> None:
    print(f"\n5 most {label} examples")
    print("-" * (16 + len(label)))
    examples = df.sort_values("vader_compound", ascending=ascending).head(5)
    for index, row in enumerate(examples.itertuples(index=False), start=1):
        text = safe_console_text(row.text_raw)
        print(f"[{index}] compound={row.vader_compound:.4f} | {text}")


def print_final_report(report: SentimentReport, df: pd.DataFrame, output_path: Path) -> None:
    print("\nVADER sentiment report")
    print("----------------------")
    print(f"Encoding used: {report.encoding_used}")
    print(f"Initial rows: {report.input_rows}")
    print(f"Final rows: {report.output_rows}")
    print(f"Mean vader_compound: {report.mean_compound:.4f}")
    print(f"Min vader_compound: {report.min_compound:.4f}")
    print(f"Max vader_compound: {report.max_compound:.4f}")
    print(f"Output file: {output_path}")

    print("\nSentiment class distribution")
    print("----------------------------")
    for sentiment_class, count in df["sentiment_class"].value_counts().items():
        print(f"{sentiment_class}: {count}")

    print_examples(df, ascending=True, label="negative")
    print_examples(df, ascending=False, label="positive")


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

        sentiment_df, report = apply_vader_sentiment(df, encoding_used)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        sentiment_df.to_csv(output_path, index=False)
        print_final_report(report, sentiment_df, output_path)

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
    except (RuntimeError, ValueError) as exc:
        print(f"Data validation error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
