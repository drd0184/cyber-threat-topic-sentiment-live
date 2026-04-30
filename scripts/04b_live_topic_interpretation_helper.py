"""
Build interpretation aids for manually labeling live LDA topics.

This script is diagnostic/read-only. It summarizes the trained live LDA topic
assignments and topic words, but does not modify datasets, run VADER, compute
P2, or touch the dashboard.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_TOPICS_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "04_live_lda_topics_dataset.csv"
DEFAULT_TOPIC_WORDS_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "04_live_lda_topic_words.csv"
DEFAULT_TABLE_OUTPUT_PATH = PROJECT_ROOT / "reports" / "live" / "live_topic_interpretation_table.csv"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "live" / "live_topic_interpretation_report.md"

TOPICS_REQUIRED_COLUMNS = [
    "id",
    "created_at",
    "source_type",
    "source_name",
    "title",
    "text_clean",
    "url",
    "dominant_topic",
    "dominant_topic_probability",
]
TOPIC_WORDS_REQUIRED_COLUMNS = ["topic_id", "top_words"]

ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")
TOP_N = 10


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create tables and report to support manual interpretation of live LDA topics."
    )
    parser.add_argument("--topics-input", type=Path, default=DEFAULT_TOPICS_INPUT_PATH)
    parser.add_argument("--topic-words-input", type=Path, default=DEFAULT_TOPIC_WORDS_INPUT_PATH)
    parser.add_argument("--table-output", type=Path, default=DEFAULT_TABLE_OUTPUT_PATH)
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
            df = pd.read_csv(input_path, dtype="string", encoding=encoding, low_memory=False)
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


def prepare_topics(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df, TOPICS_REQUIRED_COLUMNS, "topics")
    prepared = df.copy()
    prepared["dominant_topic"] = pd.to_numeric(prepared["dominant_topic"], errors="coerce")
    prepared["dominant_topic_probability"] = pd.to_numeric(
        prepared["dominant_topic_probability"], errors="coerce"
    )
    prepared["created_at"] = pd.to_datetime(prepared["created_at"], errors="coerce", utc=True)
    prepared = prepared.loc[
        prepared["dominant_topic"].notna()
        & prepared["dominant_topic_probability"].notna()
        & prepared["dominant_topic"].ge(0)
    ].copy()
    if prepared.empty:
        raise ValueError("No valid assigned topics found after excluding dominant_topic = -1.")
    prepared["dominant_topic"] = prepared["dominant_topic"].astype(int)
    return prepared


def prepare_topic_words(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df, TOPIC_WORDS_REQUIRED_COLUMNS, "topic words")
    prepared = df.copy()
    prepared["topic_id"] = pd.to_numeric(prepared["topic_id"], errors="coerce")
    prepared = prepared.loc[prepared["topic_id"].notna()].copy()
    prepared["topic_id"] = prepared["topic_id"].astype(int)
    return prepared


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


def top_tokens(text_clean: pd.Series, top_n: int = TOP_N) -> list[tuple[str, int]]:
    counter: Counter[str] = Counter()
    for text in text_clean.fillna("").astype(str):
        counter.update(text.split())
    return counter.most_common(top_n)


def format_distribution(series: pd.Series, total: int, top_n: int | None = None) -> str:
    counts = series.fillna("UNKNOWN").astype("string").replace("", "UNKNOWN").value_counts()
    if top_n is not None:
        counts = counts.head(top_n)
    return "; ".join(
        f"{label}: {int(count)} ({percentage(count, total):.2f}%)"
        for label, count in counts.items()
    )


def representative_titles(group: pd.DataFrame, top_n: int = TOP_N) -> list[dict[str, object]]:
    columns = [
        "title",
        "source_type",
        "source_name",
        "created_at",
        "dominant_topic_probability",
        "url",
    ]
    selected = group.sort_values("dominant_topic_probability", ascending=False).head(top_n)
    rows = []
    for row in selected[columns].itertuples(index=False):
        rows.append(
            {
                "title": "" if pd.isna(row.title) else str(row.title),
                "source_type": "" if pd.isna(row.source_type) else str(row.source_type),
                "source_name": "" if pd.isna(row.source_name) else str(row.source_name),
                "created_at": row.created_at.isoformat() if isinstance(row.created_at, pd.Timestamp) else "",
                "dominant_topic_probability": float(row.dominant_topic_probability),
                "url": "" if pd.isna(row.url) else str(row.url),
            }
        )
    return rows


def format_representative_titles(rows: list[dict[str, object]]) -> str:
    formatted = []
    for row in rows:
        title = str(row["title"]).replace("\n", " ").replace("|", "/")
        formatted.append(
            f"{title} [{row['source_type']} / {row['source_name']} / "
            f"{row['dominant_topic_probability']:.4f}]"
        )
    return " || ".join(formatted)


def suggest_label(top_words: str) -> str:
    words = [word.strip().lower() for word in str(top_words).split(",") if word.strip()]
    word_set = set(words)
    if {"malware", "ransomware"} & word_set:
        return "Preliminary: Malware / Ransomware Activity"
    if {"vulnerability", "cve", "exploit"} & word_set:
        return "Preliminary: Vulnerability / Exploit Signals"
    if {"credential", "account", "authentication", "access"} & word_set:
        return "Preliminary: Access / Credential Risk"
    if {"ddos", "botnet"} & word_set:
        return "Preliminary: DDoS / Botnet Signals"
    if {"privacy", "phone", "fraud", "crime"} & word_set:
        return "Preliminary: Privacy / Fraud / Abuse"
    if {"macos", "file", "command", "script"} & word_set:
        return "Preliminary: Endpoint / File Execution"
    return "Preliminary label only; manual review required"


def build_interpretation_table(topics_df: pd.DataFrame, topic_words_df: pd.DataFrame) -> pd.DataFrame:
    top_words_map = topic_words_df.set_index("topic_id")["top_words"].to_dict()
    total_docs = len(topics_df)
    rows = []
    for topic_id in sorted(topics_df["dominant_topic"].unique()):
        group = topics_df.loc[topics_df["dominant_topic"].eq(topic_id)].copy()
        docs_assigned = len(group)
        top_words = str(top_words_map.get(int(topic_id), ""))
        representative = representative_titles(group)
        tokens = top_tokens(group["text_clean"], TOP_N)
        rows.append(
            {
                "topic_id": int(topic_id),
                "top_words": top_words,
                "docs_assigned": docs_assigned,
                "percent_docs": percentage(docs_assigned, total_docs),
                "avg_dominant_topic_probability": round(
                    float(group["dominant_topic_probability"].mean()), 4
                ),
                "source_type_distribution": format_distribution(group["source_type"], docs_assigned),
                "top_10_source_name": format_distribution(group["source_name"], docs_assigned, top_n=TOP_N),
                "top_10_representative_titles": format_representative_titles(representative),
                "top_10_tokens": ", ".join(f"{token} ({count})" for token, count in tokens),
                "suggested_label": suggest_label(top_words),
            }
        )
    return pd.DataFrame(rows)


def title_rows(group: pd.DataFrame) -> list[list[object]]:
    rows = []
    for item in representative_titles(group):
        title = str(item["title"]).replace("|", "/")
        if len(title) > 140:
            title = title[:137] + "..."
        rows.append(
            [
                title,
                item["source_type"],
                item["source_name"],
                item["created_at"],
                f"{item['dominant_topic_probability']:.4f}",
                item["url"],
            ]
        )
    return rows


def distribution_rows(series: pd.Series, total: int, top_n: int | None = None) -> list[list[object]]:
    counts = series.fillna("UNKNOWN").astype("string").replace("", "UNKNOWN").value_counts()
    if top_n is not None:
        counts = counts.head(top_n)
    return [[label, int(count), f"{percentage(count, total):.2f}%"] for label, count in counts.items()]


def build_report(topics_df: pd.DataFrame, interpretation_df: pd.DataFrame) -> str:
    sections = [
        "# Live Topic Interpretation Helper",
        "Support report for manual interpretation of live LDA topics. Suggested labels are preliminary and must be reviewed manually.",
    ]
    for row in interpretation_df.sort_values("topic_id").itertuples(index=False):
        topic_id = int(row.topic_id)
        group = topics_df.loc[topics_df["dominant_topic"].eq(topic_id)]
        token_rows = [
            [token, int(count)]
            for token, count in top_tokens(group["text_clean"], TOP_N)
        ]
        sections.extend(
            [
                f"## Topic {topic_id}",
                markdown_table(
                    ["Field", "Value"],
                    [
                        ["Top words", row.top_words],
                        ["Documents", int(row.docs_assigned)],
                        ["Percent documents", f"{float(row.percent_docs):.2f}%"],
                        ["Average dominant topic probability", f"{float(row.avg_dominant_topic_probability):.4f}"],
                        ["Possible preliminary interpretation", row.suggested_label],
                    ],
                ),
                "### Main Sources",
                markdown_table(
                    ["source_type", "rows", "percent_topic"],
                    distribution_rows(group["source_type"], len(group)),
                ),
                "### Top Source Names",
                markdown_table(
                    ["source_name", "rows", "percent_topic"],
                    distribution_rows(group["source_name"], len(group), top_n=TOP_N),
                ),
                "### Representative Titles",
                markdown_table(
                    [
                        "title",
                        "source_type",
                        "source_name",
                        "created_at",
                        "dominant_topic_probability",
                        "url",
                    ],
                    title_rows(group),
                ),
                "### Top Tokens",
                markdown_table(["token", "count"], token_rows),
            ]
        )
    sections.extend(
        [
            "## Methodological Note",
            "Questa tabella serve solo a supportare l'interpretazione manuale dei topic LDA live. Non modifica dataset, non calcola sentiment, non calcola P2 e non aggiorna dashboard.",
        ]
    )
    return "\n\n".join(sections) + "\n"


def write_outputs(table: pd.DataFrame, report: str, table_path: Path, report_path: Path) -> None:
    table_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    table.to_csv(table_path, index=False, encoding="utf-8")
    report_path.write_text(report, encoding="utf-8")


def print_summary(table: pd.DataFrame, table_path: Path, report_path: Path) -> None:
    print("Live topic interpretation helper")
    print("================================")
    print(f"Topics summarized: {len(table)}")
    print(f"Table CSV: {table_path}")
    print(f"Report: {report_path}")


def main() -> int:
    args = parse_args()
    topics_input_path = resolve_project_path(args.topics_input)
    topic_words_input_path = resolve_project_path(args.topic_words_input)
    table_output_path = resolve_project_path(args.table_output)
    report_path = resolve_project_path(args.report)

    try:
        validate_file(topics_input_path, "Topics input CSV")
        validate_file(topic_words_input_path, "Topic words input CSV")
        topics_raw, _ = read_csv_with_encoding_fallback(topics_input_path)
        topic_words_raw, _ = read_csv_with_encoding_fallback(topic_words_input_path)
        topics_df = prepare_topics(topics_raw)
        topic_words_df = prepare_topic_words(topic_words_raw)
        interpretation_table = build_interpretation_table(topics_df, topic_words_df)
        report = build_report(topics_df, interpretation_table)
        write_outputs(interpretation_table, report, table_output_path, report_path)
        print_summary(interpretation_table, table_output_path, report_path)
    except Exception as exc:
        print(f"Live topic interpretation helper error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
