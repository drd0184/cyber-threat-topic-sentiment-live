"""
Preprocess live filtered text for topic modeling/topic assignment.

text_raw is preserved unchanged for later VADER sentiment analysis. The new
text_clean column is intended for topic modeling/topic assignment only. This
script does not run LDA, topic assignment, VADER, P2, or dashboard export.
"""

from __future__ import annotations

import argparse
from collections import Counter
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
NLTK_DATA_DIR = PROJECT_ROOT / "data" / "nltk_data"
DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "02_live_filtered_dataset.csv"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "03_live_preprocessed_dataset.csv"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "live" / "live_preprocess_report.md"

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
    "thing",
    "really",
    "say",
    "thank",
    "come",
    "work",
    "look",
    "first",
    "still",
    "right",
    "good",
    "bad",
    "comment",
    "comments",
    "link",
    "links",
    "submitted",
    "submit",
    "post",
    "posted",
    "thread",
    "subreddit",
    "reddit",
    "article",
    "source",
    "anyone",
    "something",
    "looking",
    "trying",
}

CYBER_TERMS_TO_KEEP = {
    "attack",
    "vulnerability",
    "vulnerable",
    "cve",
    "ransomware",
    "ddos",
    "malware",
    "exploit",
    "exploited",
    "breach",
    "leak",
    "leaked",
    "botnet",
    "phishing",
    "security",
    "cybersecurity",
    "cyber",
    "infosec",
    "microsoft",
    "wannacry",
    "patch",
    "zero",
    "zeroday",
    "0day",
    "trojan",
    "spyware",
    "backdoor",
    "injection",
    "sql",
    "xss",
    "rce",
    "threat",
    "hacker",
    "cloud",
    "data",
    "password",
    "credential",
    "authentication",
    "encryption",
    "decrypt",
    "remote",
    "code",
    "execution",
    "denial",
    "service",
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
SPECIAL_CHARS_PATTERN = re.compile(r"[^a-z0-9\s]")
WHITESPACE_PATTERN = re.compile(r"\s+")


@dataclass(frozen=True)
class PreprocessSummary:
    initial_rows: int
    empty_text_clean_rows: int
    final_rows: int
    mean_text_clean_tokens: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create text_clean for live topic modeling/topic assignment while preserving text_raw."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="Path to data/live/processed/02_live_filtered_dataset.csv.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Path to data/live/processed/03_live_preprocessed_dataset.csv.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=DEFAULT_REPORT_PATH,
        help="Path to reports/live/live_preprocess_report.md.",
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


def build_stopwords() -> set[str]:
    base_stopwords = set(stopwords.words("english"))
    combined = base_stopwords.union(DOMAIN_STOPWORDS)
    return combined.difference(CYBER_TERMS_TO_KEEP)


def preprocess_text(text: object, stop_words: set[str], lemmatizer: WordNetLemmatizer) -> str:
    value = "" if pd.isna(text) else str(text)
    value = value.lower()
    value = URL_PATTERN.sub(" ", value)
    value = MENTION_PATTERN.sub(" ", value)
    value = HASHTAG_PATTERN.sub(r"\1", value)
    value = SPECIAL_CHARS_PATTERN.sub(" ", value)
    value = WHITESPACE_PATTERN.sub(" ", value).strip()

    tokens: list[str] = []
    for token in value.split():
        if token in stop_words:
            continue
        if token.isnumeric():
            continue
        if len(token) < 3:
            continue
        tokens.append(lemmatizer.lemmatize(token))

    return " ".join(tokens)


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


def token_lengths(text_clean: pd.Series) -> pd.Series:
    return text_clean.fillna("").astype("string").map(lambda value: len(str(value).split()))


def top_tokens(text_clean: pd.Series, top_n: int = 30) -> list[tuple[str, int]]:
    counter: Counter[str] = Counter()
    for text in text_clean.fillna("").astype(str):
        counter.update(text.split())
    return counter.most_common(top_n)


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


def preprocess_dataset(df: pd.DataFrame) -> tuple[pd.DataFrame, PreprocessSummary, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, list[tuple[str, int]]]:
    validate_columns(df)
    ensure_nltk_resources()

    before_source_type = source_distribution(df, "source_type")
    before_analysis_role = source_distribution(df, "analysis_role")

    stop_words = build_stopwords()
    lemmatizer = WordNetLemmatizer()

    preprocessed = df.copy()
    original_text_raw = preprocessed["text_raw"].copy()
    preprocessed["text_clean"] = preprocessed["text_raw"].map(
        lambda value: preprocess_text(value, stop_words, lemmatizer)
    )
    preprocessed["text_raw"] = original_text_raw

    empty_text_clean_mask = preprocessed["text_clean"].fillna("").astype("string").str.strip().eq("")
    empty_text_clean_rows = int(empty_text_clean_mask.sum())
    preprocessed = preprocessed.loc[~empty_text_clean_mask].reset_index(drop=True)

    clean_token_lengths = token_lengths(preprocessed["text_clean"])
    mean_tokens = round(float(clean_token_lengths.mean()), 2) if len(preprocessed) else 0.0
    summary = PreprocessSummary(
        initial_rows=len(df),
        empty_text_clean_rows=empty_text_clean_rows,
        final_rows=len(preprocessed),
        mean_text_clean_tokens=mean_tokens,
    )

    after_source_type = source_distribution(preprocessed, "source_type")
    after_analysis_role = source_distribution(preprocessed, "analysis_role")
    frequent_tokens = top_tokens(preprocessed["text_clean"], top_n=30)
    return (
        preprocessed,
        summary,
        before_source_type,
        after_source_type,
        before_analysis_role,
        after_analysis_role,
        frequent_tokens,
    )


def build_report(
    summary: PreprocessSummary,
    before_source_type: pd.DataFrame,
    after_source_type: pd.DataFrame,
    before_analysis_role: pd.DataFrame,
    after_analysis_role: pd.DataFrame,
    frequent_tokens: list[tuple[str, int]],
) -> str:
    top_token_text = ", ".join(f"{token} ({count})" for token, count in frequent_tokens) or "n/a"
    return "\n\n".join(
        [
            "# Live Preprocess Report",
            "Preprocessing report for `data/live/processed/02_live_filtered_dataset.csv`. `text_raw` is preserved unchanged; `text_clean` is created for later topic modeling/topic assignment.",
            "## Summary",
            markdown_table(
                ["Metric", "Value"],
                [
                    ["Initial rows", summary.initial_rows],
                    ["Rows removed because text_clean is empty", summary.empty_text_clean_rows],
                    ["Final rows", summary.final_rows],
                    ["Mean text_clean length in tokens", summary.mean_text_clean_tokens],
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
            "## Top 30 Tokens After Preprocessing",
            top_token_text,
            "## Methodological Note",
            "text_raw viene preservato per VADER; text_clean viene usato per topic modeling/topic assignment.",
        ]
    ) + "\n"


def write_outputs(preprocessed: pd.DataFrame, report: str, output_path: Path, report_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    preprocessed.to_csv(output_path, index=False, encoding="utf-8")
    report_path.write_text(report, encoding="utf-8")


def print_summary(summary: PreprocessSummary, output_path: Path, report_path: Path) -> None:
    print("Live text preprocessing")
    print("=======================")
    print(f"Initial rows: {summary.initial_rows}")
    print(f"Rows removed because text_clean is empty: {summary.empty_text_clean_rows}")
    print(f"Final rows: {summary.final_rows}")
    print(f"Mean text_clean length in tokens: {summary.mean_text_clean_tokens}")
    print(f"Output CSV: {output_path}")
    print(f"Report: {report_path}")


def main() -> int:
    args = parse_args()
    input_path = resolve_project_path(args.input)
    output_path = resolve_project_path(args.output)
    report_path = resolve_project_path(args.report)

    try:
        df = load_dataset(input_path)
        (
            preprocessed,
            summary,
            before_source_type,
            after_source_type,
            before_analysis_role,
            after_analysis_role,
            frequent_tokens,
        ) = preprocess_dataset(df)
        report = build_report(
            summary,
            before_source_type,
            after_source_type,
            before_analysis_role,
            after_analysis_role,
            frequent_tokens,
        )
        write_outputs(preprocessed, report, output_path, report_path)
        print_summary(summary, output_path, report_path)
    except Exception as exc:
        print(f"Preprocess error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
