"""
Train a new live LDA baseline on the recent social/news corpus.

This script does not use the old static LDA model. It trains and compares live
LDA configurations using only text_clean from the social/news live corpus, then
saves the selected model under models/live_lda_model/.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import sys

import pandas as pd

try:
    from gensim import corpora
    from gensim.corpora import MmCorpus
    from gensim.models import CoherenceModel, LdaModel
except ImportError as exc:
    corpora = None
    MmCorpus = None
    CoherenceModel = None
    LdaModel = None
    GENSIM_IMPORT_ERROR = exc
else:
    GENSIM_IMPORT_ERROR = None


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LIVE_PROCESSED_DIR = PROJECT_ROOT / "data" / "live" / "processed"
LIVE_REPORTS_DIR = PROJECT_ROOT / "reports" / "live"
LIVE_MODEL_DIR = PROJECT_ROOT / "models" / "live_lda_model"

DEFAULT_INPUT_PATH = LIVE_PROCESSED_DIR / "03_live_preprocessed_dataset.csv"
DEFAULT_TOPICS_OUTPUT_PATH = LIVE_PROCESSED_DIR / "04_live_lda_topics_dataset.csv"
DEFAULT_TOPIC_WORDS_OUTPUT_PATH = LIVE_PROCESSED_DIR / "04_live_lda_topic_words.csv"
DEFAULT_COMPARISON_OUTPUT_PATH = LIVE_REPORTS_DIR / "live_lda_config_comparison.csv"
DEFAULT_REPORT_PATH = LIVE_REPORTS_DIR / "live_lda_training_report.md"
DEFAULT_MODEL_PATH = LIVE_MODEL_DIR / "lda_model.gensim"
DEFAULT_DICTIONARY_PATH = LIVE_MODEL_DIR / "dictionary.gensim"
DEFAULT_CORPUS_PATH = LIVE_MODEL_DIR / "corpus.mm"

REQUIRED_COLUMNS = [
    "id",
    "created_at",
    "source",
    "source_name",
    "source_type",
    "title",
    "text_raw",
    "text_clean",
    "url",
    "collected_at",
]

ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")
TOPIC_CONFIGS = [8, 10, 12, 15]
NO_BELOW = 3
NO_ABOVE = 0.60
KEEP_N = 10000
RANDOM_STATE = 42
PASSES = 12
ITERATIONS = 150
TOP_WORDS_COUNT = 12
COHERENCE_SIMILARITY_THRESHOLD = 0.02
METHODOLOGICAL_NOTE = (
    "Questo modello LDA live è addestrato esclusivamente su fonti social/news "
    "recenti. Il vecchio LDA statico non viene usato per assegnare topic nella "
    "pipeline live principale."
)


@dataclass(frozen=True)
class PreparedCorpus:
    modeling_df: pd.DataFrame
    tokenized_texts: list[list[str]]
    dictionary: object
    corpus: list[list[tuple[int, int]]]


@dataclass(frozen=True)
class ConfigResult:
    num_topics: int
    model: object
    coherence_cv: float | None
    topic_words: pd.DataFrame
    assigned_df: pd.DataFrame


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Train and compare live LDA models on social/news text_clean."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_PATH)
    parser.add_argument("--topics-output", type=Path, default=DEFAULT_TOPICS_OUTPUT_PATH)
    parser.add_argument("--topic-words-output", type=Path, default=DEFAULT_TOPIC_WORDS_OUTPUT_PATH)
    parser.add_argument("--comparison-output", type=Path, default=DEFAULT_COMPARISON_OUTPUT_PATH)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT_PATH)
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
        raise RuntimeError("The 'gensim' package is required to train live LDA.") from GENSIM_IMPORT_ERROR


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


def prepare_corpus(df: pd.DataFrame) -> PreparedCorpus:
    validate_columns(df)
    ensure_gensim_available()

    modeling_df = df.copy()
    modeling_df["text_clean"] = modeling_df["text_clean"].fillna("").astype("string").str.strip()
    modeling_df = modeling_df.loc[modeling_df["text_clean"].ne("")].reset_index(drop=True)
    if modeling_df.empty:
        raise ValueError("No rows left after removing empty text_clean.")

    tokenized_texts = [text.split() for text in modeling_df["text_clean"].astype(str)]
    dictionary = corpora.Dictionary(tokenized_texts)
    dictionary.filter_extremes(no_below=NO_BELOW, no_above=NO_ABOVE, keep_n=KEEP_N)
    if len(dictionary) == 0:
        raise ValueError("Dictionary is empty after filter_extremes.")

    corpus = [dictionary.doc2bow(tokens) for tokens in tokenized_texts]
    if not any(corpus):
        raise ValueError("Corpus is empty after bag-of-words conversion.")

    return PreparedCorpus(
        modeling_df=modeling_df,
        tokenized_texts=tokenized_texts,
        dictionary=dictionary,
        corpus=corpus,
    )


def train_lda(corpus: list[list[tuple[int, int]]], dictionary: object, num_topics: int) -> object:
    return LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        random_state=RANDOM_STATE,
        passes=PASSES,
        iterations=ITERATIONS,
        alpha="auto",
        eta="auto",
        eval_every=None,
    )


def compute_coherence(model: object, tokenized_texts: list[list[str]], dictionary: object) -> float | None:
    try:
        coherence_model = CoherenceModel(
            model=model,
            texts=tokenized_texts,
            dictionary=dictionary,
            coherence="c_v",
            processes=1,
        )
        return float(coherence_model.get_coherence())
    except Exception as exc:
        print(f"Warning: could not compute c_v coherence: {exc}", file=sys.stderr)
        return None


def topic_words_table(model: object, num_topics: int, selected: bool = False) -> pd.DataFrame:
    rows = []
    for topic_id in range(num_topics):
        top_words = [word for word, _ in model.show_topic(topic_id, topn=TOP_WORDS_COUNT)]
        row = {"topic_id": topic_id, "top_words": ", ".join(top_words)}
        if selected:
            row["num_topics_selected"] = num_topics
        rows.append(row)
    return pd.DataFrame(rows)


def assign_topics(df: pd.DataFrame, model: object, corpus: list[list[tuple[int, int]]]) -> pd.DataFrame:
    assigned = df.copy()
    dominant_topics: list[int] = []
    probabilities: list[float] = []
    statuses: list[str] = []

    for bow in corpus:
        if not bow:
            dominant_topics.append(-1)
            probabilities.append(0.0)
            statuses.append("empty_bow")
            continue

        distribution = model.get_document_topics(bow, minimum_probability=0.0)
        topic_id, probability = max(distribution, key=lambda item: item[1])
        dominant_topics.append(int(topic_id))
        probabilities.append(float(probability))
        statuses.append("assigned")

    assigned["dominant_topic"] = dominant_topics
    assigned["dominant_topic_probability"] = probabilities
    assigned["topic_assignment_status"] = statuses
    return assigned


def source_type_by_topic_rows(assigned: pd.DataFrame) -> pd.DataFrame:
    return (
        assigned.loc[assigned["dominant_topic"].ge(0)]
        .groupby(["dominant_topic", "source_type"], dropna=False)
        .size()
        .rename("rows")
        .reset_index()
        .sort_values(["dominant_topic", "rows"], ascending=[True, False])
    )


def dominant_source_type_by_topic(assigned: pd.DataFrame) -> dict[int, str]:
    grouped = source_type_by_topic_rows(assigned)
    dominant: dict[int, str] = {}
    for topic_id, group in grouped.groupby("dominant_topic"):
        if group.empty:
            dominant[int(topic_id)] = ""
        else:
            dominant[int(topic_id)] = str(group.sort_values("rows", ascending=False).iloc[0]["source_type"])
    return dominant


def compare_configs(prepared: PreparedCorpus) -> tuple[list[ConfigResult], pd.DataFrame]:
    results: list[ConfigResult] = []
    comparison_rows: list[dict[str, object]] = []

    for num_topics in TOPIC_CONFIGS:
        model = train_lda(prepared.corpus, prepared.dictionary, num_topics)
        coherence = compute_coherence(model, prepared.tokenized_texts, prepared.dictionary)
        topic_words = topic_words_table(model, num_topics)
        assigned = assign_topics(prepared.modeling_df, model, prepared.corpus)
        dominant_source = dominant_source_type_by_topic(assigned)
        doc_counts = assigned["dominant_topic"].value_counts().sort_index().to_dict()
        total_docs = len(assigned)

        for topic_row in topic_words.itertuples(index=False):
            topic_id = int(topic_row.topic_id)
            docs_assigned = int(doc_counts.get(topic_id, 0))
            comparison_rows.append(
                {
                    "num_topics": num_topics,
                    "topic_id": topic_id,
                    "top_words": topic_row.top_words,
                    "docs_assigned": docs_assigned,
                    "percent_docs": round((docs_assigned / total_docs) * 100.0, 2) if total_docs else 0.0,
                    "dominant_source_type_ex_post": dominant_source.get(topic_id, ""),
                    "coherence_cv_config": coherence if coherence is not None else "",
                }
            )

        results.append(
            ConfigResult(
                num_topics=num_topics,
                model=model,
                coherence_cv=coherence,
                topic_words=topic_words,
                assigned_df=assigned,
            )
        )

    return results, pd.DataFrame(comparison_rows)


def select_best_config(results: list[ConfigResult]) -> tuple[ConfigResult, str]:
    valid_results = [result for result in results if result.coherence_cv is not None]
    if not valid_results:
        fallback = next(result for result in results if result.num_topics == 10)
        return fallback, "Coherence c_v non disponibile; selezionata configurazione a 10 topic per interpretabilita."

    best = max(valid_results, key=lambda result: float(result.coherence_cv))
    ten_topic = next((result for result in valid_results if result.num_topics == 10), None)
    if ten_topic is not None:
        diff = float(best.coherence_cv) - float(ten_topic.coherence_cv)
        if best.num_topics != 10 and diff < COHERENCE_SIMILARITY_THRESHOLD:
            return (
                ten_topic,
                (
                    "La configurazione con coherence piu alta e "
                    f"{best.num_topics} topic, ma la differenza rispetto a 10 topic "
                    f"e {diff:.4f}, inferiore alla soglia {COHERENCE_SIMILARITY_THRESHOLD:.2f}; "
                    "selezionati 10 topic per interpretabilita."
                ),
            )

    return (
        best,
        f"Selezionata configurazione a {best.num_topics} topic per coherence c_v piu alta.",
    )


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


def coherence_rows(results: list[ConfigResult]) -> list[list[object]]:
    return [
        [
            result.num_topics,
            f"{float(result.coherence_cv):.4f}" if result.coherence_cv is not None else "n/a",
        ]
        for result in results
    ]


def topic_words_rows(topic_words: pd.DataFrame) -> list[list[object]]:
    return [[int(row.topic_id), row.top_words] for row in topic_words.itertuples(index=False)]


def doc_distribution_rows(assigned: pd.DataFrame) -> list[list[object]]:
    total = len(assigned)
    counts = assigned["dominant_topic"].value_counts().sort_index()
    return [
        [int(topic_id), int(count), f"{percentage(count, total):.2f}%"]
        for topic_id, count in counts.items()
    ]


def source_type_topic_rows(assigned: pd.DataFrame) -> list[list[object]]:
    rows = []
    grouped = source_type_by_topic_rows(assigned)
    for row in grouped.itertuples(index=False):
        rows.append([int(row.dominant_topic), row.source_type, int(row.rows)])
    return rows


def build_report(
    input_rows: int,
    prepared: PreparedCorpus,
    results: list[ConfigResult],
    selected: ConfigResult,
    selection_reason: str,
    encoding_used: str,
) -> str:
    selected_topic_words = topic_words_table(selected.model, selected.num_topics)
    selected_assigned = selected.assigned_df
    return "\n\n".join(
        [
            "# Live LDA Training Report",
            "## Summary",
            markdown_table(
                ["Metric", "Value"],
                [
                    ["Input rows", input_rows],
                    ["Rows used", len(prepared.modeling_df)],
                    ["Vocabulary size", len(prepared.dictionary)],
                    ["Configurations tested", ", ".join(str(value) for value in TOPIC_CONFIGS)],
                    ["Selected num_topics", selected.num_topics],
                    [
                        "Selected coherence c_v",
                        f"{float(selected.coherence_cv):.4f}" if selected.coherence_cv is not None else "n/a",
                    ],
                    ["Encoding used", encoding_used],
                ],
            ),
            "## Coherence by Configuration",
            markdown_table(["num_topics", "coherence_cv"], coherence_rows(results)),
            "## Selection Rationale",
            selection_reason,
            "## Final Topics",
            markdown_table(["topic_id", "top_words"], topic_words_rows(selected_topic_words)),
            "## Document Distribution by Topic",
            markdown_table(["dominant_topic", "docs_assigned", "percent_docs"], doc_distribution_rows(selected_assigned)),
            "## Source Type Distribution by Topic (Ex Post)",
            markdown_table(["dominant_topic", "source_type", "rows"], source_type_topic_rows(selected_assigned)),
            "## Methodological Note",
            METHODOLOGICAL_NOTE,
        ]
    ) + "\n"


def save_outputs(
    prepared: PreparedCorpus,
    selected: ConfigResult,
    comparison_df: pd.DataFrame,
    report: str,
    topics_output_path: Path,
    topic_words_output_path: Path,
    comparison_output_path: Path,
    report_path: Path,
) -> None:
    topics_output_path.parent.mkdir(parents=True, exist_ok=True)
    topic_words_output_path.parent.mkdir(parents=True, exist_ok=True)
    comparison_output_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    LIVE_MODEL_DIR.mkdir(parents=True, exist_ok=True)

    final_assigned = selected.assigned_df.copy()
    final_topic_words = topic_words_table(selected.model, selected.num_topics, selected=True)

    final_assigned.to_csv(topics_output_path, index=False, encoding="utf-8")
    final_topic_words.to_csv(topic_words_output_path, index=False, encoding="utf-8")
    comparison_df.to_csv(comparison_output_path, index=False, encoding="utf-8")
    report_path.write_text(report, encoding="utf-8")

    selected.model.save(str(DEFAULT_MODEL_PATH))
    prepared.dictionary.save(str(DEFAULT_DICTIONARY_PATH))
    MmCorpus.serialize(str(DEFAULT_CORPUS_PATH), prepared.corpus)


def print_summary(
    input_rows: int,
    prepared: PreparedCorpus,
    results: list[ConfigResult],
    selected: ConfigResult,
    topics_output_path: Path,
    comparison_output_path: Path,
    report_path: Path,
) -> None:
    print("Live LDA baseline training")
    print("==========================")
    print(f"Input rows: {input_rows}")
    print(f"Rows used: {len(prepared.modeling_df)}")
    print(f"Vocabulary size: {len(prepared.dictionary)}")
    print("Coherence c_v:")
    for result in results:
        value = f"{float(result.coherence_cv):.4f}" if result.coherence_cv is not None else "n/a"
        print(f"  - {result.num_topics} topics: {value}")
    print(f"Selected num_topics: {selected.num_topics}")
    print(f"Output topics dataset: {topics_output_path}")
    print(f"Comparison CSV: {comparison_output_path}")
    print(f"Report: {report_path}")
    print(f"Model dir: {LIVE_MODEL_DIR}")


def main() -> int:
    args = parse_args()
    input_path = resolve_project_path(args.input)
    topics_output_path = resolve_project_path(args.topics_output)
    topic_words_output_path = resolve_project_path(args.topic_words_output)
    comparison_output_path = resolve_project_path(args.comparison_output)
    report_path = resolve_project_path(args.report)

    try:
        validate_file(input_path, "Input CSV")
        df, encoding_used = read_csv_with_encoding_fallback(input_path)
        prepared = prepare_corpus(df)
        results, comparison_df = compare_configs(prepared)
        selected, selection_reason = select_best_config(results)
        report = build_report(
            input_rows=len(df),
            prepared=prepared,
            results=results,
            selected=selected,
            selection_reason=selection_reason,
            encoding_used=encoding_used,
        )
        save_outputs(
            prepared,
            selected,
            comparison_df,
            report,
            topics_output_path,
            topic_words_output_path,
            comparison_output_path,
            report_path,
        )
        print_summary(
            len(df),
            prepared,
            results,
            selected,
            topics_output_path,
            comparison_output_path,
            report_path,
        )
    except Exception as exc:
        print(f"Live LDA training error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
