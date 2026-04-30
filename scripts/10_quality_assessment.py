"""
Qualitative assessment for LDA topics and P2 hot topics.

original_type, annotation, and relevant are used only as ex post quality checks.
They are not used to recompute topics, sentiment, or the P2 index.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
REPORT_TABLES_DIR = PROJECT_ROOT / "reports" / "tables"

DEFAULT_LDA_DATASET_PATH = PROCESSED_DIR / "04_lda_topics_dataset.csv"
DEFAULT_TOPIC_WORDS_PATH = PROCESSED_DIR / "04_lda_topic_words.csv"
DEFAULT_P2_PATH = PROCESSED_DIR / "07_p2_index_12h.csv"
DEFAULT_SENTIMENT_PATH = PROCESSED_DIR / "05_sentiment_dataset.csv"

DEFAULT_TOPIC_QUALITY_OUTPUT = REPORT_TABLES_DIR / "topic_quality_assessment.csv"
DEFAULT_P2_QUALITY_OUTPUT = REPORT_TABLES_DIR / "p2_hot_topics_quality.csv"
DEFAULT_P2_COMPARISON_OUTPUT = REPORT_TABLES_DIR / "p2_vs_volume_vs_sentiment.csv"

ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")

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

QUALITY_NOTES = {
    "high": "Topic semantically coherent and strongly aligned with ex-post validation.",
    "medium": "Topic mostly interpretable, but includes mixed signals.",
    "low": "Broad or noisy topic. Use with caution.",
}

HOT_SIGNAL_NOTE = "Il segnale e da interpretare come priorita informativa, non come conferma di attacco."
NOISY_TOPICS = {0, 7}

TOPIC_TYPE_KEYWORDS = {
    0: {"vulnerability", "security"},
    1: {"data", "leak", "botnet", "cloud", "email"},
    2: {"ddos", "attack", "protection"},
    3: {"cve", "remote", "exploit", "buffer", "overflow", "vuln"},
    4: {"ransomware", "malware", "attack", "hack", "threat"},
    5: {"sql", "injection", "dos", "denial", "microsoft", "vulnerability"},
    6: {"ransomware", "business", "risk", "wannacry", "attack"},
    7: {"zero", "zero-day", "browser", "exploit", "vulnerability"},
    8: {"cve", "patch", "rsa", "bsafe", "bug", "vulnerability"},
    9: {"cybersecurity", "iot", "botnet", "infosec", "patch"},
}

REQUIRED_LDA_COLUMNS = {"dominant_topic", "original_type", "annotation"}
REQUIRED_TOPIC_WORDS_COLUMNS = {"topic_id", "top_words"}
REQUIRED_P2_COLUMNS = {
    "time_window",
    "dominant_topic",
    "topic_volume",
    "topic_sentiment_sum",
    "p2_index",
    "p2_abs",
}
REQUIRED_SENTIMENT_COLUMNS = {
    "created_at",
    "dominant_topic",
    "original_type",
    "annotation",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Assess LDA topic and P2 hot topic quality with ex post labels."
    )
    parser.add_argument("--lda-dataset", type=Path, default=DEFAULT_LDA_DATASET_PATH)
    parser.add_argument("--topic-words", type=Path, default=DEFAULT_TOPIC_WORDS_PATH)
    parser.add_argument("--p2-input", type=Path, default=DEFAULT_P2_PATH)
    parser.add_argument("--sentiment-input", type=Path, default=DEFAULT_SENTIMENT_PATH)
    parser.add_argument("--topic-quality-output", type=Path, default=DEFAULT_TOPIC_QUALITY_OUTPUT)
    parser.add_argument("--p2-quality-output", type=Path, default=DEFAULT_P2_QUALITY_OUTPUT)
    parser.add_argument("--p2-comparison-output", type=Path, default=DEFAULT_P2_COMPARISON_OUTPUT)
    return parser.parse_args()


def resolve_project_path(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


def validate_input_file(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    if not path.is_file():
        raise FileNotFoundError(f"Input path is not a file: {path}")
    if path.suffix.lower() != ".csv":
        raise ValueError(f"Input file must be a CSV: {path}")


def read_csv_with_encoding_fallback(path: Path) -> pd.DataFrame:
    last_error: UnicodeDecodeError | None = None
    for encoding in ENCODINGS_TO_TRY:
        try:
            return pd.read_csv(path, encoding=encoding, low_memory=False)
        except UnicodeDecodeError as exc:
            last_error = exc

    raise UnicodeDecodeError(
        last_error.encoding if last_error else "unknown",
        last_error.object if last_error else b"",
        last_error.start if last_error else 0,
        last_error.end if last_error else 1,
        f"Could not decode CSV with encodings: {', '.join(ENCODINGS_TO_TRY)}",
    )


def require_columns(df: pd.DataFrame, required_columns: set[str], dataset_name: str) -> None:
    missing = sorted(required_columns.difference(df.columns))
    if missing:
        raise ValueError(
            f"{dataset_name} missing required column(s): {', '.join(missing)}. "
            f"Available columns: {', '.join(df.columns)}"
        )


def normalize_text(value: object) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip().lower()


def topic_label(topic_id: int) -> str:
    return TOPIC_LABELS.get(int(topic_id), f"Topic {int(topic_id)}")


def parse_topic_words(topic_words_df: pd.DataFrame) -> pd.DataFrame:
    require_columns(topic_words_df, REQUIRED_TOPIC_WORDS_COLUMNS, "Topic words CSV")
    topic_words = topic_words_df[["topic_id", "top_words"]].copy()
    topic_words["topic_id"] = pd.to_numeric(topic_words["topic_id"], errors="coerce")
    topic_words = topic_words.dropna(subset=["topic_id"])
    topic_words["topic_id"] = topic_words["topic_id"].astype(int)
    topic_words["top_words"] = topic_words["top_words"].fillna("").astype(str)
    return topic_words.sort_values("topic_id").reset_index(drop=True)


def prepare_lda_dataset(lda_df: pd.DataFrame) -> pd.DataFrame:
    require_columns(lda_df, REQUIRED_LDA_COLUMNS, "LDA topics dataset")
    df = lda_df.copy()
    df["dominant_topic"] = pd.to_numeric(df["dominant_topic"], errors="coerce")
    df = df.dropna(subset=["dominant_topic"])
    df["dominant_topic"] = df["dominant_topic"].astype(int)
    df["annotation_norm"] = df["annotation"].map(normalize_text)
    df["original_type_norm"] = df["original_type"].map(normalize_text)
    return df


def prepare_p2(p2_df: pd.DataFrame, topic_words: pd.DataFrame) -> pd.DataFrame:
    require_columns(p2_df, REQUIRED_P2_COLUMNS, "P2 CSV")
    df = p2_df.copy()
    df["time_window"] = pd.to_datetime(df["time_window"], errors="coerce", utc=True)
    df["dominant_topic"] = pd.to_numeric(df["dominant_topic"], errors="coerce")

    numeric_columns = [
        "topic_volume",
        "topic_sentiment_sum",
        "topic_sentiment_mean",
        "p2_index",
        "p2_abs",
    ]
    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    df = df.dropna(subset=["time_window", "dominant_topic", "p2_index", "p2_abs"])
    df["dominant_topic"] = df["dominant_topic"].astype(int)
    df["topic_label"] = df["dominant_topic"].map(topic_label)
    df = df.merge(topic_words, left_on="dominant_topic", right_on="topic_id", how="left")
    df = df.drop(columns=["topic_id"])
    df["top_words"] = df["top_words"].fillna("")
    return df.sort_values(["time_window", "dominant_topic"]).reset_index(drop=True)


def prepare_sentiment(sentiment_df: pd.DataFrame) -> pd.DataFrame:
    require_columns(sentiment_df, REQUIRED_SENTIMENT_COLUMNS, "Sentiment CSV")
    df = sentiment_df.copy()
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce", utc=True)
    df["time_window"] = df["created_at"].dt.floor("12h")
    df["dominant_topic"] = pd.to_numeric(df["dominant_topic"], errors="coerce")
    df = df.dropna(subset=["time_window", "dominant_topic"])
    df["dominant_topic"] = df["dominant_topic"].astype(int)
    df["annotation_norm"] = df["annotation"].map(normalize_text)
    df["original_type_norm"] = df["original_type"].map(normalize_text)
    return df


def most_common_with_pct(series: pd.Series, total: int) -> tuple[str, float]:
    if total == 0:
        return "", 0.0
    counts = series.fillna("").astype(str).replace("", "unknown").value_counts()
    if counts.empty:
        return "", 0.0
    top_value = counts.index[0]
    top_pct = float(counts.iloc[0] / total * 100)
    return top_value, top_pct


def distribution_string(series: pd.Series) -> str:
    counts = series.fillna("").astype(str).replace("", "unknown").value_counts()
    total = int(counts.sum())
    if total == 0:
        return ""
    parts = [f"{value}: {count} ({count / total * 100:.1f}%)" for value, count in counts.items()]
    return "; ".join(parts)


def type_matches_topic(topic_id: int, original_type: str) -> bool:
    keywords = TOPIC_TYPE_KEYWORDS.get(int(topic_id), set())
    normalized_type = normalize_text(original_type)
    if not normalized_type:
        return False
    return any(keyword in normalized_type for keyword in keywords)


def assess_quality(topic_id: int, top_annotation: str, threat_pct: float, top_type: str) -> tuple[str, str]:
    type_coherent = type_matches_topic(topic_id, top_type)
    if top_annotation == "threat" and threat_pct >= 50:
        return "high", QUALITY_NOTES["high"]
    if threat_pct >= 30 and type_coherent:
        return "medium", QUALITY_NOTES["medium"]
    if threat_pct >= 30:
        return "medium", QUALITY_NOTES["medium"]
    if type_coherent:
        return "medium", QUALITY_NOTES["medium"]
    return "low", QUALITY_NOTES["low"]


def build_topic_quality(lda_df: pd.DataFrame, topic_words: pd.DataFrame) -> pd.DataFrame:
    total_docs = len(lda_df)
    rows = []

    topic_words_map = topic_words.set_index("topic_id")["top_words"].to_dict()
    for topic_id, group in lda_df.groupby("dominant_topic", sort=True):
        doc_count = len(group)
        annotation_top, annotation_top_pct = most_common_with_pct(group["annotation_norm"], doc_count)
        original_type_top, original_type_top_pct = most_common_with_pct(group["original_type_norm"], doc_count)
        threat_pct = float((group["annotation_norm"] == "threat").mean() * 100)
        irrelevant_pct = float((group["annotation_norm"] == "irrelevant").mean() * 100)
        quality_score, quality_note = assess_quality(
            int(topic_id), annotation_top, threat_pct, original_type_top
        )

        rows.append(
            {
                "dominant_topic": int(topic_id),
                "topic_label": topic_label(int(topic_id)),
                "documents": int(doc_count),
                "percent_total": doc_count / total_docs * 100,
                "top_words": topic_words_map.get(int(topic_id), ""),
                "top_original_type_ex_post": original_type_top,
                "top_original_type_pct": original_type_top_pct,
                "top_annotation_ex_post": annotation_top,
                "top_annotation_pct": annotation_top_pct,
                "threat_pct": threat_pct,
                "irrelevant_pct": irrelevant_pct,
                "quality_score": quality_score,
                "quality_note": quality_note,
            }
        )

    return pd.DataFrame(rows).sort_values("dominant_topic").reset_index(drop=True)


def interpret_hot_topic(
    row: pd.Series,
    threat_pct: float,
    irrelevant_pct: float,
    top_original_type: str,
    original_type_coherent: bool,
) -> str:
    return HOT_SIGNAL_NOTE


def build_p2_hot_topic_quality(p2_df: pd.DataFrame, sentiment_df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    top_negative = p2_df.sort_values("p2_index", ascending=True).head(10)

    for _, hot_row in top_negative.iterrows():
        subset = sentiment_df[
            (sentiment_df["time_window"] == hot_row["time_window"])
            & (sentiment_df["dominant_topic"] == hot_row["dominant_topic"])
        ]
        total = len(subset)
        threat_pct = float((subset["annotation_norm"] == "threat").mean() * 100) if total else 0.0
        irrelevant_pct = (
            float((subset["annotation_norm"] == "irrelevant").mean() * 100) if total else 0.0
        )
        top_annotation, top_annotation_pct = most_common_with_pct(subset["annotation_norm"], total)
        top_original_type, top_original_type_pct = most_common_with_pct(
            subset["original_type_norm"], total
        )
        original_type_coherent = type_matches_topic(
            int(hot_row["dominant_topic"]), top_original_type
        )

        rows.append(
            {
                "time_window": hot_row["time_window"],
                "dominant_topic": int(hot_row["dominant_topic"]),
                "topic_label": hot_row["topic_label"],
                "top_words": hot_row["top_words"],
                "topic_volume": hot_row["topic_volume"],
                "topic_sentiment_sum": hot_row["topic_sentiment_sum"],
                "p2_index": hot_row["p2_index"],
                "p2_abs": hot_row["p2_abs"],
                "top_annotation_ex_post": top_annotation,
                "top_annotation_pct": top_annotation_pct,
                "top_original_type_ex_post": top_original_type,
                "top_original_type_pct": top_original_type_pct,
                "top_original_type_coherent": original_type_coherent,
                "annotation_distribution_ex_post": distribution_string(subset["annotation_norm"]),
                "original_type_distribution_ex_post": distribution_string(subset["original_type_norm"]),
                "threat_pct": threat_pct,
                "irrelevant_pct": irrelevant_pct,
                "interpretation": interpret_hot_topic(
                    hot_row,
                    threat_pct,
                    irrelevant_pct,
                    top_original_type,
                    original_type_coherent,
                ),
            }
        )

    return pd.DataFrame(rows)


def build_p2_metric_comparison(p2_df: pd.DataFrame) -> pd.DataFrame:
    ranking_specs = [
        ("top_topic_volume", p2_df.sort_values("topic_volume", ascending=False).head(10)),
        (
            "top_negative_sentiment_sum",
            p2_df.sort_values("topic_sentiment_sum", ascending=True).head(10),
        ),
        ("top_negative_p2_index", p2_df.sort_values("p2_index", ascending=True).head(10)),
    ]
    rows = []
    for ranking_type, ranking_df in ranking_specs:
        for rank, (_, row) in enumerate(ranking_df.iterrows(), start=1):
            rows.append(
                {
                    "ranking_type": ranking_type,
                    "rank": rank,
                    "time_window": row["time_window"],
                    "dominant_topic": int(row["dominant_topic"]),
                    "topic_label": row["topic_label"],
                    "topic_volume": row["topic_volume"],
                    "topic_sentiment_sum": row["topic_sentiment_sum"],
                    "p2_index": row["p2_index"],
                    "top_words": row["top_words"],
                }
            )
    return pd.DataFrame(rows)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    output_df = df.copy()
    for column in output_df.columns:
        if pd.api.types.is_datetime64_any_dtype(output_df[column]):
            output_df[column] = output_df[column].dt.strftime("%Y-%m-%d %H:%M:%S%z")
    output_df.to_csv(path, index=False, encoding="utf-8")


def print_report(topic_quality: pd.DataFrame, p2_quality: pd.DataFrame) -> None:
    quality_counts = topic_quality["quality_score"].value_counts().to_dict()
    high_count = int(quality_counts.get("high", 0))
    medium_count = int(quality_counts.get("medium", 0))
    low_count = int(quality_counts.get("low", 0))

    reliable = topic_quality[topic_quality["quality_score"].isin(["high", "medium"])]
    reliable = reliable.sort_values(["quality_score", "threat_pct"], ascending=[True, False])
    noisy = topic_quality[
        (topic_quality["quality_score"] == "low")
        | (topic_quality["dominant_topic"].isin(NOISY_TOPICS))
    ].sort_values(["quality_score", "irrelevant_pct"], ascending=[True, False])

    primary = p2_quality.sort_values("p2_index", ascending=True).iloc[0]

    print("Quality assessment completed.")
    print(f"  Topic quality counts: high={high_count}, medium={medium_count}, low={low_count}")
    print(
        "  Most reliable topics: "
        + ", ".join(
            f"T{int(row.dominant_topic)} {row.topic_label}"
            for row in reliable.head(5).itertuples(index=False)
        )
    )
    print(
        "  Noisy / low-confidence topics: "
        + ", ".join(
            f"T{int(row.dominant_topic)} {row.topic_label}"
            for row in noisy.head(5).itertuples(index=False)
        )
    )
    print(
        "  Primary negative P2 hot topic: "
        "informational priority, not an incident confirmation "
        f"(threat_pct={primary['threat_pct']:.1f}%, "
        f"irrelevant_pct={primary['irrelevant_pct']:.1f}%)"
    )


def main() -> int:
    args = parse_args()

    try:
        lda_path = resolve_project_path(args.lda_dataset)
        topic_words_path = resolve_project_path(args.topic_words)
        p2_path = resolve_project_path(args.p2_input)
        sentiment_path = resolve_project_path(args.sentiment_input)
        topic_quality_output = resolve_project_path(args.topic_quality_output)
        p2_quality_output = resolve_project_path(args.p2_quality_output)
        p2_comparison_output = resolve_project_path(args.p2_comparison_output)

        for path in (lda_path, topic_words_path, p2_path, sentiment_path):
            validate_input_file(path)

        lda_df = prepare_lda_dataset(read_csv_with_encoding_fallback(lda_path))
        topic_words = parse_topic_words(read_csv_with_encoding_fallback(topic_words_path))
        p2_df = prepare_p2(read_csv_with_encoding_fallback(p2_path), topic_words)
        sentiment_df = prepare_sentiment(read_csv_with_encoding_fallback(sentiment_path))

        topic_quality = build_topic_quality(lda_df, topic_words)
        p2_quality = build_p2_hot_topic_quality(p2_df, sentiment_df)
        p2_comparison = build_p2_metric_comparison(p2_df)

        write_csv(topic_quality, topic_quality_output)
        write_csv(p2_quality, p2_quality_output)
        write_csv(p2_comparison, p2_comparison_output)

        print(f"Saved topic quality assessment: {topic_quality_output}")
        print(f"Saved P2 hot topics quality: {p2_quality_output}")
        print(f"Saved P2 comparison table: {p2_comparison_output}")
        print_report(topic_quality, p2_quality)
    except FileNotFoundError as exc:
        print(f"File error: {exc}", file=sys.stderr)
        return 1
    except UnicodeDecodeError as exc:
        print(f"Encoding error: {exc}", file=sys.stderr)
        return 1
    except pd.errors.EmptyDataError:
        print("Data validation error: input CSV is empty.", file=sys.stderr)
        return 1
    except pd.errors.ParserError as exc:
        print(f"CSV parsing error: {exc}", file=sys.stderr)
        return 1
    except (RuntimeError, ValueError, KeyError) as exc:
        print(f"Data validation error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
