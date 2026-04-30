"""
Preprocess cybersecurity social text for topic modeling.

text_raw is preserved unchanged for sentiment analysis with VADER. The new
text_clean column is intended for LDA/topic modeling only. Qualitative metadata
such as original_type, annotation, relevant, and urls is preserved when present,
but should not be used as model features.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import re
import sys
from pathlib import Path

import pandas as pd

try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
except ImportError as exc:
    nltk = None
    stopwords = None
    WordNetLemmatizer = None
    NLTK_IMPORT_ERROR = exc
else:
    NLTK_IMPORT_ERROR = None


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
NLTK_DATA_DIR = PROJECT_ROOT / "data" / "nltk_data"
DEFAULT_INPUT_PATH = PROCESSED_DIR / "02_filtered_dataset.csv"
DEFAULT_OUTPUT_PATH = PROCESSED_DIR / "03_preprocessed_dataset.csv"

REQUIRED_COLUMNS = {"id", "created_at", "text_raw"}
ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")
NLTK_RESOURCES = {
    "stopwords": "corpora/stopwords",
    "wordnet": "corpora/wordnet",
    "omw-1.4": "corpora/omw-1.4",
}
DOMAIN_STOPWORDS = {
    "amp",
    "like",
    "get",
    "got",
    "make",
    "made",
    "take",
    "way",
    "one",
    "two",
    "many",
    "much",
    "people",
    "think",
    "need",
    "know",
    "want",
    "would",
    "could",
    "should",
    "also",
    "please",
    "great",
    "love",
    "talk",
    "show",
    "part",
    "set",
    "issue",
    "new",
    "day",
    "today",
    "tweet",
    "account",
    "blog",
    "find",
    "almost",
    "xlabor",
    "mydatasens",
    "kunde",
    "dauertest",
}

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
MENTION_PATTERN = re.compile(r"(?<!\w)@[A-Za-z0-9_]+")
HASHTAG_PATTERN = re.compile(r"(?<!\w)#([A-Za-z0-9_]+)")
NON_LETTER_PATTERN = re.compile(r"[^a-z\s]")
WHITESPACE_PATTERN = re.compile(r"\s+")


@dataclass(frozen=True)
class PreprocessReport:
    input_rows: int
    empty_text_clean_rows: int
    output_rows: int
    encoding_used: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create text_clean for LDA topic modeling while preserving text_raw."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="Path to the filtered CSV.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Path where the preprocessed CSV will be saved.",
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


def ensure_nltk_resources() -> None:
    if NLTK_IMPORT_ERROR is not None:
        raise RuntimeError(
            "The 'nltk' package is not installed. Install it with 'pip install nltk' "
            "and rerun this script."
        ) from NLTK_IMPORT_ERROR

    NLTK_DATA_DIR.mkdir(parents=True, exist_ok=True)
    nltk_data_path = str(NLTK_DATA_DIR)
    if nltk_data_path not in nltk.data.path:
        nltk.data.path.insert(0, nltk_data_path)

    for package_name, resource_path in NLTK_RESOURCES.items():
        try:
            nltk.data.find(resource_path)
        except LookupError:
            print(f"Downloading missing NLTK resource: {package_name}")
            if not nltk.download(package_name, download_dir=nltk_data_path, quiet=True):
                raise RuntimeError(f"Could not download NLTK resource: {package_name}")


def preprocess_text(
    text: str,
    stop_words: set[str],
    lemmatizer: WordNetLemmatizer,
) -> str:
    text = text.lower()
    text = URL_PATTERN.sub(" ", text)
    text = MENTION_PATTERN.sub(" ", text)
    text = HASHTAG_PATTERN.sub(r"\1", text)
    text = NON_LETTER_PATTERN.sub(" ", text)
    text = WHITESPACE_PATTERN.sub(" ", text).strip()

    tokens = []
    for token in text.split():
        if token in stop_words:
            continue
        if token.isnumeric():
            continue
        if len(token) < 3:
            continue
        tokens.append(lemmatizer.lemmatize(token))

    return " ".join(tokens)


def preprocess_dataset(df: pd.DataFrame, encoding_used: str) -> tuple[pd.DataFrame, PreprocessReport]:
    validate_columns(df)
    ensure_nltk_resources()

    # Domain stopwords remove frequent conversational/noisy terms observed in
    # early LDA topics while preserving cyber terms such as attack, cve, ddos,
    # ransomware, vulnerability, malware, exploit, breach, and security.
    stop_words = set(stopwords.words("english")).union(DOMAIN_STOPWORDS)
    lemmatizer = WordNetLemmatizer()

    preprocessed = df.copy()
    raw_text = preprocessed["text_raw"].astype("string")

    # Keep text_raw intact. All cleanup is written to a separate modeling column.
    preprocessed["text_clean"] = raw_text.fillna("").map(
        lambda value: preprocess_text(value, stop_words, lemmatizer)
    )

    empty_text_clean_mask = preprocessed["text_clean"].eq("")
    empty_text_clean_rows = int(empty_text_clean_mask.sum())
    preprocessed = preprocessed.loc[~empty_text_clean_mask].reset_index(drop=True)

    report = PreprocessReport(
        input_rows=len(df),
        empty_text_clean_rows=empty_text_clean_rows,
        output_rows=len(preprocessed),
        encoding_used=encoding_used,
    )

    return preprocessed, report


def print_examples(df: pd.DataFrame, max_examples: int = 5) -> None:
    print("\nExamples")
    print("--------")
    for index, row in df.head(max_examples).iterrows():
        print(f"[{index + 1}] text_raw: {row['text_raw']}")
        print(f"    text_clean: {row['text_clean']}")


def print_final_report(report: PreprocessReport, df: pd.DataFrame, output_path: Path) -> None:
    print("\nText preprocessing report")
    print("-------------------------")
    print(f"Encoding used: {report.encoding_used}")
    print(f"Initial rows: {report.input_rows}")
    print(f"Rows removed - empty text_clean: {report.empty_text_clean_rows}")
    print(f"Final rows: {report.output_rows}")
    print(f"Output file: {output_path}")
    print_examples(df)


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

        preprocessed, report = preprocess_dataset(df, encoding_used)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        preprocessed.to_csv(output_path, index=False)
        print_final_report(report, preprocessed, output_path)

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
