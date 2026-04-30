"""
Export optimized JSON data for the local React intelligence dashboard.

The script reads already-produced pipeline outputs. It does not rerun NLP,
topic modeling, sentiment analysis, or P2. original_type, annotation, and
relevant are used only through the ex-post quality assessment tables.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
TABLES_DIR = PROJECT_ROOT / "reports" / "tables"
DASHBOARD_DATA_DIR = PROJECT_ROOT / "dashboard" / "src" / "data"

DEFAULT_P2_INPUT = PROCESSED_DIR / "07_p2_index_12h.csv"
DEFAULT_SENTIMENT_INPUT = PROCESSED_DIR / "05_sentiment_dataset.csv"
DEFAULT_TOPIC_WORDS_INPUT = PROCESSED_DIR / "04_lda_topic_words.csv"
DEFAULT_TOPIC_QUALITY_INPUT = TABLES_DIR / "topic_quality_assessment.csv"
DEFAULT_HOT_TOPICS_QUALITY_INPUT = TABLES_DIR / "p2_hot_topics_quality.csv"
DEFAULT_VALIDATION_INPUT = TABLES_DIR / "p2_vs_volume_vs_sentiment.csv"

ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")
MAX_POSTS = 5000
MAX_TEXT_CHARS = 500
NOISY_TOPICS = {0, 7}

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

TOPIC_META = {
    0: {"category": "noisy_generic", "icon": "scan", "accent": "slate"},
    1: {"category": "data_leak", "icon": "database", "accent": "blue"},
    2: {"category": "ddos", "icon": "activity", "accent": "cyan"},
    3: {"category": "cve_vulnerability", "icon": "bug", "accent": "amber"},
    4: {"category": "ransomware_malware", "icon": "shield_alert", "accent": "red"},
    5: {"category": "cve_vulnerability", "icon": "bug", "accent": "amber"},
    6: {"category": "ransomware_malware", "icon": "shield_alert", "accent": "red"},
    7: {"category": "noisy_generic", "icon": "scan", "accent": "slate"},
    8: {"category": "cve_vulnerability", "icon": "alert_triangle", "accent": "amber"},
    9: {"category": "botnet_iot", "icon": "radio", "accent": "cyan"},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export dashboard JSON data.")
    parser.add_argument("--p2-input", type=Path, default=DEFAULT_P2_INPUT)
    parser.add_argument("--sentiment-input", type=Path, default=DEFAULT_SENTIMENT_INPUT)
    parser.add_argument("--topic-words", type=Path, default=DEFAULT_TOPIC_WORDS_INPUT)
    parser.add_argument("--topic-quality", type=Path, default=DEFAULT_TOPIC_QUALITY_INPUT)
    parser.add_argument("--hot-topics-quality", type=Path, default=DEFAULT_HOT_TOPICS_QUALITY_INPUT)
    parser.add_argument("--validation", type=Path, default=DEFAULT_VALIDATION_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DASHBOARD_DATA_DIR)
    parser.add_argument("--max-posts", type=int, default=MAX_POSTS)
    parser.add_argument("--max-text-chars", type=int, default=MAX_TEXT_CHARS)
    return parser.parse_args()


def resolve(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


def validate_csv(path: Path) -> None:
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"Input CSV not found: {path}")
    if path.suffix.lower() != ".csv":
        raise ValueError(f"Input must be a CSV: {path}")


def read_csv(path: Path) -> pd.DataFrame:
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


def require_columns(df: pd.DataFrame, columns: set[str], label: str) -> None:
    missing = sorted(columns.difference(df.columns))
    if missing:
        raise ValueError(f"{label} missing columns: {', '.join(missing)}")


def label_for(topic_id: int) -> str:
    return TOPIC_LABELS.get(int(topic_id), f"Topic {int(topic_id)}")


def quality_note_for(score: object) -> str:
    return QUALITY_NOTES.get(str(score).lower(), "Topic confidence not available.")


def words(value: object) -> list[str]:
    if pd.isna(value):
        return []
    return [part.strip() for part in str(value).split(",") if part.strip()]


def iso_datetime(series: pd.Series) -> pd.Series:
    return pd.to_datetime(series, errors="coerce", utc=True).dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def trim_text(value: object, max_chars: int) -> str:
    text = "" if pd.isna(value) else " ".join(str(value).split())
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3].rstrip() + "..."


def cybercon_level(p2_abs: float) -> int:
    if p2_abs >= 30:
        return 1
    if p2_abs >= 15:
        return 2
    if p2_abs >= 8:
        return 3
    if p2_abs >= 3:
        return 4
    return 5


def clean_value(value: Any) -> Any:
    if value is None:
        return None
    if hasattr(value, "item"):
        return clean_value(value.item())
    if isinstance(value, pd.Timestamp):
        return None if pd.isna(value) else value.isoformat()
    if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
        return None
    if pd.isna(value):
        return None
    return value


def clean_payload(payload: Any) -> Any:
    if isinstance(payload, dict):
        return {key: clean_payload(value) for key, value in payload.items()}
    if isinstance(payload, list):
        return [clean_payload(value) for value in payload]
    return clean_value(payload)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(clean_payload(payload), ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def prepare_topic_words(df: pd.DataFrame) -> pd.DataFrame:
    require_columns(df, {"topic_id", "top_words"}, "Topic words")
    out = df[["topic_id", "top_words"]].copy()
    out["topic_id"] = pd.to_numeric(out["topic_id"], errors="coerce")
    out = out.dropna(subset=["topic_id"])
    out["topic_id"] = out["topic_id"].astype(int)
    out["top_words_list"] = out["top_words"].map(words)
    return out


def prepare_topic_quality(df: pd.DataFrame) -> pd.DataFrame:
    require_columns(
        df,
        {
            "dominant_topic",
            "quality_score",
            "quality_note",
            "threat_pct",
            "irrelevant_pct",
            "top_original_type_ex_post",
            "top_annotation_ex_post",
            "documents",
        },
        "Topic quality",
    )
    out = df.copy()
    out["dominant_topic"] = pd.to_numeric(out["dominant_topic"], errors="coerce")
    out = out.dropna(subset=["dominant_topic"])
    out["dominant_topic"] = out["dominant_topic"].astype(int)
    for col in [
        "documents",
        "percent_total",
        "top_original_type_pct",
        "top_annotation_pct",
        "threat_pct",
        "irrelevant_pct",
    ]:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    out["quality_score"] = out["quality_score"].fillna("unknown").astype(str).str.lower()
    out["quality_note"] = out["quality_score"].map(quality_note_for)
    return out


def prepare_hot_quality(df: pd.DataFrame) -> pd.DataFrame:
    require_columns(
        df,
        {
            "time_window",
            "dominant_topic",
            "threat_pct",
            "irrelevant_pct",
            "top_original_type_ex_post",
            "interpretation",
        },
        "Hot topics quality",
    )
    out = df.copy()
    out["time_window"] = iso_datetime(out["time_window"])
    out["dominant_topic"] = pd.to_numeric(out["dominant_topic"], errors="coerce")
    out = out.dropna(subset=["time_window", "dominant_topic"])
    out["dominant_topic"] = out["dominant_topic"].astype(int)
    for col in [
        "topic_volume",
        "topic_sentiment_sum",
        "p2_index",
        "p2_abs",
        "top_annotation_pct",
        "top_original_type_pct",
        "threat_pct",
        "irrelevant_pct",
    ]:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    if "top_original_type_coherent" in out.columns:
        out["top_original_type_coherent"] = out["top_original_type_coherent"].astype(str).str.lower().isin(["true", "1", "yes"])
    if "interpretation" in out.columns:
        out["interpretation"] = HOT_SIGNAL_NOTE
    return out


def prepare_p2(df: pd.DataFrame, topic_words: pd.DataFrame, topic_quality: pd.DataFrame) -> pd.DataFrame:
    require_columns(
        df,
        {
            "time_window",
            "dominant_topic",
            "topic_volume",
            "topic_sentiment_sum",
            "topic_sentiment_mean",
            "total_window_volume",
            "topic_volume_share",
            "volume_factor",
            "sentiment_factor",
            "p2_index",
            "p2_abs",
            "p2_direction",
        },
        "P2",
    )
    out = df.copy()
    out["time_window"] = iso_datetime(out["time_window"])
    out["dominant_topic"] = pd.to_numeric(out["dominant_topic"], errors="coerce")
    out = out.dropna(subset=["time_window", "dominant_topic"])
    out["dominant_topic"] = out["dominant_topic"].astype(int)
    out["topic_label"] = out["dominant_topic"].map(label_for)
    for col in [
        "topic_volume",
        "topic_sentiment_sum",
        "topic_sentiment_mean",
        "total_window_volume",
        "topic_volume_share",
        "volume_factor",
        "sentiment_factor",
        "p2_index",
        "p2_abs",
    ]:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    out = out.merge(topic_words[["topic_id", "top_words", "top_words_list"]], left_on="dominant_topic", right_on="topic_id", how="left").drop(columns=["topic_id"])
    quality_cols = ["dominant_topic", "quality_score", "quality_note", "threat_pct", "irrelevant_pct"]
    out = out.merge(topic_quality[quality_cols], on="dominant_topic", how="left")
    out["top_words"] = out["top_words_list"].apply(lambda value: value if isinstance(value, list) else [])
    out["topic_quality"] = out.apply(
        lambda row: {
            "quality_score": row.get("quality_score"),
            "quality_note": row.get("quality_note"),
            "threat_pct": row.get("threat_pct"),
            "irrelevant_pct": row.get("irrelevant_pct"),
        },
        axis=1,
    )
    columns = [
        "time_window",
        "dominant_topic",
        "topic_label",
        "topic_volume",
        "topic_sentiment_sum",
        "topic_sentiment_mean",
        "total_window_volume",
        "topic_volume_share",
        "volume_factor",
        "sentiment_factor",
        "p2_index",
        "p2_abs",
        "p2_direction",
        "top_words",
        "topic_quality",
    ]
    return out[columns].sort_values(["time_window", "dominant_topic"]).reset_index(drop=True)


def prepare_posts(df: pd.DataFrame, max_posts: int, max_chars: int) -> pd.DataFrame:
    require_columns(
        df,
        {"id", "created_at", "dominant_topic", "vader_compound", "sentiment_class", "text_raw"},
        "Sentiment dataset",
    )
    out = df.copy()
    out["created_at_dt"] = pd.to_datetime(out["created_at"], errors="coerce", utc=True)
    out["dominant_topic"] = pd.to_numeric(out["dominant_topic"], errors="coerce")
    out["vader_compound"] = pd.to_numeric(out["vader_compound"], errors="coerce")
    if "dominant_topic_probability" in out.columns:
        out["dominant_topic_probability"] = pd.to_numeric(out["dominant_topic_probability"], errors="coerce")
    else:
        out["dominant_topic_probability"] = None
    out = out.dropna(subset=["created_at_dt", "dominant_topic", "vader_compound"])
    out["dominant_topic"] = out["dominant_topic"].astype(int)
    out["time_window"] = out["created_at_dt"].dt.floor("12h").dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    out["created_at"] = out["created_at_dt"].dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    out["topic_label"] = out["dominant_topic"].map(label_for)
    out["id"] = out["id"].fillna("").astype(str)
    out["text_raw"] = out["text_raw"].map(lambda value: trim_text(value, max_chars))
    out["post_relevance_score"] = out["vader_compound"].abs() * 0.7 + out["dominant_topic_probability"].fillna(0.0) * 0.3
    out = out.sort_values("post_relevance_score", ascending=False).head(max_posts)
    cols = [
        "id",
        "created_at",
        "time_window",
        "dominant_topic",
        "topic_label",
        "vader_compound",
        "sentiment_class",
        "text_raw",
        "dominant_topic_probability",
    ]
    return out[cols].sort_values(["time_window", "dominant_topic", "created_at"]).reset_index(drop=True)


def prepare_topics(
    topic_words: pd.DataFrame,
    topic_quality: pd.DataFrame,
    p2: pd.DataFrame,
    posts: pd.DataFrame,
) -> list[dict[str, Any]]:
    rows = []
    quality_map = topic_quality.set_index("dominant_topic").to_dict(orient="index")
    for topic in sorted(topic_words["topic_id"].unique()):
        topic_id = int(topic)
        topic_p2 = p2[p2["dominant_topic"] == topic_id]
        topic_posts = posts[posts["dominant_topic"] == topic_id]
        word_list = topic_words.loc[topic_words["topic_id"] == topic_id, "top_words_list"].iloc[0]
        q = quality_map.get(topic_id, {})
        rows.append(
            {
                "topic_id": topic_id,
                "topic_label": label_for(topic_id),
                "category": TOPIC_META.get(topic_id, {}).get("category", "unknown"),
                "icon": TOPIC_META.get(topic_id, {}).get("icon", "scan"),
                "accent": TOPIC_META.get(topic_id, {}).get("accent", "cyan"),
                "top_words": word_list,
                "top_5_words": word_list[:5],
                "is_noisy": topic_id in NOISY_TOPICS,
                "quality_score": q.get("quality_score"),
                "quality_note": q.get("quality_note"),
                "threat_pct": q.get("threat_pct"),
                "irrelevant_pct": q.get("irrelevant_pct"),
                "dominant_original_type_ex_post": q.get("top_original_type_ex_post"),
                "dominant_annotation_ex_post": q.get("top_annotation_ex_post"),
                "total_docs": q.get("documents"),
                "max_negative_p2": topic_p2["p2_index"].min() if not topic_p2.empty else None,
                "max_positive_p2": topic_p2["p2_index"].max() if not topic_p2.empty else None,
                "total_volume": topic_p2["topic_volume"].sum() if not topic_p2.empty else 0,
                "avg_sentiment": topic_posts["vader_compound"].mean() if not topic_posts.empty else None,
                "last_seen_window": topic_p2["time_window"].max() if not topic_p2.empty else None,
            }
        )
    return rows


def prepare_validation(df: pd.DataFrame) -> pd.DataFrame:
    require_columns(
        df,
        {"ranking_type", "rank", "time_window", "dominant_topic", "topic_label", "topic_volume", "topic_sentiment_sum", "p2_index"},
        "P2 validation",
    )
    out = df.copy()
    out["time_window"] = iso_datetime(out["time_window"])
    out["dominant_topic"] = pd.to_numeric(out["dominant_topic"], errors="coerce")
    out = out.dropna(subset=["dominant_topic", "time_window"])
    out["dominant_topic"] = out["dominant_topic"].astype(int)
    out["topic_label"] = out["dominant_topic"].map(label_for)
    for col in ["rank", "topic_volume", "topic_sentiment_sum", "p2_index"]:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    if "top_words" in out.columns:
        out["top_words"] = out["top_words"].map(words)
    return out.sort_values(["ranking_type", "rank"]).reset_index(drop=True)


def build_summary(p2: pd.DataFrame, posts: pd.DataFrame, topics: list[dict[str, Any]], topic_quality: pd.DataFrame) -> dict[str, Any]:
    hottest_negative = p2.sort_values("p2_index", ascending=True).iloc[0].to_dict()
    hottest_positive = p2.sort_values("p2_index", ascending=False).iloc[0].to_dict()
    counts = posts["sentiment_class"].value_counts()
    quality_counts = topic_quality["quality_score"].value_counts()
    reliable = (
        topic_quality[topic_quality["quality_score"].isin(["high", "medium"])]
        .sort_values(["quality_score", "threat_pct"], ascending=[True, False])
        .head(5)["dominant_topic"]
        .astype(int)
        .tolist()
    )
    noisy = (
        topic_quality[
            (topic_quality["quality_score"] == "low")
            | (topic_quality["dominant_topic"].isin(NOISY_TOPICS))
        ]
        .sort_values(["quality_score", "irrelevant_pct"], ascending=[True, False])
        .head(3)["dominant_topic"]
        .astype(int)
        .tolist()
    )
    return {
        "product_name": "CYBER THREAT HOT TOPIC INDEX",
        "subtitle": "Semantic Intelligence Monitor",
        "last_build": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "total_posts": int(len(posts)),
        "total_topics": int(len(topics)),
        "total_time_windows": int(p2["time_window"].nunique()),
        "date_min": posts["created_at"].min(),
        "date_max": posts["created_at"].max(),
        "hottest_negative": hottest_negative,
        "hottest_positive": hottest_positive,
        "average_sentiment": posts["vader_compound"].mean(),
        "negative_count": int(counts.get("negative", 0)),
        "positive_count": int(counts.get("positive", 0)),
        "neutral_count": int(counts.get("neutral", 0)),
        "high_quality_topics_count": int(quality_counts.get("high", 0)),
        "medium_quality_topics_count": int(quality_counts.get("medium", 0)),
        "low_quality_topics_count": int(quality_counts.get("low", 0)),
        "most_reliable_topics": reliable,
        "noisy_topics": noisy,
        "cybercon_level": cybercon_level(float(hottest_negative["p2_abs"])),
    }


def records(df: pd.DataFrame) -> list[dict[str, Any]]:
    return [clean_payload(row) for row in df.to_dict(orient="records")]


def main() -> int:
    args = parse_args()
    try:
        paths = {
            "p2": resolve(args.p2_input),
            "sentiment": resolve(args.sentiment_input),
            "topic_words": resolve(args.topic_words),
            "topic_quality": resolve(args.topic_quality),
            "hot_quality": resolve(args.hot_topics_quality),
            "validation": resolve(args.validation),
        }
        for path in paths.values():
            validate_csv(path)
        output_dir = resolve(args.output_dir)

        topic_words = prepare_topic_words(read_csv(paths["topic_words"]))
        topic_quality = prepare_topic_quality(read_csv(paths["topic_quality"]))
        p2 = prepare_p2(read_csv(paths["p2"]), topic_words, topic_quality)
        posts = prepare_posts(read_csv(paths["sentiment"]), args.max_posts, args.max_text_chars)
        topics = prepare_topics(topic_words, topic_quality, p2, posts)
        hot_quality = prepare_hot_quality(read_csv(paths["hot_quality"]))
        validation = prepare_validation(read_csv(paths["validation"]))
        summary = build_summary(p2, posts, topics, topic_quality)

        outputs = {
            "summary": output_dir / "summary.json",
            "p2": output_dir / "p2.json",
            "topics": output_dir / "topics.json",
            "posts": output_dir / "posts.json",
            "topic_quality": output_dir / "topic_quality.json",
            "hot_topics_quality": output_dir / "hot_topics_quality.json",
            "validation": output_dir / "validation.json",
            "p2_hot_topics_quality": output_dir / "p2_hot_topics_quality.json",
            "p2_validation": output_dir / "p2_validation.json",
        }
        write_json(outputs["summary"], summary)
        write_json(outputs["p2"], records(p2))
        write_json(outputs["topics"], topics)
        write_json(outputs["posts"], records(posts))
        write_json(outputs["topic_quality"], records(topic_quality))
        write_json(outputs["hot_topics_quality"], records(hot_quality))
        write_json(outputs["validation"], records(validation))
        write_json(outputs["p2_hot_topics_quality"], records(hot_quality))
        write_json(outputs["p2_validation"], records(validation))

        print("Dashboard JSON export completed.")
        for key, path in outputs.items():
            payload_len = 1 if key == "summary" else len(json.loads(path.read_text(encoding="utf-8")))
            print(f"  {path} ({payload_len:,} records)")
        print(f"  Hottest negative: {summary['hottest_negative']['topic_label']} | P2 {summary['hottest_negative']['p2_index']:.4f}")
        print(f"  CYBERCON: {summary['cybercon_level']}")
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
