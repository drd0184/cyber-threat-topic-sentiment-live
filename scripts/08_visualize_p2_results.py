"""
Visualize P2 topic dynamics and export hot-topic tables.

Inputs:
- data/processed/07_p2_index_12h.csv
- data/processed/04_lda_topic_words.csv

Outputs are written under reports/figures/ and reports/tables/.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
TABLES_DIR = REPORTS_DIR / "tables"
MATPLOTLIB_CACHE_DIR = REPORTS_DIR / "matplotlib_cache"

MATPLOTLIB_CACHE_DIR.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MATPLOTLIB_CACHE_DIR))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

DEFAULT_P2_INPUT_PATH = PROCESSED_DIR / "07_p2_index_12h.csv"
DEFAULT_TOPIC_WORDS_PATH = PROCESSED_DIR / "04_lda_topic_words.csv"
P2_TIMESERIES_PATH = FIGURES_DIR / "p2_timeseries_by_topic.png"
TOP_NEGATIVE_PATH = FIGURES_DIR / "top_negative_hot_topics.png"
VOLUME_TIMESERIES_PATH = FIGURES_DIR / "topic_volume_timeseries.png"
TOP_HOT_TOPICS_PATH = TABLES_DIR / "top_p2_hot_topics.csv"

REQUIRED_P2_COLUMNS = {
    "time_window",
    "dominant_topic",
    "topic_volume",
    "topic_sentiment_sum",
    "topic_sentiment_mean",
    "volume_factor",
    "sentiment_factor",
    "p2_index",
    "p2_abs",
    "p2_direction",
}
HOT_TOPIC_COLUMNS = [
    "time_window",
    "dominant_topic",
    "topic_volume",
    "topic_sentiment_sum",
    "topic_sentiment_mean",
    "volume_factor",
    "sentiment_factor",
    "p2_index",
    "p2_abs",
    "p2_direction",
]
ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Visualize P2 time series and export hot-topic tables."
    )
    parser.add_argument(
        "--p2-input",
        type=Path,
        default=DEFAULT_P2_INPUT_PATH,
        help="Path to the P2 index CSV.",
    )
    parser.add_argument(
        "--topic-words",
        type=Path,
        default=DEFAULT_TOPIC_WORDS_PATH,
        help="Path to the topic words CSV.",
    )
    return parser.parse_args()


def resolve_project_path(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


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


def validate_input_path(input_path: Path, required: bool = True) -> bool:
    if not input_path.exists():
        if required:
            raise FileNotFoundError(f"Input CSV not found: {input_path}")
        print(f"Warning: optional topic words file not found: {input_path}")
        return False
    if not input_path.is_file():
        raise FileNotFoundError(f"Input path is not a file: {input_path}")
    if input_path.suffix.lower() != ".csv":
        raise ValueError(f"Input file must be a CSV: {input_path}")
    return True


def validate_p2_columns(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("P2 input CSV is empty.")

    missing_columns = sorted(REQUIRED_P2_COLUMNS.difference(df.columns))
    if missing_columns:
        available = ", ".join(df.columns)
        missing = ", ".join(missing_columns)
        raise ValueError(
            f"Missing required column(s): {missing}\nAvailable columns: {available}"
        )


def prepare_p2_data(df: pd.DataFrame) -> pd.DataFrame:
    validate_p2_columns(df)

    prepared = df.copy()
    prepared["time_window"] = pd.to_datetime(
        prepared["time_window"], errors="coerce", utc=True
    )
    prepared["dominant_topic"] = pd.to_numeric(
        prepared["dominant_topic"], errors="coerce"
    )
    for column in [
        "topic_volume",
        "topic_sentiment_sum",
        "topic_sentiment_mean",
        "volume_factor",
        "sentiment_factor",
        "p2_index",
        "p2_abs",
    ]:
        prepared[column] = pd.to_numeric(prepared[column], errors="coerce")

    invalid_rows = prepared[
        ["time_window", "dominant_topic", "topic_volume", "p2_index", "p2_abs"]
    ].isna().any(axis=1)
    if invalid_rows.any():
        print(f"Warning: dropping {int(invalid_rows.sum())} invalid P2 row(s).")
    prepared = prepared.loc[~invalid_rows].copy()

    if prepared.empty:
        raise ValueError("No valid rows left after parsing P2 input.")

    prepared["dominant_topic"] = prepared["dominant_topic"].astype(int)
    return prepared.sort_values(["time_window", "dominant_topic"]).reset_index(drop=True)


def load_topic_labels(topic_words_path: Path) -> dict[int, str]:
    if not validate_input_path(topic_words_path, required=False):
        return {}

    topic_words_df, _ = read_csv_with_encoding_fallback(topic_words_path)
    if {"topic_id", "top_words"}.difference(topic_words_df.columns):
        print("Warning: topic words file does not contain topic_id and top_words.")
        return {}

    labels = {}
    for row in topic_words_df.itertuples(index=False):
        words = str(row.top_words).split(", ")
        short_words = ", ".join(words[:3])
        labels[int(row.topic_id)] = f"Topic {int(row.topic_id)}: {short_words}"
    return labels


def topic_label(topic_id: int, topic_labels: dict[int, str]) -> str:
    return topic_labels.get(topic_id, f"Topic {topic_id}")


def create_output_dirs() -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    TABLES_DIR.mkdir(parents=True, exist_ok=True)


def plot_p2_timeseries(df: pd.DataFrame, topic_labels: dict[int, str]) -> None:
    fig, ax = plt.subplots(figsize=(14, 7))
    for topic_id, topic_df in df.groupby("dominant_topic"):
        ax.plot(
            topic_df["time_window"],
            topic_df["p2_index"],
            marker="o",
            linewidth=1.4,
            markersize=3,
            label=topic_label(topic_id, topic_labels),
        )

    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title("P2 Index Over Time by Dominant Topic")
    ax.set_xlabel("Time window")
    ax.set_ylabel("P2 index")
    ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1), fontsize=8)
    fig.autofmt_xdate(rotation=45)
    fig.tight_layout()
    fig.savefig(P2_TIMESERIES_PATH, dpi=200)
    plt.close(fig)


def plot_top_negative_hot_topics(df: pd.DataFrame, topic_labels: dict[int, str]) -> None:
    top_negative = df.sort_values("p2_index", ascending=True).head(10).copy()
    top_negative["label"] = top_negative.apply(
        lambda row: f"{row.time_window:%Y-%m-%d %H:%M} | {topic_label(int(row.dominant_topic), topic_labels)}",
        axis=1,
    )

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.barh(top_negative["label"], top_negative["p2_index"], color="#b23a48")
    ax.invert_yaxis()
    ax.set_title("Top 10 Negative P2 Hot Topics")
    ax.set_xlabel("P2 index")
    ax.set_ylabel("Time window and topic")
    fig.tight_layout()
    fig.savefig(TOP_NEGATIVE_PATH, dpi=200)
    plt.close(fig)


def plot_topic_volume_timeseries(df: pd.DataFrame, topic_labels: dict[int, str]) -> None:
    fig, ax = plt.subplots(figsize=(14, 7))
    for topic_id, topic_df in df.groupby("dominant_topic"):
        ax.plot(
            topic_df["time_window"],
            topic_df["topic_volume"],
            marker="o",
            linewidth=1.4,
            markersize=3,
            label=topic_label(topic_id, topic_labels),
        )

    ax.set_title("Topic Volume Over Time by Dominant Topic")
    ax.set_xlabel("Time window")
    ax.set_ylabel("Topic volume")
    ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1), fontsize=8)
    fig.autofmt_xdate(rotation=45)
    fig.tight_layout()
    fig.savefig(VOLUME_TIMESERIES_PATH, dpi=200)
    plt.close(fig)


def save_hot_topics_table(df: pd.DataFrame) -> pd.DataFrame:
    hot_topics = df.sort_values("p2_abs", ascending=False)[HOT_TOPIC_COLUMNS].copy()
    hot_topics.to_csv(TOP_HOT_TOPICS_PATH, index=False)
    return hot_topics


def print_hot_topics(df: pd.DataFrame, title: str) -> None:
    print(f"\n{title}")
    print("-" * len(title))
    print(df[HOT_TOPIC_COLUMNS].to_string(index=False))


def print_final_report(df: pd.DataFrame) -> None:
    print_hot_topics(
        df.sort_values("p2_index", ascending=True).head(10),
        "Top 10 negative P2 hot topics",
    )
    print_hot_topics(
        df.sort_values("p2_index", ascending=False).head(10),
        "Top 10 positive P2 hot topics",
    )
    print_hot_topics(
        df.sort_values("p2_abs", ascending=False).head(10),
        "Top 10 absolute P2 hot topics",
    )


def main() -> int:
    args = parse_args()

    try:
        p2_input_path = resolve_project_path(args.p2_input)
        topic_words_path = resolve_project_path(args.topic_words)

        validate_input_path(p2_input_path, required=True)
        create_output_dirs()

        print(f"Loading P2 CSV: {p2_input_path}")
        p2_df, encoding_used = read_csv_with_encoding_fallback(p2_input_path)
        print(f"Encoding used: {encoding_used}")
        print(f"Input rows: {len(p2_df)}")

        p2_df = prepare_p2_data(p2_df)
        topic_labels = load_topic_labels(topic_words_path)

        plot_p2_timeseries(p2_df, topic_labels)
        plot_top_negative_hot_topics(p2_df, topic_labels)
        plot_topic_volume_timeseries(p2_df, topic_labels)
        save_hot_topics_table(p2_df)

        print(f"Saved figure: {P2_TIMESERIES_PATH}")
        print(f"Saved figure: {TOP_NEGATIVE_PATH}")
        print(f"Saved figure: {VOLUME_TIMESERIES_PATH}")
        print(f"Saved table: {TOP_HOT_TOPICS_PATH}")
        print_final_report(p2_df)

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
    except ValueError as exc:
        print(f"Data validation error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
