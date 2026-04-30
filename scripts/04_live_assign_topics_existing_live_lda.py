"""
Assign topics to live documents using the official live LDA model.

This operational step does not retrain LDA. It projects the current
social/news live corpus onto the topic space saved in models/live_lda_model/.
Manual topic labels are applied by scripts/04c_apply_live_topic_labels.py.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd

try:
    from gensim.corpora import Dictionary
    from gensim.models import LdaModel
except ImportError as exc:
    Dictionary = None
    LdaModel = None
    GENSIM_IMPORT_ERROR = exc
else:
    GENSIM_IMPORT_ERROR = None


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "03_live_preprocessed_dataset.csv"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "04_live_lda_topics_dataset.csv"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "live" / "live_topic_assignment_report.md"
DEFAULT_MODEL_PATH = PROJECT_ROOT / "models" / "live_lda_model" / "lda_model.gensim"
DEFAULT_DICTIONARY_PATH = PROJECT_ROOT / "models" / "live_lda_model" / "dictionary.gensim"

REQUIRED_COLUMNS = [
    "id",
    "created_at",
    "source",
    "source_name",
    "source_type",
    "title",
    "text_raw",
    "text_clean",
]

ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")
METHODOLOGICAL_NOTE = (
    "Il modello LDA live ufficiale non viene riaddestrato nella pipeline operativa. "
    "I documenti social/news recenti vengono proiettati sullo spazio topic salvato "
    "in models/live_lda_model/. Il retraining LDA resta uno step manuale o periodico separato."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Assign topics using the existing official live LDA model."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT_PATH)
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL_PATH)
    parser.add_argument("--dictionary", type=Path, default=DEFAULT_DICTIONARY_PATH)
    return parser.parse_args()


def resolve_project_path(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


def validate_file(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"{label} not found: {path}")
    if not path.is_file():
        raise FileNotFoundError(f"{label} is not a file: {path}")


def ensure_gensim_available() -> None:
    if GENSIM_IMPORT_ERROR is not None:
        raise RuntimeError(
            "The 'gensim' package is required to load the live LDA model and dictionary."
        ) from GENSIM_IMPORT_ERROR


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
        raise ValueError(f"Duplicate column name(s) found in CSV: {', '.join(duplicate_columns)}")

    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        available = ", ".join(df.columns)
        raise ValueError(
            f"Missing required column(s): {', '.join(missing_columns)}\n"
            f"Available columns: {available}"
        )


def load_live_lda(model_path: Path, dictionary_path: Path):
    ensure_gensim_available()
    validate_file(model_path, "Live LDA model")
    validate_file(dictionary_path, "Live LDA dictionary")
    lda_model = LdaModel.load(str(model_path))
    dictionary = Dictionary.load(str(dictionary_path))
    return lda_model, dictionary


def assign_document_topic(text_clean: object, lda_model, dictionary) -> tuple[int, float, str]:
    text = "" if pd.isna(text_clean) else str(text_clean)
    tokens = text.split()
    bow = dictionary.doc2bow(tokens)

    if not bow:
        return -1, 0.0, "empty_bow"

    topic_distribution = lda_model.get_document_topics(bow, minimum_probability=0)
    topic_id, probability = max(topic_distribution, key=lambda item: item[1])
    return int(topic_id), float(probability), "assigned"


def assign_topics(df: pd.DataFrame, lda_model, dictionary) -> pd.DataFrame:
    validate_columns(df)

    output = df.copy()
    assignments = output["text_clean"].map(
        lambda value: assign_document_topic(value, lda_model, dictionary)
    )

    output["dominant_topic"] = assignments.map(lambda item: item[0]).astype(int)
    output["dominant_topic_probability"] = assignments.map(lambda item: item[1]).astype(float)
    output["topic_assignment_status"] = assignments.map(lambda item: item[2])
    return output


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


def build_report(df: pd.DataFrame, input_rows: int, encoding_used: str) -> str:
    assigned_rows = int((df["topic_assignment_status"] == "assigned").sum())
    empty_bow_rows = int((df["topic_assignment_status"] == "empty_bow").sum())
    probabilities = df["dominant_topic_probability"].astype(float)

    return "\n\n".join(
        [
            "# Live LDA Topic Assignment Report",
            "## Summary",
            markdown_table(
                ["Metric", "Value"],
                [
                    ["Input rows", input_rows],
                    ["Assigned rows", assigned_rows],
                    ["Empty BOW rows", empty_bow_rows],
                    ["Mean dominant_topic_probability", f"{float(probabilities.mean()):.4f}"],
                    ["Min dominant_topic_probability", f"{float(probabilities.min()):.4f}"],
                    ["Max dominant_topic_probability", f"{float(probabilities.max()):.4f}"],
                    ["Encoding used", encoding_used],
                    ["Model", str(DEFAULT_MODEL_PATH)],
                    ["Dictionary", str(DEFAULT_DICTIONARY_PATH)],
                ],
            ),
            "## Topic Assignment Status",
            markdown_table(
                ["topic_assignment_status", "rows", "percent_dataset"],
                distribution_rows(df, "topic_assignment_status"),
            ),
            "## Dominant Topic Distribution",
            markdown_table(
                ["dominant_topic", "rows", "percent_dataset"],
                distribution_rows(df, "dominant_topic"),
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
    assigned_rows = int((df["topic_assignment_status"] == "assigned").sum())
    empty_bow_rows = int((df["topic_assignment_status"] == "empty_bow").sum())
    print("Live topic assignment using official live LDA")
    print("============================================")
    print(f"Input rows: {len(df)}")
    print(f"Assigned rows: {assigned_rows}")
    print(f"Empty BOW rows: {empty_bow_rows}")
    print(f"Mean topic probability: {df['dominant_topic_probability'].mean():.4f}")
    print(f"Output CSV: {output_path}")
    print(f"Report: {report_path}")


def main() -> int:
    args = parse_args()
    input_path = resolve_project_path(args.input)
    output_path = resolve_project_path(args.output)
    report_path = resolve_project_path(args.report)
    model_path = resolve_project_path(args.model)
    dictionary_path = resolve_project_path(args.dictionary)

    try:
        validate_file(input_path, "Input CSV")
        df, encoding_used = read_csv_with_encoding_fallback(input_path)
        lda_model, dictionary = load_live_lda(model_path, dictionary_path)
        topics_df = assign_topics(df, lda_model, dictionary)
        report = build_report(topics_df, input_rows=len(df), encoding_used=encoding_used)
        write_outputs(topics_df, report, output_path, report_path)
        print_summary(topics_df, output_path, report_path)
    except Exception as exc:
        print(f"Live LDA topic assignment error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
