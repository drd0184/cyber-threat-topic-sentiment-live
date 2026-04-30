"""
Apply VADER sentiment analysis to the live topic-assigned dataset.

VADER is applied only to text_raw because the raw text preserves punctuation,
capitalization, negations, and expressive cues. text_clean remains reserved for
topic assignment.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NLTK_DATA_DIR = PROJECT_ROOT / "data" / "nltk_data"

DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "04_live_lda_topics_dataset.csv"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "05_live_sentiment_dataset.csv"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "live" / "live_sentiment_vader_report.md"

REQUIRED_COLUMNS = [
    "id",
    "created_at",
    "source",
    "source_name",
    "source_type",
    "title",
    "text_raw",
    "text_clean",
    "analysis_role",
    "dominant_topic",
    "dominant_topic_probability",
    "topic_label",
    "topic_confidence",
    "topic_assignment_status",
]

ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")
VADER_RESOURCE = "sentiment/vader_lexicon.zip"
METHODOLOGICAL_NOTE = (
    "VADER viene applicato a text_raw perche il testo grezzo conserva "
    "punteggiatura, maiuscole, negazioni e segnali espressivi utili alla "
    "sentiment analysis. text_clean resta riservato al topic assignment."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Apply VADER sentiment analysis to live topic-assigned records."
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
                    "title": "string",
                    "text_raw": "string",
                    "text_clean": "string",
                    "analysis_role": "string",
                    "topic_label": "string",
                    "topic_confidence": "string",
                    "topic_assignment_status": "string",
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


def apply_vader(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df)
    ensure_vader_resource()

    sentiment_df = df.copy()
    original_text_raw = sentiment_df["text_raw"].copy()
    analyzer = SentimentIntensityAnalyzer()

    scores = sentiment_df["text_raw"].fillna("").map(analyzer.polarity_scores)
    sentiment_df["vader_neg"] = scores.map(lambda score: score["neg"])
    sentiment_df["vader_neu"] = scores.map(lambda score: score["neu"])
    sentiment_df["vader_pos"] = scores.map(lambda score: score["pos"])
    sentiment_df["vader_compound"] = scores.map(lambda score: score["compound"])
    sentiment_df["sentiment_class"] = sentiment_df["vader_compound"].map(classify_sentiment)
    sentiment_df["text_raw"] = original_text_raw

    return sentiment_df


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


def sentiment_distribution_rows(df: pd.DataFrame) -> list[list[object]]:
    counts = (
        df["sentiment_class"]
        .fillna("UNKNOWN")
        .astype("string")
        .value_counts()
        .rename_axis("sentiment_class")
        .reset_index(name="rows")
    )
    total = int(counts["rows"].sum())
    return [
        [row.sentiment_class, int(row.rows), f"{percentage(row.rows, total):.2f}%"]
        for row in counts.itertuples(index=False)
    ]


def sentiment_cross_rows(df: pd.DataFrame, group_columns: list[str]) -> list[list[object]]:
    grouped = (
        df.groupby(group_columns + ["sentiment_class"], dropna=False)
        .size()
        .rename("rows")
        .reset_index()
        .sort_values(group_columns + ["rows"], ascending=[True] * len(group_columns) + [False])
    )

    rows = []
    for row in grouped.itertuples(index=False):
        values = []
        for column in group_columns:
            value = getattr(row, column)
            values.append(value if pd.notna(value) else "UNKNOWN")
        values.extend([row.sentiment_class if pd.notna(row.sentiment_class) else "UNKNOWN", int(row.rows)])
        rows.append(values)
    return rows


def title_for_report(value: object) -> str:
    title = "" if pd.isna(value) else str(value).replace("|", "/").replace("\n", " ")
    if len(title) > 140:
        title = title[:137] + "..."
    return title


def extreme_sentiment_rows(df: pd.DataFrame, ascending: bool) -> list[list[object]]:
    columns = ["id", "created_at", "source_type", "topic_label", "vader_compound", "title"]
    selected = df.sort_values("vader_compound", ascending=ascending).head(10)
    rows = []
    for row in selected[columns].itertuples(index=False):
        rows.append(
            [
                row.id,
                row.created_at,
                row.source_type,
                row.topic_label,
                f"{float(row.vader_compound):.4f}",
                title_for_report(row.title),
            ]
        )
    return rows


def build_report(df: pd.DataFrame, input_rows: int, encoding_used: str) -> str:
    compound = df["vader_compound"].astype(float)

    return "\n\n".join(
        [
            "# Live VADER Sentiment Report",
            "## Summary",
            markdown_table(
                ["Metric", "Value"],
                [
                    ["Input rows", input_rows],
                    ["Output rows", len(df)],
                    ["Mean vader_compound", f"{float(compound.mean()):.4f}"],
                    ["Min vader_compound", f"{float(compound.min()):.4f}"],
                    ["Max vader_compound", f"{float(compound.max()):.4f}"],
                    ["Encoding used", encoding_used],
                ],
            ),
            "## Sentiment Class Distribution",
            markdown_table(
                ["sentiment_class", "rows", "percent_dataset"],
                sentiment_distribution_rows(df),
            ),
            "## Sentiment Class by Source Type",
            markdown_table(
                ["source_type", "sentiment_class", "rows"],
                sentiment_cross_rows(df, ["source_type"]),
            ),
            "## Sentiment Class by Analysis Role",
            markdown_table(
                ["analysis_role", "sentiment_class", "rows"],
                sentiment_cross_rows(df, ["analysis_role"]),
            ),
            "## Sentiment Class by Topic",
            markdown_table(
                ["dominant_topic", "topic_label", "sentiment_class", "rows"],
                sentiment_cross_rows(df, ["dominant_topic", "topic_label"]),
            ),
            "## Top 10 Most Negative Texts",
            markdown_table(
                ["id", "created_at", "source_type", "topic_label", "vader_compound", "title"],
                extreme_sentiment_rows(df, ascending=True),
            ),
            "## Top 10 Most Positive Texts",
            markdown_table(
                ["id", "created_at", "source_type", "topic_label", "vader_compound", "title"],
                extreme_sentiment_rows(df, ascending=False),
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


def print_summary(df: pd.DataFrame, output_path: Path, report_path: Path) -> None:
    compound = df["vader_compound"].astype(float)
    print("Live VADER sentiment")
    print("====================")
    print(f"Input/output rows: {len(df)}")
    print(f"Mean vader_compound: {float(compound.mean()):.4f}")
    print(f"Min vader_compound: {float(compound.min()):.4f}")
    print(f"Max vader_compound: {float(compound.max()):.4f}")
    print("Sentiment distribution:")
    for sentiment_class, count in df["sentiment_class"].value_counts().items():
        print(f"  {sentiment_class}: {count}")
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
        sentiment_df = apply_vader(df)
        report = build_report(sentiment_df, input_rows=len(df), encoding_used=encoding_used)
        write_outputs(sentiment_df, report, output_path, report_path)
        print_summary(sentiment_df, output_path, report_path)
    except Exception as exc:
        print(f"Live VADER sentiment error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
