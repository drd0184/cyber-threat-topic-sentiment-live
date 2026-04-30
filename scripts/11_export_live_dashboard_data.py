"""
Export live dashboard JSON files from the official live pipeline outputs.

This script reads only existing live pipeline artifacts. It does not retrain
LDA, does not recompute P2, and does not modify the NLP pipeline.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json
import math
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LIVE_PROCESSED_DIR = PROJECT_ROOT / "data" / "live" / "processed"
DASHBOARD_DATA_DIR = PROJECT_ROOT / "dashboard" / "src" / "data"

P2_PATH = LIVE_PROCESSED_DIR / "07_live_p2_index_12h.csv"
AGG_PATH = LIVE_PROCESSED_DIR / "06_live_temporal_aggregation_12h.csv"
SENTIMENT_PATH = LIVE_PROCESSED_DIR / "05_live_sentiment_dataset.csv"
TOPICS_PATH = LIVE_PROCESSED_DIR / "04_live_lda_topics_dataset.csv"
TOPIC_WORDS_PATH = LIVE_PROCESSED_DIR / "04_live_lda_topic_words.csv"

SOCIAL_NEWS_SOURCE_TYPES = {"reddit_rss", "news_rss", "news_api", "social_news_api"}

TOPIC_LABELS = {
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

TOPIC_NOTES = {
    7: "Generic discussion topic. Useful for monitoring broad signals, but interpret alerts with caution.",
}

INPUT_FILES = {
    "p2": "data/live/processed/07_live_p2_index_12h.csv",
    "temporal_aggregation": "data/live/processed/06_live_temporal_aggregation_12h.csv",
    "sentiment": "data/live/processed/05_live_sentiment_dataset.csv",
    "topics": "data/live/processed/04_live_lda_topics_dataset.csv",
    "topic_words": "data/live/processed/04_live_lda_topic_words.csv",
}


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Required input not found: {path}")
    return pd.read_csv(path, low_memory=False)


def as_float(value: object, default: float = 0.0) -> float:
    try:
        if pd.isna(value):
            return default
        value = float(value)
        if math.isnan(value) or math.isinf(value):
            return default
        return value
    except (TypeError, ValueError):
        return default


def as_int(value: object, default: int = 0) -> int:
    try:
        if pd.isna(value):
            return default
        return int(float(value))
    except (TypeError, ValueError):
        return default


def as_string(value: object, default: str = "") -> str:
    if value is None or pd.isna(value):
        return default
    return str(value)


def iso_or_none(value: object) -> str | None:
    if value is None or pd.isna(value):
        return None
    ts = pd.to_datetime(value, errors="coerce", utc=True)
    if pd.isna(ts):
        return None
    return ts.isoformat().replace("+00:00", "Z")


def truncate_text(value: object, max_chars: int = 700) -> str:
    text = as_string(value).replace("\r", " ").replace("\n", " ")
    text = " ".join(text.split())
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1].rstrip() + "…"


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def distribution(df: pd.DataFrame, column: str) -> dict[str, int]:
    if column not in df.columns or df.empty:
        return {}
    counts = df[column].fillna("unknown").astype(str).value_counts()
    return {str(key): int(value) for key, value in counts.items()}


def normalize_topic_columns(df: pd.DataFrame) -> pd.DataFrame:
    output = df.copy()
    if "dominant_topic" in output.columns:
        output["dominant_topic"] = pd.to_numeric(output["dominant_topic"], errors="coerce").astype("Int64")
        output["topic_label"] = output["dominant_topic"].map(lambda topic_id: TOPIC_LABELS.get(int(topic_id), f"Topic {topic_id}") if not pd.isna(topic_id) else "Topic n/a")
    return output


def classify_cybercon(p2_abs: float) -> tuple[int, str]:
    if p2_abs >= 30:
        return 1, "CRITICAL"
    if p2_abs >= 15:
        return 2, "HIGH"
    if p2_abs >= 8:
        return 3, "ELEVATED"
    if p2_abs >= 3:
        return 4, "WATCH"
    return 5, "NOMINAL"


def source_distribution_for_group(group: pd.DataFrame) -> dict[str, int]:
    return {source_type: int(count) for source_type, count in group["source_type"].fillna("unknown").astype(str).value_counts().items()}


def parse_topic_words(topic_words_df: pd.DataFrame) -> dict[int, list[str]]:
    topic_words: dict[int, list[str]] = {}
    for row in topic_words_df.itertuples(index=False):
        topic_id = as_int(getattr(row, "topic_id"))
        words = [word.strip() for word in as_string(getattr(row, "top_words", "")).split(",") if word.strip()]
        topic_words[topic_id] = words
    return topic_words


def build_posts(sentiment_df: pd.DataFrame) -> list[dict[str, object]]:
    posts_df = sentiment_df.copy()
    posts_df["created_at_dt"] = pd.to_datetime(posts_df["created_at"], errors="coerce", utc=True)
    posts_df["time_window_dt"] = posts_df["created_at_dt"].dt.floor("12h")
    posts_df = posts_df.sort_values(["created_at_dt", "id"], ascending=[False, True])

    posts: list[dict[str, object]] = []
    for row in posts_df.itertuples(index=False):
        topic_id = as_int(getattr(row, "dominant_topic", -1), -1)
        posts.append(
            {
                "id": as_string(getattr(row, "id", "")),
                "created_at": iso_or_none(getattr(row, "created_at", None)),
                "collected_at": iso_or_none(getattr(row, "collected_at", None)),
                "source_type": as_string(getattr(row, "source_type", "")),
                "source_name": as_string(getattr(row, "source_name", "")),
                "title": as_string(getattr(row, "title", "")),
                "text_raw": truncate_text(getattr(row, "text_raw", "")),
                "url": as_string(getattr(row, "url", "")),
                "dominant_topic": topic_id,
                "topic_label": TOPIC_LABELS.get(topic_id, f"Topic {topic_id}"),
                "topic_confidence": as_string(getattr(row, "topic_confidence", "none"), "none"),
                "dominant_topic_probability": as_float(getattr(row, "dominant_topic_probability", 0.0)),
                "vader_compound": as_float(getattr(row, "vader_compound", 0.0)),
                "sentiment_class": as_string(getattr(row, "sentiment_class", "neutral"), "neutral"),
                "time_window": iso_or_none(getattr(row, "time_window_dt", None)),
            }
        )
    return posts


def build_p2_rows(p2_df: pd.DataFrame, sentiment_df: pd.DataFrame) -> list[dict[str, object]]:
    p2 = normalize_topic_columns(p2_df)
    p2["time_window_dt"] = pd.to_datetime(p2["time_window"], errors="coerce", utc=True)

    source_counts: dict[tuple[str, int], dict[str, int]] = {}
    if not sentiment_df.empty:
        source_df = sentiment_df.copy()
        source_df["created_at_dt"] = pd.to_datetime(source_df["created_at"], errors="coerce", utc=True)
        source_df["time_window_dt"] = source_df["created_at_dt"].dt.floor("12h")
        for (window, topic_id), group in source_df.groupby(["time_window_dt", "dominant_topic"], dropna=True):
            source_counts[(pd.Timestamp(window).isoformat().replace("+00:00", "Z"), int(topic_id))] = source_distribution_for_group(group)

    rows: list[dict[str, object]] = []
    for row in p2.sort_values(["time_window_dt", "dominant_topic"]).itertuples(index=False):
        topic_id = as_int(getattr(row, "dominant_topic", -1), -1)
        window = iso_or_none(getattr(row, "time_window_dt", None))
        source_dist = source_counts.get((window or "", topic_id), {})
        reddit_count = int(source_dist.get("reddit_rss", as_int(getattr(row, "reddit_count", 0))))
        news_rss_count = int(source_dist.get("news_rss", 0))
        news_api_count = int(source_dist.get("news_api", 0) + source_dist.get("social_news_api", 0))
        news_count = int(news_rss_count + news_api_count or as_int(getattr(row, "news_count", 0)))
        p2_abs = as_float(getattr(row, "p2_abs", 0.0))
        cybercon_level, _ = classify_cybercon(p2_abs)
        rows.append(
            {
                "time_window": window,
                "dominant_topic": topic_id,
                "topic_label": TOPIC_LABELS.get(topic_id, f"Topic {topic_id}"),
                "topic_confidence": as_string(getattr(row, "topic_confidence", "none"), "none"),
                "topic_volume": as_int(getattr(row, "topic_volume", 0)),
                "topic_sentiment_sum": as_float(getattr(row, "topic_sentiment_sum", 0.0)),
                "topic_sentiment_mean": as_float(getattr(row, "topic_sentiment_mean", 0.0)),
                "avg_topic_probability": as_float(getattr(row, "avg_topic_probability", 0.0)),
                "total_window_volume": as_int(getattr(row, "total_window_volume", 0)),
                "topic_volume_share": as_float(getattr(row, "topic_volume_share", 0.0)),
                "volume_factor": as_float(getattr(row, "volume_factor", 0.0)),
                "sentiment_factor": as_float(getattr(row, "sentiment_factor", 0.0)),
                "p2_index": as_float(getattr(row, "p2_index", 0.0)),
                "p2_abs": p2_abs,
                "p2_direction": as_string(getattr(row, "p2_direction", "neutral"), "neutral"),
                "severity": as_string(getattr(row, "severity", "low"), "low"),
                "cybercon_level": cybercon_level,
                "negative_count": as_int(getattr(row, "negative_count", 0)),
                "neutral_count": as_int(getattr(row, "neutral_count", 0)),
                "positive_count": as_int(getattr(row, "positive_count", 0)),
                "reddit_count": reddit_count,
                "news_count": news_count,
                "news_api_count": news_api_count,
                "source_distribution": source_dist,
            }
        )
    return rows


def build_alerts(p2_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    alerts = []
    for index, row in enumerate(sorted(p2_rows, key=lambda item: item["p2_abs"], reverse=True), start=1):
        low_confidence = row["topic_confidence"] == "low"
        alert = {
            "alert_id": f"LIVE-{index:04d}",
            "time_window": row["time_window"],
            "dominant_topic": row["dominant_topic"],
            "topic_label": row["topic_label"],
            "topic_confidence": row["topic_confidence"],
            "p2_index": row["p2_index"],
            "p2_abs": row["p2_abs"],
            "direction": row["p2_direction"],
            "severity": row["severity"],
            "cybercon_level": row["cybercon_level"],
            "topic_volume": row["topic_volume"],
            "topic_sentiment_sum": row["topic_sentiment_sum"],
            "topic_sentiment_mean": row["topic_sentiment_mean"],
            "source_counts": {
                "reddit_rss": row["reddit_count"],
                "news_rss": row["source_distribution"].get("news_rss", 0),
                "news_api": row["news_api_count"],
            },
            "sentiment_counts": {
                "negative": row["negative_count"],
                "neutral": row["neutral_count"],
                "positive": row["positive_count"],
            },
            "warning": "Low-confidence topic. Interpret this alert with caution." if low_confidence else None,
        }
        alerts.append(alert)
    return alerts


def build_topics(
    sentiment_df: pd.DataFrame,
    p2_rows: list[dict[str, object]],
    topic_words: dict[int, list[str]],
) -> list[dict[str, object]]:
    topics: list[dict[str, object]] = []
    p2_by_topic: dict[int, list[dict[str, object]]] = {}
    for row in p2_rows:
        p2_by_topic.setdefault(int(row["dominant_topic"]), []).append(row)

    for topic_id in range(10):
        topic_docs = sentiment_df.loc[sentiment_df["dominant_topic"] == topic_id].copy()
        topic_p2 = p2_by_topic.get(topic_id, [])
        confidence = (
            as_string(topic_docs["topic_confidence"].dropna().mode().iloc[0])
            if not topic_docs.empty and not topic_docs["topic_confidence"].dropna().empty
            else "none"
        )
        words = topic_words.get(topic_id, [])
        max_negative = min((as_float(row["p2_index"]) for row in topic_p2), default=0.0)
        max_positive = max((as_float(row["p2_index"]) for row in topic_p2), default=0.0)
        max_abs = max((as_float(row["p2_abs"]) for row in topic_p2), default=0.0)
        note = TOPIC_NOTES.get(topic_id)
        if not note and confidence == "low":
            note = "Low-confidence topic. Included in P2, but alerts should be interpreted with caution."
        elif not note:
            note = "Included in the live P2 dashboard."
        sorted_topic_p2 = sorted(topic_p2, key=lambda item: item["time_window"] or "")
        topics.append(
            {
                "topic_id": topic_id,
                "topic_label": TOPIC_LABELS[topic_id],
                "topic_confidence": confidence,
                "quality_score": confidence,
                "top_words": words,
                "top_5_words": words[:5],
                "docs_assigned": int(len(topic_docs)),
                "total_docs": int(len(topic_docs)),
                "total_volume": int(sum(as_int(row["topic_volume"]) for row in topic_p2)),
                "max_negative_p2": max_negative,
                "max_positive_p2": max_positive,
                "max_abs_p2": max_abs,
                "avg_sentiment": as_float(topic_docs["vader_compound"].mean()) if not topic_docs.empty else 0.0,
                "sentiment_distribution": distribution(topic_docs, "sentiment_class"),
                "source_type_distribution": distribution(topic_docs, "source_type"),
                "latest_seen": iso_or_none(topic_docs["created_at"].max()) if not topic_docs.empty else None,
                "first_seen": iso_or_none(topic_docs["created_at"].min()) if not topic_docs.empty else None,
                "is_low_confidence": confidence == "low",
                "is_noisy": confidence == "low" or topic_id == 7,
                "note": note,
                "quality_note": note,
                "p2_series": [
                    {
                        "time_window": row["time_window"],
                        "p2_index": row["p2_index"],
                        "p2_abs": row["p2_abs"],
                        "severity": row["severity"],
                        "direction": row["p2_direction"],
                    }
                    for row in sorted_topic_p2
                ],
                "volume_series": [
                    {"time_window": row["time_window"], "topic_volume": row["topic_volume"]}
                    for row in sorted_topic_p2
                ],
                "sentiment_series": [
                    {
                        "time_window": row["time_window"],
                        "topic_sentiment_sum": row["topic_sentiment_sum"],
                        "topic_sentiment_mean": row["topic_sentiment_mean"],
                    }
                    for row in sorted_topic_p2
                ],
            }
        )
    return topics


def build_p2_trend(p2_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    by_window: dict[str, list[dict[str, object]]] = {}
    for row in p2_rows:
        by_window.setdefault(str(row["time_window"]), []).append(row)

    trend = []
    for window, rows in sorted(by_window.items()):
        strongest = max(rows, key=lambda item: as_float(item["p2_abs"]))
        trend.append(
            {
                "time_window": window,
                "max_abs_p2": strongest["p2_abs"],
                "p2_index": strongest["p2_index"],
                "topic_label": strongest["topic_label"],
                "dominant_topic": strongest["dominant_topic"],
                "topic_confidence": strongest["topic_confidence"],
                "severity": strongest["severity"],
                "direction": strongest["p2_direction"],
            }
        )
    return trend


def build_summary(
    sentiment_df: pd.DataFrame,
    p2_rows: list[dict[str, object]],
    alerts: list[dict[str, object]],
    topics: list[dict[str, object]],
    generated_at_utc: str,
) -> dict[str, object]:
    total_topics = len({row["dominant_topic"] for row in p2_rows})
    total_time_windows = len({row["time_window"] for row in p2_rows})
    strongest = alerts[0] if alerts else None
    cybercon_level, cybercon_label = classify_cybercon(as_float(strongest["p2_abs"]) if strongest else 0.0)
    negative_alerts = [alert for alert in alerts if alert["p2_index"] < 0]
    positive_alerts = [alert for alert in alerts if alert["p2_index"] > 0]
    hottest_negative = max(negative_alerts, key=lambda item: item["p2_abs"], default=None)
    hottest_positive = max(positive_alerts, key=lambda item: item["p2_abs"], default=None)
    top_alerts = alerts[:8]
    latest_alerts = sorted(alerts, key=lambda item: item["time_window"] or "", reverse=True)[:10]
    top_topics = sorted(
        [
            {
                "topic_id": topic["topic_id"],
                "topic_label": topic["topic_label"],
                "topic_confidence": topic["topic_confidence"],
                "docs_assigned": topic["docs_assigned"],
                "max_abs_p2": topic["max_abs_p2"],
                "max_negative_p2": topic["max_negative_p2"],
                "max_positive_p2": topic["max_positive_p2"],
                "avg_sentiment": topic["avg_sentiment"],
                "top_words": topic["top_words"][:8],
                "note": topic["note"],
            }
            for topic in topics
        ],
        key=lambda item: (as_float(item["max_abs_p2"]), as_int(item["docs_assigned"])),
        reverse=True,
    )[:6]

    return {
        "total_documents": int(len(sentiment_df)),
        "total_posts": int(len(sentiment_df)),
        "total_topics": int(total_topics),
        "total_time_windows": int(total_time_windows),
        "sentiment_distribution": distribution(sentiment_df, "sentiment_class"),
        "average_vader_compound": as_float(sentiment_df["vader_compound"].mean()) if not sentiment_df.empty else 0.0,
        "average_sentiment": as_float(sentiment_df["vader_compound"].mean()) if not sentiment_df.empty else 0.0,
        "latest_document_created_at": iso_or_none(sentiment_df["created_at"].max()) if not sentiment_df.empty else None,
        "latest_collected_at": iso_or_none(sentiment_df["collected_at"].max()) if "collected_at" in sentiment_df.columns and not sentiment_df.empty else None,
        "generated_at_utc": generated_at_utc,
        "hottest_negative_alert": hottest_negative,
        "hottest_positive_alert": hottest_positive,
        "hottest_negative": hottest_negative,
        "hottest_positive": hottest_positive,
        "max_abs_p2": as_float(strongest["p2_abs"]) if strongest else 0.0,
        "cybercon_level": cybercon_level,
        "cybercon_label": cybercon_label,
        "cybercon_warning": "CYBERCON is currently driven by a low-confidence topic. Interpret with caution." if strongest and strongest["topic_confidence"] == "low" else None,
        "source_type_distribution": distribution(sentiment_df, "source_type"),
        "topic_distribution": {str(int(topic_id)): int(count) for topic_id, count in sentiment_df["dominant_topic"].value_counts().sort_index().items()} if not sentiment_df.empty else {},
        "topic_confidence_distribution": distribution(sentiment_df, "topic_confidence"),
        "severity_distribution": {severity: sum(1 for row in p2_rows if row["severity"] == severity) for severity in ["low", "watch", "elevated", "high", "critical"]},
        "high_quality_topics_count": int((sentiment_df.groupby("dominant_topic")["topic_confidence"].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else "none") == "high").sum()) if not sentiment_df.empty else 0,
        "medium_quality_topics_count": int((sentiment_df.groupby("dominant_topic")["topic_confidence"].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else "none") == "medium").sum()) if not sentiment_df.empty else 0,
        "low_quality_topics_count": int((sentiment_df.groupby("dominant_topic")["topic_confidence"].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else "none") == "low").sum()) if not sentiment_df.empty else 0,
        "p2_trend": build_p2_trend(p2_rows),
        "top_alerts": top_alerts,
        "top_topics": top_topics,
        "latest_alerts": latest_alerts,
    }


def main() -> int:
    try:
        p2_df = read_csv(P2_PATH)
        read_csv(AGG_PATH)
        sentiment_df = normalize_topic_columns(read_csv(SENTIMENT_PATH))
        topics_df = normalize_topic_columns(read_csv(TOPICS_PATH))
        topic_words_df = read_csv(TOPIC_WORDS_PATH)

        sentiment_df = sentiment_df.loc[
            sentiment_df["source_type"].fillna("").astype(str).isin(SOCIAL_NEWS_SOURCE_TYPES)
        ].copy()
        topics_df = topics_df.loc[
            topics_df["source_type"].fillna("").astype(str).isin(SOCIAL_NEWS_SOURCE_TYPES)
        ].copy()

        generated_at = datetime.now(timezone.utc)
        generated_at_utc = generated_at.isoformat().replace("+00:00", "Z")
        generated_at_local = datetime.now().astimezone().isoformat()

        topic_words = parse_topic_words(topic_words_df)
        p2_rows = build_p2_rows(p2_df, sentiment_df)
        alerts = build_alerts(p2_rows)
        topics = build_topics(sentiment_df, p2_rows, topic_words)
        posts = build_posts(sentiment_df)
        summary = build_summary(sentiment_df, p2_rows, alerts, topics, generated_at_utc)

        metadata = {
            "generated_at_utc": generated_at_utc,
            "generated_at_local": generated_at_local,
            "latest_collected_at": summary["latest_collected_at"],
            "latest_document_created_at": summary["latest_document_created_at"],
            "earliest_document_created_at": iso_or_none(sentiment_df["created_at"].min()) if not sentiment_df.empty else None,
            "pipeline_schedule": "00:00 and 12:00 UTC",
            "pipeline_mode": "GitHub Actions scheduled live pipeline",
            "data_scope": "social/news only",
            "excluded_sources_note": "Technical-descriptive sources are not used in the main P2 pipeline.",
            "source_types_included": sorted(distribution(sentiment_df, "source_type").keys()),
            "total_documents": summary["total_documents"],
            "total_topics": summary["total_topics"],
            "total_time_windows": summary["total_time_windows"],
            "input_files": INPUT_FILES,
            "official_model": "models/live_lda_model/",
            "official_topic_model": "LDA live, 10 topics",
        }

        write_json(DASHBOARD_DATA_DIR / "live_summary.json", summary)
        write_json(DASHBOARD_DATA_DIR / "live_p2.json", p2_rows)
        write_json(DASHBOARD_DATA_DIR / "live_topics.json", topics)
        write_json(DASHBOARD_DATA_DIR / "live_posts.json", posts)
        write_json(DASHBOARD_DATA_DIR / "live_alerts.json", alerts)
        write_json(DASHBOARD_DATA_DIR / "live_metadata.json", metadata)

        print("Live dashboard export completed")
        print(f"Documents: {summary['total_documents']}")
        print(f"Topics: {summary['total_topics']}")
        print(f"Time windows: {summary['total_time_windows']}")
        print(f"Output directory: {DASHBOARD_DATA_DIR}")
    except Exception as exc:
        print(f"Live dashboard export error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
