"""
Generate a standalone OSINT-style dashboard for the Cyber Threat Hot Topic Index.

The dashboard reads existing pipeline outputs only. It does not rerun NLP steps
and does not use original_type, annotation, or relevant for calculations.
"""

from __future__ import annotations

import argparse
import html
import os
import sys
from pathlib import Path
from typing import Iterable

import pandas as pd

try:
    import plotly.graph_objects as go
    from plotly.offline import get_plotlyjs, plot
except ImportError as exc:
    go = None
    get_plotlyjs = None
    plot = None
    PLOTLY_IMPORT_ERROR = exc
else:
    PLOTLY_IMPORT_ERROR = None


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"

DEFAULT_P2_INPUT_PATH = PROCESSED_DIR / "07_p2_index_12h.csv"
DEFAULT_TOPIC_WORDS_PATH = PROCESSED_DIR / "04_lda_topic_words.csv"
DEFAULT_SENTIMENT_INPUT_PATH = PROCESSED_DIR / "05_sentiment_dataset.csv"
DEFAULT_OUTPUT_PATH = REPORTS_DIR / "dashboard.html"

ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")

REQUIRED_P2_COLUMNS = {
    "time_window",
    "dominant_topic",
    "topic_volume",
    "topic_sentiment_sum",
    "p2_index",
    "p2_abs",
    "p2_direction",
}

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

NOISY_TOPICS = {0, 7}

TOPIC_COLORS = {
    0: "#67e8f9",
    1: "#60a5fa",
    2: "#22d3ee",
    3: "#a78bfa",
    4: "#f87171",
    5: "#fbbf24",
    6: "#fb7185",
    7: "#94a3b8",
    8: "#34d399",
    9: "#2dd4bf",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a standalone Cyber Threat Hot Topic Index dashboard."
    )
    parser.add_argument("--p2-input", type=Path, default=DEFAULT_P2_INPUT_PATH)
    parser.add_argument("--topic-words", type=Path, default=DEFAULT_TOPIC_WORDS_PATH)
    parser.add_argument("--sentiment-input", type=Path, default=DEFAULT_SENTIMENT_INPUT_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    return parser.parse_args()


def resolve_project_path(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


def ensure_plotly_available() -> None:
    if PLOTLY_IMPORT_ERROR is not None:
        raise RuntimeError(
            "Plotly is required to generate the dashboard. Install it with "
            "'pip install plotly' and rerun this script."
        ) from PLOTLY_IMPORT_ERROR


def validate_input_path(path: Path, required: bool = True) -> bool:
    if path.exists() and path.is_file():
        return True
    if required:
        raise FileNotFoundError(f"Required input file not found: {path}")
    print(f"Warning: optional input file not found: {path}")
    return False


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


def escape(value: object) -> str:
    return html.escape("" if pd.isna(value) else str(value), quote=True)


def fmt_int(value: object) -> str:
    if pd.isna(value):
        return "n/a"
    return f"{int(round(float(value))):,}"


def fmt_float(value: object, digits: int = 2) -> str:
    if pd.isna(value):
        return "n/a"
    return f"{float(value):,.{digits}f}"


def fmt_signed(value: object, digits: int = 2) -> str:
    if pd.isna(value):
        return "n/a"
    return f"{float(value):+,.{digits}f}"


def fmt_timestamp(value: object) -> str:
    if pd.isna(value):
        return "n/a"
    return pd.Timestamp(value).strftime("%Y-%m-%d %H:%M UTC")


def split_words(top_words: object, limit: int | None = None) -> list[str]:
    words = [word.strip() for word in str(top_words).split(",") if word.strip()]
    return words if limit is None else words[:limit]


def topic_label(topic_id: int) -> str:
    return TOPIC_LABELS.get(topic_id, f"Topic {topic_id}")


def compact_label(topic_id: int) -> str:
    return f"T{topic_id} - {topic_label(topic_id)}"


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


def cybercon_class(level: int) -> str:
    return f"cybercon-{level}"


def direction_class(value: float) -> str:
    if value < 0:
        return "negative"
    if value > 0:
        return "positive"
    return "neutral"


def narrative_for(row: pd.Series) -> str:
    label = str(row["topic_label"]).lower()
    direction = str(row.get("p2_direction", "")).lower()
    if direction == "negative":
        if "ransomware" in label or "malware" in label:
            return "High negative momentum detected in ransomware/malware-related discussions."
        if "cve" in label or "exploit" in label or "zero-day" in label:
            return "Negative momentum is concentrated around vulnerability and exploit-related discussion."
        if "ddos" in label:
            return "Elevated negative signal detected around DDoS and attack-protection narratives."
        if "data leak" in label or "botnet" in label:
            return "Negative pressure is visible in data leak, botnet, and cloud-risk discussion."
        return "Negative cyber-risk momentum is elevated for this topic cluster."
    return "Positive or stabilizing momentum is currently stronger than negative signal for this topic."


def load_topic_words(path: Path) -> pd.DataFrame:
    if not validate_input_path(path, required=False):
        return pd.DataFrame(columns=["topic_id", "top_words"])

    df = read_csv_with_encoding_fallback(path)
    if not {"topic_id", "top_words"}.issubset(df.columns):
        print(f"Warning: topic words file has unexpected columns: {path}")
        return pd.DataFrame(columns=["topic_id", "top_words"])

    df = df[["topic_id", "top_words"]].copy()
    df["topic_id"] = pd.to_numeric(df["topic_id"], errors="coerce")
    df = df.dropna(subset=["topic_id"])
    df["topic_id"] = df["topic_id"].astype(int)
    df["top_words"] = df["top_words"].fillna("")
    return df.sort_values("topic_id").reset_index(drop=True)


def load_sentiment_stats(path: Path) -> dict[str, str]:
    if not validate_input_path(path, required=False):
        return {}

    df = read_csv_with_encoding_fallback(path)
    if "vader_compound" not in df.columns:
        print("Warning: optional sentiment CSV has no vader_compound column.")
        return {}

    compound = pd.to_numeric(df["vader_compound"], errors="coerce")
    return {"Average sentiment": fmt_signed(compound.mean(), 4)}


def prepare_p2_data(p2_df: pd.DataFrame, topic_words_df: pd.DataFrame) -> pd.DataFrame:
    if p2_df.empty:
        raise ValueError("P2 input CSV is empty.")

    missing = sorted(REQUIRED_P2_COLUMNS.difference(p2_df.columns))
    if missing:
        raise ValueError(f"Missing required P2 column(s): {', '.join(missing)}")

    df = p2_df.copy()
    df["time_window"] = pd.to_datetime(df["time_window"], errors="coerce", utc=True)
    df["dominant_topic"] = pd.to_numeric(df["dominant_topic"], errors="coerce")

    numeric_columns = [
        "topic_volume",
        "topic_sentiment_sum",
        "topic_sentiment_mean",
        "avg_topic_probability",
        "total_window_volume",
        "topic_volume_share",
        "volume_factor",
        "sentiment_factor",
        "p2_index",
        "p2_abs",
    ]
    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    invalid = df[["time_window", "dominant_topic", "p2_index", "p2_abs"]].isna().any(axis=1)
    if invalid.any():
        print(f"Warning: dropping {int(invalid.sum())} invalid P2 row(s).")
    df = df.loc[~invalid].copy()
    if df.empty:
        raise ValueError("No valid rows left after parsing P2 input.")

    df["dominant_topic"] = df["dominant_topic"].astype(int)
    if topic_words_df.empty:
        df["top_words"] = ""
    else:
        df = df.merge(
            topic_words_df,
            left_on="dominant_topic",
            right_on="topic_id",
            how="left",
        ).drop(columns=["topic_id"])
        df["top_words"] = df["top_words"].fillna("")

    df["topic_label"] = df["dominant_topic"].map(topic_label)
    df["topic_display"] = df["dominant_topic"].map(compact_label)
    df["p2_direction"] = df["p2_direction"].fillna("").astype(str)
    return df.sort_values(["time_window", "dominant_topic"]).reset_index(drop=True)


def build_topic_catalog(topic_words_df: pd.DataFrame, p2_df: pd.DataFrame) -> pd.DataFrame:
    if topic_words_df.empty:
        topic_ids = sorted(p2_df["dominant_topic"].dropna().astype(int).unique())
        catalog = pd.DataFrame({"topic_id": topic_ids, "top_words": [""] * len(topic_ids)})
    else:
        catalog = topic_words_df.copy()

    catalog["topic_label"] = catalog["topic_id"].map(topic_label)
    catalog["top_5_words"] = catalog["top_words"].map(lambda value: split_words(value, limit=5))
    catalog["is_noisy"] = catalog["topic_id"].isin(NOISY_TOPICS)
    return catalog.sort_values("topic_id").reset_index(drop=True)


def plot_div(fig: go.Figure) -> str:
    return plot(
        fig,
        include_plotlyjs=False,
        output_type="div",
        config={"displayModeBar": False, "responsive": True},
    )


def apply_dark_layout(fig: go.Figure, height: int = 360) -> go.Figure:
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"family": "Inter, ui-sans-serif, system-ui, Segoe UI, Arial, sans-serif", "color": "#dbeafe"},
        height=height,
        margin={"l": 36, "r": 18, "t": 18, "b": 36},
        hoverlabel={"bgcolor": "#08111f", "bordercolor": "#334155", "font_size": 12},
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "left",
            "x": 0,
            "font": {"size": 10},
        },
    )
    fig.update_xaxes(gridcolor="rgba(148,163,184,0.14)", zerolinecolor="rgba(148,163,184,0.25)")
    fig.update_yaxes(gridcolor="rgba(148,163,184,0.14)", zerolinecolor="rgba(148,163,184,0.25)")
    return fig


def top_default_topics(p2_df: pd.DataFrame, limit: int = 5) -> set[int]:
    top_rows = p2_df.sort_values("p2_abs", ascending=False).drop_duplicates("dominant_topic")
    return set(top_rows.head(limit)["dominant_topic"].astype(int))


def create_negative_alerts_chart(p2_df: pd.DataFrame) -> str:
    chart_df = p2_df.sort_values("p2_index", ascending=True).head(10).copy()
    chart_df = chart_df.sort_values("p2_index", ascending=True)
    chart_df["item_label"] = chart_df.apply(
        lambda row: f"{row.time_window:%m-%d %H:%M}  T{int(row.dominant_topic)}",
        axis=1,
    )

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=chart_df["p2_index"],
            y=chart_df["item_label"],
            orientation="h",
            marker={"color": "#ef4444", "line": {"color": "#fecaca", "width": 0.4}},
            customdata=chart_df[
                ["time_window", "topic_label", "top_words", "topic_volume", "topic_sentiment_sum", "p2_index"]
            ],
            hovertemplate=(
                "Window: %{customdata[0]|%Y-%m-%d %H:%M UTC}<br>"
                "Topic: %{customdata[1]}<br>"
                "Top words: %{customdata[2]}<br>"
                "Volume: %{customdata[3]}<br>"
                "Sentiment sum: %{customdata[4]:.3f}<br>"
                "P2: %{customdata[5]:.3f}<extra></extra>"
            ),
        )
    )
    fig.update_layout(xaxis_title="P2 index", yaxis_title="")
    fig.update_yaxes(autorange="reversed")
    return plot_div(apply_dark_layout(fig, height=360))


def create_topic_line_chart(
    p2_df: pd.DataFrame,
    y_column: str,
    y_title: str,
    default_topics: set[int],
    height: int = 390,
) -> str:
    fig = go.Figure()
    for topic_id, topic_df in p2_df.groupby("dominant_topic", sort=True):
        topic_id = int(topic_id)
        visible = True if topic_id in default_topics else "legendonly"
        color = TOPIC_COLORS.get(topic_id, "#e2e8f0")
        fig.add_trace(
            go.Scatter(
                x=topic_df["time_window"],
                y=topic_df[y_column],
                mode="lines+markers",
                name=compact_label(topic_id),
                visible=visible,
                line={"width": 2, "color": color},
                marker={"size": 5, "color": color},
                customdata=topic_df[
                    ["topic_label", "top_words", "p2_index", "topic_volume", "topic_sentiment_sum"]
                ],
                hovertemplate=(
                    "Window: %{x|%Y-%m-%d %H:%M UTC}<br>"
                    "Topic: %{customdata[0]}<br>"
                    "Top words: %{customdata[1]}<br>"
                    "P2: %{customdata[2]:.3f}<br>"
                    "Volume: %{customdata[3]}<br>"
                    "Sentiment sum: %{customdata[4]:.3f}<br>"
                    f"{escape(y_title)}: %{{y:.3f}}<extra></extra>"
                ),
            )
        )

    fig.update_layout(xaxis_title="", yaxis_title=y_title)
    return plot_div(apply_dark_layout(fig, height=height))


def metric_card(title: str, value: str, tone: str = "neutral") -> str:
    return f"""
      <article class="metric-card tone-{tone}">
        <span>{escape(title)}</span>
        <strong>{escape(value)}</strong>
      </article>
    """


def badge(text: str, tone: str = "neutral") -> str:
    return f'<span class="badge badge-{tone}">{escape(text)}</span>'


def topic_cards(catalog: pd.DataFrame) -> str:
    cards = []
    for row in catalog.itertuples(index=False):
        chips = "".join(f"<span>{escape(word)}</span>" for word in row.top_5_words)
        noisy = badge("NOISY SIGNAL", "muted") if row.is_noisy else ""
        cards.append(
            f"""
            <article class="topic-card">
              <div class="topic-card-head">
                <span class="topic-id">TOPIC {int(row.topic_id)}</span>
                {noisy}
              </div>
              <h3>{escape(row.topic_label)}</h3>
              <div class="word-chips">{chips}</div>
            </article>
            """
        )
    return "\n".join(cards)


def hot_topic_feed(p2_df: pd.DataFrame) -> str:
    items = []
    feed_df = p2_df.sort_values("p2_abs", ascending=False).head(10)
    for row in feed_df.itertuples(index=False):
        direction = "negative" if row.p2_index < 0 else "positive" if row.p2_index > 0 else "neutral"
        words = ", ".join(split_words(row.top_words, limit=5))
        items.append(
            f"""
            <article class="feed-item feed-{direction}">
              <div class="feed-time">{fmt_timestamp(row.time_window)}</div>
              <div class="feed-main">
                <h3>{escape(row.topic_label)}</h3>
                <p>{escape(words)}</p>
              </div>
              <div class="feed-stats">
                <span class="{direction}">P2 {fmt_signed(row.p2_index, 2)}</span>
                <span>{escape(str(row.p2_direction).upper())}</span>
                <span>VOL {fmt_int(row.topic_volume)}</span>
                <span>SENT {fmt_signed(row.topic_sentiment_sum, 2)}</span>
              </div>
            </article>
            """
        )
    return "\n".join(items)


def relative_link(target: Path, label: str, output_path: Path) -> str:
    if not target.exists():
        return f'<span class="missing-link">{escape(label)} - missing</span>'
    relative = os.path.relpath(target.resolve(), start=output_path.parent.resolve())
    relative = Path(relative).as_posix()
    return f'<a href="{escape(relative)}">{escape(label)}</a>'


def make_link_list(output_path: Path) -> str:
    links = [
        relative_link(PROCESSED_DIR / "07_p2_index_12h.csv", "P2 index CSV", output_path),
        relative_link(PROCESSED_DIR / "04_lda_topic_words.csv", "LDA topic words CSV", output_path),
        relative_link(PROJECT_ROOT / "PROJECT_STATUS.md", "Project status", output_path),
    ]
    return "\n".join(f"<li>{link}</li>" for link in links)


def build_dashboard_html(
    p2_df: pd.DataFrame,
    topic_catalog: pd.DataFrame,
    sentiment_stats: dict[str, str],
    output_path: Path,
) -> str:
    default_topics = top_default_topics(p2_df)
    top_negative = p2_df.sort_values("p2_index", ascending=True).iloc[0]
    top_positive = p2_df.sort_values("p2_index", ascending=False).iloc[0]
    num_topics = p2_df["dominant_topic"].nunique()
    num_windows = p2_df["time_window"].nunique()
    level = cybercon_level(float(top_negative["p2_abs"]))

    reports_analyzed = int(p2_df["topic_volume"].sum())
    metric_cards = [
        metric_card("Reports analyzed", fmt_int(reports_analyzed)),
        metric_card("Time windows", fmt_int(num_windows)),
        metric_card("Topics monitored", fmt_int(num_topics)),
        metric_card("Most negative P2", fmt_signed(top_negative["p2_index"], 2), "negative"),
        metric_card("Most positive P2", fmt_signed(top_positive["p2_index"], 2), "positive"),
    ]
    if "Average sentiment" in sentiment_stats:
        avg_sentiment = sentiment_stats["Average sentiment"]
        tone = "negative" if avg_sentiment.startswith("-") else "positive"
        metric_cards.append(metric_card("Average sentiment", avg_sentiment, tone))

    css = """
    :root {
      --bg: #050912;
      --panel: #0b1220;
      --panel-soft: #0f172a;
      --panel-strong: #111827;
      --border: rgba(148, 163, 184, 0.22);
      --border-strong: rgba(148, 163, 184, 0.36);
      --text: #e5edf6;
      --muted: #94a3b8;
      --faint: #64748b;
      --cyan: #22d3ee;
      --blue: #60a5fa;
      --red: #ef4444;
      --green: #34d399;
      --amber: #fbbf24;
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      color: var(--text);
      background: var(--bg);
      font-family: Inter, ui-sans-serif, system-ui, "Segoe UI", Arial, sans-serif;
      line-height: 1.5;
    }
    body::before {
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      background:
        linear-gradient(rgba(34, 211, 238, 0.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(34, 211, 238, 0.03) 1px, transparent 1px);
      background-size: 42px 42px;
      mask-image: linear-gradient(to bottom, black 0%, transparent 85%);
    }
    a { color: var(--cyan); text-decoration: none; }
    a:hover { text-decoration: underline; }
    .shell { max-width: 1180px; margin: 0 auto; padding: 28px 22px 54px; }
    .hero {
      min-height: 360px;
      display: grid;
      align-content: end;
      border-bottom: 1px solid var(--border);
      padding: 30px 0 36px;
    }
    .eyebrow {
      color: var(--cyan);
      font: 700 12px/1.2 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }
    h1 {
      margin: 14px 0 8px;
      max-width: 820px;
      font-size: clamp(42px, 8vw, 86px);
      line-height: 0.94;
      letter-spacing: 0;
    }
    .subtitle { margin: 0; color: #cbd5e1; font-size: 20px; }
    .hero-badges, .nav-links, .status-grid, .metrics-grid, .topic-grid, .chart-pair {
      display: grid;
      gap: 12px;
    }
    .hero-badges {
      grid-template-columns: repeat(3, max-content);
      margin-top: 28px;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      min-height: 28px;
      border: 1px solid var(--border-strong);
      padding: 5px 9px;
      color: #dbeafe;
      background: rgba(15, 23, 42, 0.72);
      border-radius: 4px;
      font: 700 11px/1 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      white-space: nowrap;
    }
    .badge-negative { border-color: rgba(239, 68, 68, 0.55); color: #fecaca; }
    .badge-positive { border-color: rgba(52, 211, 153, 0.55); color: #bbf7d0; }
    .badge-muted { color: #cbd5e1; }
    .nav {
      position: sticky;
      top: 0;
      z-index: 20;
      margin: 0 -22px 24px;
      padding: 10px 22px;
      background: rgba(5, 9, 18, 0.9);
      border-bottom: 1px solid var(--border);
      backdrop-filter: blur(14px);
    }
    .nav-links {
      max-width: 1180px;
      margin: 0 auto;
      grid-template-columns: repeat(7, max-content);
      overflow-x: auto;
    }
    .nav a {
      color: #cbd5e1;
      font: 700 12px/1 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 8px 0;
      white-space: nowrap;
    }
    section {
      scroll-margin-top: 72px;
      margin-bottom: 24px;
      padding: 22px;
      border: 1px solid var(--border);
      background: rgba(11, 18, 32, 0.88);
      border-radius: 8px;
    }
    section h2 {
      margin: 0 0 6px;
      font-size: 18px;
      letter-spacing: 0;
      text-transform: uppercase;
    }
    .section-note { margin: 0 0 16px; color: var(--muted); max-width: 840px; }
    .status-grid { grid-template-columns: 280px 1fr; align-items: stretch; }
    .cybercon {
      display: grid;
      align-content: center;
      justify-items: center;
      min-height: 230px;
      border: 1px solid var(--border-strong);
      border-radius: 8px;
      background: var(--panel-strong);
    }
    .cybercon span {
      color: var(--muted);
      font: 700 12px/1 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }
    .cybercon strong {
      margin-top: 10px;
      font-size: 84px;
      line-height: 1;
    }
    .cybercon-1 strong, .cybercon-2 strong { color: var(--red); }
    .cybercon-3 strong { color: var(--amber); }
    .cybercon-4 strong { color: var(--cyan); }
    .cybercon-5 strong { color: var(--green); }
    .status-card {
      border: 1px solid var(--border-strong);
      border-radius: 8px;
      padding: 22px;
      background: var(--panel-soft);
    }
    .status-card h2 { font-size: 26px; text-transform: none; margin-bottom: 10px; }
    .status-narrative { color: #dbeafe; font-size: 17px; margin: 0 0 20px; }
    .status-kpis {
      display: grid;
      grid-template-columns: repeat(4, minmax(110px, 1fr));
      gap: 10px;
    }
    .status-kpis div, .metric-card {
      border: 1px solid var(--border);
      background: rgba(15, 23, 42, 0.72);
      border-radius: 8px;
      padding: 12px;
    }
    .status-kpis span, .metric-card span {
      display: block;
      color: var(--muted);
      font: 700 11px/1.2 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }
    .status-kpis strong, .metric-card strong {
      display: block;
      margin-top: 8px;
      font-size: 23px;
      line-height: 1.1;
    }
    .metrics-grid { grid-template-columns: repeat(6, 1fr); }
    .tone-negative strong, .negative { color: #fca5a5; }
    .tone-positive strong, .positive { color: #86efac; }
    .neutral { color: #bfdbfe; }
    .topic-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .topic-card {
      border: 1px solid var(--border);
      border-radius: 8px;
      background: rgba(15, 23, 42, 0.72);
      padding: 14px;
    }
    .topic-card-head {
      display: flex;
      justify-content: space-between;
      gap: 10px;
      align-items: center;
      min-height: 28px;
    }
    .topic-id {
      color: var(--cyan);
      font: 800 12px/1 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      letter-spacing: 0.08em;
    }
    .topic-card h3 { margin: 12px 0; font-size: 17px; }
    .word-chips { display: flex; flex-wrap: wrap; gap: 7px; }
    .word-chips span {
      border: 1px solid rgba(96, 165, 250, 0.28);
      border-radius: 4px;
      color: #bfdbfe;
      padding: 4px 7px;
      font-size: 12px;
      background: rgba(30, 41, 59, 0.72);
    }
    .feed-list { display: grid; gap: 10px; }
    .feed-item {
      display: grid;
      grid-template-columns: 155px 1fr 310px;
      gap: 14px;
      align-items: center;
      border: 1px solid var(--border);
      border-left-width: 3px;
      border-radius: 8px;
      background: rgba(15, 23, 42, 0.72);
      padding: 12px;
    }
    .feed-negative { border-left-color: var(--red); }
    .feed-positive { border-left-color: var(--green); }
    .feed-neutral { border-left-color: var(--blue); }
    .feed-time {
      color: var(--muted);
      font: 700 12px/1.35 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    }
    .feed-main h3 { margin: 0 0 4px; font-size: 15px; }
    .feed-main p { margin: 0; color: var(--muted); font-size: 13px; }
    .feed-stats {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 6px;
      font: 700 12px/1 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      color: #dbeafe;
    }
    .feed-stats span {
      border: 1px solid rgba(148, 163, 184, 0.18);
      border-radius: 4px;
      padding: 7px;
      background: rgba(2, 6, 23, 0.38);
    }
    .chart-card {
      min-height: 390px;
      border: 1px solid var(--border);
      border-radius: 8px;
      background: rgba(15, 23, 42, 0.52);
      padding: 8px;
    }
    .chart-pair { grid-template-columns: 1fr 1fr; }
    .method-list { margin: 0; padding-left: 18px; color: #cbd5e1; }
    .method-list li { margin: 7px 0; }
    .download-list { display: flex; flex-wrap: wrap; gap: 10px; padding: 0; margin: 0; list-style: none; }
    .download-list a, .missing-link {
      display: inline-flex;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 10px 12px;
      background: rgba(15, 23, 42, 0.72);
      font-weight: 700;
    }
    .missing-link { color: var(--faint); }
    code {
      color: #bae6fd;
      background: rgba(2, 6, 23, 0.42);
      border: 1px solid rgba(148, 163, 184, 0.18);
      border-radius: 4px;
      padding: 1px 4px;
    }
    @media (max-width: 980px) {
      .status-grid, .chart-pair, .topic-grid { grid-template-columns: 1fr; }
      .metrics-grid { grid-template-columns: repeat(2, 1fr); }
      .feed-item { grid-template-columns: 1fr; }
      .feed-stats { grid-template-columns: repeat(2, minmax(0, 1fr)); }
      .hero-badges { grid-template-columns: 1fr; justify-items: start; }
      .nav-links { grid-template-columns: repeat(7, max-content); }
    }
    @media (max-width: 620px) {
      .shell { padding-left: 14px; padding-right: 14px; }
      section { padding: 16px; }
      .metrics-grid, .status-kpis { grid-template-columns: 1fr; }
      .cybercon strong { font-size: 64px; }
    }
    """

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Cyber Threat Hot Topic Index</title>
  <script>{get_plotlyjs()}</script>
  <style>{css}</style>
</head>
<body>
  <div class="shell">
    <header class="hero">
      <div class="eyebrow">Cyber Threat Hot Topic Index</div>
      <h1>CYBER THREAT HOT TOPIC INDEX</h1>
      <p class="subtitle">Semantic Intelligence for Cybersecurity</p>
      <div class="hero-badges">
        {badge("STATUS: STATIC ANALYSIS")}
        {badge("WINDOW: 12H")}
        {badge("SOURCE: CYBER SOCIAL DATASET")}
      </div>
    </header>

    <nav class="nav" aria-label="Dashboard sections">
      <div class="nav-links">
        <a href="#status">Status</a>
        <a href="#metrics">Metrics</a>
        <a href="#topics">Topics</a>
        <a href="#feed">Feed</a>
        <a href="#alerts">Alerts</a>
        <a href="#timeline">Timeline</a>
        <a href="#methodology">Method</a>
      </div>
    </nav>

    <main>
      <section id="status">
        <div class="status-grid">
          <aside class="cybercon {cybercon_class(level)}">
            <span>CYBERCON</span>
            <strong>{level}</strong>
          </aside>
          <article class="status-card">
            <div>{badge("Primary negative hot topic", "negative")}</div>
            <h2>{escape(top_negative["topic_label"])}</h2>
            <p class="status-narrative">{escape(narrative_for(top_negative))}</p>
            <div class="status-kpis">
              <div><span>Time window</span><strong>{fmt_timestamp(top_negative["time_window"])}</strong></div>
              <div><span>P2 index</span><strong class="negative">{fmt_signed(top_negative["p2_index"], 2)}</strong></div>
              <div><span>Topic volume</span><strong>{fmt_int(top_negative["topic_volume"])}</strong></div>
              <div><span>Sentiment sum</span><strong class="negative">{fmt_signed(top_negative["topic_sentiment_sum"], 2)}</strong></div>
            </div>
          </article>
        </div>
      </section>

      <section id="metrics">
        <h2>Metric Cards</h2>
        <p class="section-note">Compact overview of the already-generated P2 and sentiment outputs.</p>
        <div class="metrics-grid">
          {"".join(metric_cards)}
        </div>
      </section>

      <section id="topics">
        <h2>Topics Monitored</h2>
        <p class="section-note">Manual topic labels are qualitative interpretations based on LDA top words.</p>
        <div class="topic-grid">
          {topic_cards(topic_catalog)}
        </div>
      </section>

      <section id="feed">
        <h2>Hot Topic Feed</h2>
        <p class="section-note">Top 10 observations ordered by absolute P2 strength.</p>
        <div class="feed-list">
          {hot_topic_feed(p2_df)}
        </div>
      </section>

      <section id="alerts">
        <h2>Negative Alerts</h2>
        <p class="section-note">Top 10 negative P2 observations. Lower values indicate stronger negative momentum.</p>
        <div class="chart-card">
          {create_negative_alerts_chart(p2_df)}
        </div>
      </section>

      <section id="timeline">
        <h2>P2 Timeline</h2>
        <p class="section-note">The five topics with the strongest absolute P2 observations are visible by default. Other topics are available from the legend.</p>
        <div class="chart-card">
          {create_topic_line_chart(p2_df, "p2_index", "P2 index", default_topics, height=410)}
        </div>
      </section>

      <section id="volume-sentiment">
        <h2>Volume &amp; Sentiment</h2>
        <p class="section-note">Simple temporal views for topic volume and aggregated sentiment, with the same default topic visibility.</p>
        <div class="chart-pair">
          <div class="chart-card">
            {create_topic_line_chart(p2_df, "topic_volume", "Topic volume", default_topics)}
          </div>
          <div class="chart-card">
            {create_topic_line_chart(p2_df, "topic_sentiment_sum", "Topic sentiment sum", default_topics)}
          </div>
        </div>
      </section>

      <section id="methodology">
        <h2>Methodology Note</h2>
        <ul class="method-list">
          <li>LDA uses <code>text_clean</code>.</li>
          <li>VADER uses <code>text_raw</code>.</li>
          <li>P2 uses only aggregated volume and aggregated sentiment.</li>
          <li><code>original_type</code>, <code>annotation</code>, and <code>relevant</code> are not used as features; they are kept only for ex post checks.</li>
          <li>Topic labels are manual interpretations based on LDA <code>top_words</code>.</li>
        </ul>
      </section>

      <section id="downloads">
        <h2>Downloads / Links</h2>
        <ul class="download-list">
          {make_link_list(output_path)}
        </ul>
      </section>
    </main>
  </div>
</body>
</html>
"""


def print_report(p2_df: pd.DataFrame, output_path: Path) -> None:
    hottest_negative = p2_df.sort_values("p2_index", ascending=True).iloc[0]
    hottest_positive = p2_df.sort_values("p2_index", ascending=False).iloc[0]

    print(f"Dashboard saved to: {output_path}")
    print("Generation report:")
    print(
        "  Hottest negative topic: "
        f"{hottest_negative['topic_label']} | "
        f"{fmt_timestamp(hottest_negative['time_window'])} | "
        f"P2 {fmt_signed(hottest_negative['p2_index'], 4)}"
    )
    print(
        "  Hottest positive topic: "
        f"{hottest_positive['topic_label']} | "
        f"{fmt_timestamp(hottest_positive['time_window'])} | "
        f"P2 {fmt_signed(hottest_positive['p2_index'], 4)}"
    )
    print(f"  Topics: {p2_df['dominant_topic'].nunique()}")
    print(f"  Time windows: {p2_df['time_window'].nunique()}")


def main() -> int:
    args = parse_args()

    try:
        ensure_plotly_available()
        p2_input_path = resolve_project_path(args.p2_input)
        topic_words_path = resolve_project_path(args.topic_words)
        sentiment_input_path = resolve_project_path(args.sentiment_input)
        output_path = resolve_project_path(args.output)

        validate_input_path(p2_input_path, required=True)
        topic_words_df = load_topic_words(topic_words_path)
        p2_raw_df = read_csv_with_encoding_fallback(p2_input_path)
        sentiment_stats = load_sentiment_stats(sentiment_input_path)

        p2_df = prepare_p2_data(p2_raw_df, topic_words_df)
        topic_catalog = build_topic_catalog(topic_words_df, p2_df)
        dashboard_html = build_dashboard_html(p2_df, topic_catalog, sentiment_stats, output_path)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(dashboard_html, encoding="utf-8")
        print_report(p2_df, output_path)
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
    except (RuntimeError, ValueError) as exc:
        print(f"Data validation error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
