"""
Inspect the strongest negative hotspot from the corrected live P2 pipeline.

This script is read-only with respect to pipeline datasets: it loads the
corrected social/news-only P2 output and the live sentiment dataset, then
exports an inspection report and the documents contributing to the hotspot.
It does not recalculate P2.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_P2_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "07_live_p2_index_12h.csv"
DEFAULT_SENTIMENT_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "05_live_sentiment_dataset.csv"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "live" / "live_corrected_p2_hotspot_inspection.md"
DEFAULT_DOCUMENTS_OUTPUT_PATH = PROJECT_ROOT / "reports" / "live" / "live_corrected_p2_hotspot_documents.csv"

P2_REQUIRED_COLUMNS = [
    "time_window",
    "dominant_topic",
    "topic_label",
    "p2_index",
    "topic_volume",
    "topic_sentiment_sum",
    "severity",
]

SENTIMENT_REQUIRED_COLUMNS = [
    "id",
    "created_at",
    "source_type",
    "source_name",
    "topic_label",
    "dominant_topic",
    "dominant_topic_probability",
    "vader_compound",
    "sentiment_class",
    "title",
    "url",
    "text_raw",
]

DOCUMENT_COLUMNS = [
    "id",
    "created_at",
    "source_type",
    "source_name",
    "topic_label",
    "dominant_topic_probability",
    "vader_compound",
    "sentiment_class",
    "title",
    "url",
    "text_raw",
]

ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")
METHODOLOGICAL_NOTE = (
    "Questo hotspot è calcolato solo su fonti social/news. CVE/NVD non "
    "contribuisce al P2."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect the strongest negative corrected live P2 hotspot."
    )
    parser.add_argument("--p2-input", type=Path, default=DEFAULT_P2_INPUT_PATH)
    parser.add_argument("--sentiment-input", type=Path, default=DEFAULT_SENTIMENT_INPUT_PATH)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT_PATH)
    parser.add_argument("--documents-output", type=Path, default=DEFAULT_DOCUMENTS_OUTPUT_PATH)
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


def validate_columns(df: pd.DataFrame, required_columns: list[str], label: str) -> None:
    if df.empty:
        raise ValueError(f"{label} CSV is empty.")

    duplicate_columns = sorted(df.columns[df.columns.duplicated()].unique())
    if duplicate_columns:
        duplicates = ", ".join(duplicate_columns)
        raise ValueError(f"Duplicate column name(s) found in {label}: {duplicates}")

    missing_columns = [column for column in required_columns if column not in df.columns]
    if missing_columns:
        missing = ", ".join(missing_columns)
        available = ", ".join(df.columns)
        raise ValueError(f"Missing required column(s) in {label}: {missing}\nAvailable columns: {available}")


def prepare_p2(p2_df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(p2_df, P2_REQUIRED_COLUMNS, "P2")

    prepared = p2_df.copy()
    prepared["time_window"] = pd.to_datetime(prepared["time_window"], errors="coerce", utc=True)
    prepared["dominant_topic"] = pd.to_numeric(prepared["dominant_topic"], errors="coerce")
    prepared["p2_index"] = pd.to_numeric(prepared["p2_index"], errors="coerce")
    prepared["topic_volume"] = pd.to_numeric(prepared["topic_volume"], errors="coerce")
    prepared["topic_sentiment_sum"] = pd.to_numeric(
        prepared["topic_sentiment_sum"], errors="coerce"
    )

    invalid_rows = prepared["time_window"].isna() | prepared["dominant_topic"].isna() | prepared["p2_index"].isna()
    prepared = prepared.loc[~invalid_rows].copy()
    if prepared.empty:
        raise ValueError("No valid P2 rows after parsing time_window, dominant_topic, and p2_index.")

    prepared["dominant_topic"] = prepared["dominant_topic"].astype(int)
    return prepared


def prepare_sentiment(sentiment_df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(sentiment_df, SENTIMENT_REQUIRED_COLUMNS, "sentiment")

    prepared = sentiment_df.copy()
    prepared["created_at"] = pd.to_datetime(prepared["created_at"], errors="coerce", utc=True)
    prepared["dominant_topic"] = pd.to_numeric(prepared["dominant_topic"], errors="coerce")
    prepared["dominant_topic_probability"] = pd.to_numeric(
        prepared["dominant_topic_probability"], errors="coerce"
    )
    prepared["vader_compound"] = pd.to_numeric(prepared["vader_compound"], errors="coerce")

    valid_rows = (
        prepared["created_at"].notna()
        & prepared["dominant_topic"].notna()
        & prepared["vader_compound"].notna()
    )
    prepared = prepared.loc[valid_rows].copy()
    if prepared.empty:
        raise ValueError("No valid sentiment rows after parsing created_at, dominant_topic, and VADER scores.")

    prepared["dominant_topic"] = prepared["dominant_topic"].astype(int)
    prepared["time_window"] = prepared["created_at"].dt.floor("12h")
    return prepared


def find_hotspot(p2_df: pd.DataFrame) -> pd.Series:
    return p2_df.sort_values("p2_index", ascending=True).iloc[0]


def filter_hotspot_documents(sentiment_df: pd.DataFrame, hotspot: pd.Series) -> pd.DataFrame:
    hotspot_time_window = hotspot["time_window"]
    hotspot_topic = int(hotspot["dominant_topic"])
    docs = sentiment_df.loc[
        sentiment_df["time_window"].eq(hotspot_time_window)
        & sentiment_df["dominant_topic"].eq(hotspot_topic)
    ].copy()
    return docs.sort_values(["vader_compound", "created_at"], ascending=[True, True]).reset_index(drop=True)


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


def title_for_report(value: object) -> str:
    title = "" if pd.isna(value) else str(value).replace("|", "/").replace("\n", " ")
    if len(title) > 140:
        title = title[:137] + "..."
    return title


def top_negative_rows(docs: pd.DataFrame) -> list[list[object]]:
    rows = []
    columns = [
        "id",
        "created_at",
        "source_type",
        "source_name",
        "vader_compound",
        "sentiment_class",
        "title",
    ]
    for row in docs.sort_values("vader_compound", ascending=True).head(10)[columns].itertuples(index=False):
        rows.append(
            [
                row.id,
                row.created_at.isoformat() if isinstance(row.created_at, pd.Timestamp) else row.created_at,
                row.source_type,
                row.source_name,
                f"{float(row.vader_compound):.4f}",
                row.sentiment_class,
                title_for_report(row.title),
            ]
        )
    return rows


def build_report(hotspot: pd.Series, docs: pd.DataFrame, p2_encoding: str, sentiment_encoding: str) -> str:
    compound = docs["vader_compound"].astype(float)
    topic_probability = docs["dominant_topic_probability"].astype(float)
    hotspot_rows = [
        ["time_window", hotspot["time_window"].isoformat()],
        ["dominant_topic", int(hotspot["dominant_topic"])],
        ["topic_label", hotspot["topic_label"]],
        ["p2_index", f"{float(hotspot['p2_index']):.4f}"],
        ["topic_volume", int(hotspot["topic_volume"])],
        ["topic_sentiment_sum", f"{float(hotspot['topic_sentiment_sum']):.4f}"],
        ["severity", hotspot["severity"]],
    ]

    summary_rows = [
        ["Hotspot documents", len(docs)],
        ["Mean vader_compound", f"{float(compound.mean()):.4f}"],
        ["Min vader_compound", f"{float(compound.min()):.4f}"],
        ["Max vader_compound", f"{float(compound.max()):.4f}"],
        ["Mean dominant_topic_probability", f"{float(topic_probability.mean()):.4f}"],
        ["P2 CSV encoding", p2_encoding],
        ["Sentiment CSV encoding", sentiment_encoding],
    ]

    return "\n\n".join(
        [
            "# Corrected Live P2 Hotspot Inspection",
            "## Hotspot Description",
            "Strongest negative P2 hotspot in the corrected social/news-only live pipeline.",
            markdown_table(["Field", "Value"], hotspot_rows),
            "## Document Summary",
            markdown_table(["Metric", "Value"], summary_rows),
            "## Source Type Distribution",
            markdown_table(["source_type", "rows", "percent_hotspot"], distribution_rows(docs, "source_type")),
            "## Source Name Distribution",
            markdown_table(["source_name", "rows", "percent_hotspot"], distribution_rows(docs, "source_name")),
            "## Sentiment Class Distribution",
            markdown_table(["sentiment_class", "rows", "percent_hotspot"], distribution_rows(docs, "sentiment_class")),
            "## Top 10 Most Negative Documents",
            markdown_table(
                [
                    "id",
                    "created_at",
                    "source_type",
                    "source_name",
                    "vader_compound",
                    "sentiment_class",
                    "title",
                ],
                top_negative_rows(docs),
            ),
            "## Methodological Note",
            METHODOLOGICAL_NOTE,
        ]
    ) + "\n"


def write_outputs(docs: pd.DataFrame, report: str, documents_output_path: Path, report_path: Path) -> None:
    documents_output_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    output_docs = docs[DOCUMENT_COLUMNS].copy()
    output_docs["created_at"] = output_docs["created_at"].dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    output_docs.to_csv(documents_output_path, index=False, encoding="utf-8")
    report_path.write_text(report, encoding="utf-8")


def print_summary(hotspot: pd.Series, docs: pd.DataFrame, documents_output_path: Path, report_path: Path) -> None:
    print("Corrected live P2 hotspot inspection")
    print("====================================")
    print(f"Time window: {hotspot['time_window']}")
    print(f"Topic: T{int(hotspot['dominant_topic'])} | {hotspot['topic_label']}")
    print(f"P2 index: {float(hotspot['p2_index']):.4f}")
    print(f"Topic volume: {int(hotspot['topic_volume'])}")
    print(f"Topic sentiment sum: {float(hotspot['topic_sentiment_sum']):.4f}")
    print(f"Severity: {hotspot['severity']}")
    print(f"Documents exported: {len(docs)}")
    print(f"Documents CSV: {documents_output_path}")
    print(f"Report: {report_path}")


def main() -> int:
    args = parse_args()
    p2_input_path = resolve_project_path(args.p2_input)
    sentiment_input_path = resolve_project_path(args.sentiment_input)
    report_path = resolve_project_path(args.report)
    documents_output_path = resolve_project_path(args.documents_output)

    try:
        validate_file(p2_input_path, "P2 input CSV")
        validate_file(sentiment_input_path, "Sentiment input CSV")

        p2_raw, p2_encoding = read_csv_with_encoding_fallback(p2_input_path)
        sentiment_raw, sentiment_encoding = read_csv_with_encoding_fallback(sentiment_input_path)
        p2_df = prepare_p2(p2_raw)
        sentiment_df = prepare_sentiment(sentiment_raw)
        hotspot = find_hotspot(p2_df)
        docs = filter_hotspot_documents(sentiment_df, hotspot)

        if docs.empty:
            raise ValueError("No sentiment documents matched the strongest negative P2 hotspot.")

        report = build_report(hotspot, docs, p2_encoding, sentiment_encoding)
        write_outputs(docs, report, documents_output_path, report_path)
        print_summary(hotspot, docs, documents_output_path, report_path)
    except Exception as exc:
        print(f"Corrected live P2 hotspot inspection error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
