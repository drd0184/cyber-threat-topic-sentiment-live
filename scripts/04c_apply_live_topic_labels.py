"""
Apply official manual labels and confidence levels to live LDA topics.

This script updates the live topic-assigned dataset in place, preserving all
columns and adding/updating topic_label and topic_confidence. It does not train
LDA, run VADER, compute P2, or touch the dashboard.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "04_live_lda_topics_dataset.csv"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "live" / "live_topic_labels_report.md"

REQUIRED_COLUMNS = ["dominant_topic"]
ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")

TOPIC_LABELS_LIVE = {
    0: "Network Attacks / Device Access",
    1: "Command Execution / Payload Delivery",
    2: "Cybercrime / Fraud / Law Enforcement",
    3: "Memory Exploitation / Buffer & Heap Bugs",
    4: "Access Control / Process & API Abuse",
    5: "Exploit Tooling / Metasploit / RCE",
    6: "Security Risk / Exposure Management",
    7: "Cybersecurity Tools / Generic Discussion",
    8: "Microsoft / Privilege Escalation / Patch Exploitation",
    9: "Ransomware / Malware / Email Campaigns",
}

TOPIC_CONFIDENCE_LIVE = {
    0: "medium",
    1: "high",
    2: "medium",
    3: "high",
    4: "medium",
    5: "high",
    6: "medium",
    7: "low",
    8: "high",
    9: "high",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Apply official live topic labels.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_INPUT_PATH)
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
        raise ValueError(f"Missing required column(s): {', '.join(missing_columns)}")


def label_for_topic(topic: object) -> str:
    topic_id = int(topic)
    if topic_id == -1:
        return "Unassigned / Empty BoW"
    return TOPIC_LABELS_LIVE.get(topic_id, "Unknown Topic")


def confidence_for_topic(topic: object) -> str:
    topic_id = int(topic)
    if topic_id == -1:
        return "none"
    return TOPIC_CONFIDENCE_LIVE.get(topic_id, "unknown")


def apply_labels(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df)
    labeled = df.copy()
    labeled["dominant_topic"] = pd.to_numeric(labeled["dominant_topic"], errors="coerce")
    if labeled["dominant_topic"].isna().any():
        raise ValueError("dominant_topic contains unparsable values.")
    labeled["dominant_topic"] = labeled["dominant_topic"].astype(int)
    labeled["topic_label"] = labeled["dominant_topic"].map(label_for_topic)
    labeled["topic_confidence"] = labeled["dominant_topic"].map(confidence_for_topic)
    return labeled


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
    counts = df[column].fillna("UNKNOWN").astype("string").value_counts().rename_axis(column).reset_index(name="rows")
    total = len(df)
    return [
        [getattr(row, column), int(row.rows), f"{percentage(row.rows, total):.2f}%"]
        for row in counts.itertuples(index=False)
    ]


def build_report(df: pd.DataFrame, encoding_used: str) -> str:
    return "\n\n".join(
        [
            "# Live Topic Labels Report",
            "Official manual labels and confidence levels applied to the live 10-topic LDA dataset.",
            "## Summary",
            markdown_table(
                ["Metric", "Value"],
                [
                    ["Rows", len(df)],
                    ["Encoding used", encoding_used],
                    ["Output dataset", str(DEFAULT_INPUT_PATH)],
                ],
            ),
            "## Topic Label Distribution",
            markdown_table(["topic_label", "rows", "percent_dataset"], distribution_rows(df, "topic_label")),
            "## Topic Confidence Distribution",
            markdown_table(["topic_confidence", "rows", "percent_dataset"], distribution_rows(df, "topic_confidence")),
        ]
    ) + "\n"


def write_outputs(df: pd.DataFrame, report: str, output_path: Path, report_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8")
    report_path.write_text(report, encoding="utf-8")


def print_summary(df: pd.DataFrame, output_path: Path, report_path: Path) -> None:
    print("Apply live topic labels")
    print("=======================")
    print(f"Rows: {len(df)}")
    print(f"Topic labels: {df['topic_label'].nunique()}")
    print(f"Confidence distribution: {df['topic_confidence'].value_counts().to_dict()}")
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
        labeled = apply_labels(df)
        report = build_report(labeled, encoding_used)
        write_outputs(labeled, report, output_path, report_path)
        print_summary(labeled, output_path, report_path)
    except Exception as exc:
        print(f"Apply live topic labels error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
