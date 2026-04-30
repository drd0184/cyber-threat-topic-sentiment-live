"""
Assign existing static LDA topics to live cybersecurity documents.

The live pipeline does not retrain LDA. Recent documents are projected onto
the topic space learned in the static baseline so topic labels stay coherent
across static and live dashboard outputs.
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
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "04_live_topics_dataset.csv"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "live" / "live_topic_assignment_report.md"
DEFAULT_MODEL_PATH = PROJECT_ROOT / "models" / "lda_model" / "lda_model.gensim"
DEFAULT_DICTIONARY_PATH = PROJECT_ROOT / "models" / "lda_model" / "dictionary.gensim"

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
]

TOPIC_LABELS = {
    0: "Generic Vulnerability Signals",
    1: "Data Leak / Botnet / Cloud",
    2: "DDoS / Attack Protection",
    3: "CVE / Remote Exploit / Buffer Overflow",
    4: "Ransomware / Malware / Attacks",
    5: "SQL Injection / DoS / Microsoft",
    6: "Ransomware / Business Risk / WannaCry",
    7: "Zero-day / Browser Exploit Signals",
    8: "CVE / Patch / RSA BSAFE",
    9: "Cybersecurity / IoT / Botnet",
}

ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")
METHODOLOGICAL_NOTE = (
    "Il modello LDA non viene riaddestrato nella pipeline live. I documenti "
    "recenti vengono proiettati sullo spazio topic definito dalla baseline "
    "statica, cosi la dashboard mantiene topic label coerenti."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Assign topics to live documents using the existing baseline LDA model."
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
            "The 'gensim' package is required to load the LDA model and dictionary."
        ) from GENSIM_IMPORT_ERROR


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


def load_existing_lda(model_path: Path, dictionary_path: Path):
    ensure_gensim_available()
    validate_file(model_path, "LDA model")
    validate_file(dictionary_path, "LDA dictionary")
    lda_model = LdaModel.load(str(model_path))
    dictionary = Dictionary.load(str(dictionary_path))
    return lda_model, dictionary


def assign_document_topic(text_clean: object, lda_model, dictionary) -> tuple[int, float, str]:
    tokens = "" if pd.isna(text_clean) else str(text_clean)
    bow = dictionary.doc2bow(tokens.split())

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
    output["topic_label"] = output["dominant_topic"].map(TOPIC_LABELS).fillna("Unassigned")

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


def value_distribution_rows(df: pd.DataFrame, column: str) -> list[list[object]]:
    counts = (
        df[column]
        .fillna("UNKNOWN")
        .astype("string")
        .replace("", "UNKNOWN")
        .value_counts()
        .rename_axis(column)
        .reset_index(name="rows")
    )
    total = int(counts["rows"].sum())
    return [
        [getattr(row, column), int(row.rows), f"{percentage(row.rows, total):.2f}%"]
        for row in counts.itertuples(index=False)
    ]


def topic_cross_distribution_rows(df: pd.DataFrame, column: str) -> list[list[object]]:
    grouped = (
        df.groupby(["dominant_topic", "topic_label", column], dropna=False)
        .size()
        .rename("rows")
        .reset_index()
        .sort_values(["dominant_topic", "rows", column], ascending=[True, False, True])
    )
    return [
        [
            int(row.dominant_topic),
            row.topic_label,
            getattr(row, column) if pd.notna(getattr(row, column)) else "UNKNOWN",
            int(row.rows),
        ]
        for row in grouped.itertuples(index=False)
    ]


def low_probability_rows(df: pd.DataFrame) -> list[list[object]]:
    columns = ["id", "source_type", "title", "dominant_topic", "dominant_topic_probability"]
    lowest = df.sort_values("dominant_topic_probability", ascending=True).head(10)
    rows = []
    for row in lowest[columns].itertuples(index=False):
        title = "" if pd.isna(row.title) else str(row.title).replace("|", "/")
        if len(title) > 120:
            title = title[:117] + "..."
        rows.append(
            [
                row.id,
                row.source_type,
                title,
                int(row.dominant_topic),
                f"{float(row.dominant_topic_probability):.4f}",
            ]
        )
    return rows


def build_report(df: pd.DataFrame, input_rows: int, encoding_used: str) -> str:
    assigned_rows = int((df["topic_assignment_status"] == "assigned").sum())
    empty_bow_rows = int((df["topic_assignment_status"] == "empty_bow").sum())
    probabilities = df["dominant_topic_probability"].astype(float)

    return "\n\n".join(
        [
            "# Live Topic Assignment Report",
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
                ],
            ),
            "## Dominant Topic Distribution",
            markdown_table(
                ["dominant_topic", "rows", "percent_dataset"],
                value_distribution_rows(df, "dominant_topic"),
            ),
            "## Topic Label Distribution",
            markdown_table(
                ["topic_label", "rows", "percent_dataset"],
                value_distribution_rows(df, "topic_label"),
            ),
            "## Source Type Distribution by Topic",
            markdown_table(
                ["dominant_topic", "topic_label", "source_type", "rows"],
                topic_cross_distribution_rows(df, "source_type"),
            ),
            "## Analysis Role Distribution by Topic",
            markdown_table(
                ["dominant_topic", "topic_label", "analysis_role", "rows"],
                topic_cross_distribution_rows(df, "analysis_role"),
            ),
            "## Lowest Topic Probability Documents",
            markdown_table(
                ["id", "source_type", "title", "dominant_topic", "probability"],
                low_probability_rows(df),
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
    print("Live topic assignment using existing LDA")
    print("========================================")
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
        lda_model, dictionary = load_existing_lda(model_path, dictionary_path)
        topics_df = assign_topics(df, lda_model, dictionary)
        report = build_report(topics_df, input_rows=len(df), encoding_used=encoding_used)
        write_outputs(topics_df, report, output_path, report_path)
        print_summary(topics_df, output_path, report_path)
    except Exception as exc:
        print(f"Live topic assignment error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
