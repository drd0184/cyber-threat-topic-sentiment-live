"""
Run experimental LDA tuning for the live social/news corpus.

This script is experimental only. It writes reports under reports/live/ and
does not overwrite models/live_lda_model/ or the official 04 live LDA outputs.
It does not run VADER, P2, or dashboard export.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import product
from pathlib import Path
import sys
from typing import Iterable

import pandas as pd

try:
    from gensim import corpora
    from gensim.models import CoherenceModel, LdaModel, Phrases
    from gensim.models.phrases import Phraser
except ImportError as exc:
    corpora = None
    CoherenceModel = None
    LdaModel = None
    Phrases = None
    Phraser = None
    GENSIM_IMPORT_ERROR = exc
else:
    GENSIM_IMPORT_ERROR = None


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "live" / "processed" / "03_live_preprocessed_dataset.csv"
DEFAULT_RESULTS_PATH = PROJECT_ROOT / "reports" / "live" / "live_lda_tuning_results.csv"
DEFAULT_REPORT_PATH = PROJECT_ROOT / "reports" / "live" / "live_lda_tuning_report.md"

REQUIRED_COLUMNS = ["text_clean"]
ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")

TOKEN_VARIANTS = ["unigram", "bigram", "trigram"]
NO_BELOW_VALUES = [3, 5]
NO_ABOVE_VALUES = [0.5, 0.6]
KEEP_N = 10000
NUM_TOPICS_VALUES = [8, 10, 12, 15]
ALPHA_VALUES = ["symmetric", "asymmetric"]
ETA_VALUES = ["auto", "symmetric"]
PASSES_VALUES = [10, 20]
ITERATIONS = 200
RANDOM_STATE = 42
TOP_WORDS_COUNT = 10
BASELINE_10_COHERENCE = 0.5082
BASELINE_12_COHERENCE = 0.5203
BALANCED_LARGEST_TOPIC_MAX = 30.0
BALANCED_SMALLEST_TOPIC_MIN = 1.0
TARGET_COHERENCE = 0.55
METHODOLOGICAL_NOTE = (
    "La coherence è usata come supporto alla scelta del modello, ma la selezione "
    "finale considera anche interpretabilità, stabilità e utilità per P2."
)


@dataclass(frozen=True)
class TokenVariantCorpus:
    token_variant: str
    tokenized_texts: list[list[str]]


@dataclass(frozen=True)
class DictionaryCorpus:
    token_variant: str
    tokenized_texts: list[list[str]]
    dictionary: object
    corpus: list[list[tuple[int, int]]]
    empty_bow_count: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run experimental LDA tuning on the live social/news corpus."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_PATH)
    parser.add_argument("--results-output", type=Path, default=DEFAULT_RESULTS_PATH)
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
        raise RuntimeError("The 'gensim' package is required for LDA tuning.") from GENSIM_IMPORT_ERROR


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
        raise ValueError(f"Duplicate column name(s) found in CSV: {', '.join(duplicate_columns)}")
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required column(s): {', '.join(missing_columns)}")


def load_tokenized_texts(df: pd.DataFrame) -> list[list[str]]:
    validate_columns(df)
    text_clean = df["text_clean"].fillna("").astype("string").str.strip()
    tokenized = [str(text).split() for text in text_clean if str(text).strip()]
    if not tokenized:
        raise ValueError("No non-empty text_clean rows found.")
    return tokenized


def build_token_variants(base_tokens: list[list[str]]) -> list[TokenVariantCorpus]:
    variants = [TokenVariantCorpus("unigram", base_tokens)]

    bigram_model = Phrases(base_tokens, min_count=5, threshold=10)
    bigram_phraser = Phraser(bigram_model)
    bigram_tokens = [bigram_phraser[tokens] for tokens in base_tokens]
    variants.append(TokenVariantCorpus("bigram", bigram_tokens))

    trigram_model = Phrases(bigram_tokens, min_count=5, threshold=10)
    trigram_phraser = Phraser(trigram_model)
    trigram_tokens = [trigram_phraser[bigram_phraser[tokens]] for tokens in base_tokens]
    variants.append(TokenVariantCorpus("trigram", trigram_tokens))
    return variants


def build_dictionary_corpus(
    variant: TokenVariantCorpus,
    no_below: int,
    no_above: float,
) -> DictionaryCorpus:
    dictionary = corpora.Dictionary(variant.tokenized_texts)
    dictionary.filter_extremes(no_below=no_below, no_above=no_above, keep_n=KEEP_N)
    corpus = [dictionary.doc2bow(tokens) for tokens in variant.tokenized_texts]
    empty_bow_count = sum(1 for bow in corpus if not bow)
    return DictionaryCorpus(
        token_variant=variant.token_variant,
        tokenized_texts=variant.tokenized_texts,
        dictionary=dictionary,
        corpus=corpus,
        empty_bow_count=empty_bow_count,
    )


def train_lda(dictionary_corpus: DictionaryCorpus, num_topics: int, alpha: str, eta: str, passes: int) -> object:
    return LdaModel(
        corpus=dictionary_corpus.corpus,
        id2word=dictionary_corpus.dictionary,
        num_topics=num_topics,
        random_state=RANDOM_STATE,
        passes=passes,
        iterations=ITERATIONS,
        alpha=alpha,
        eta=eta,
        eval_every=None,
    )


def compute_coherence(model: object, dictionary_corpus: DictionaryCorpus) -> float:
    coherence_model = CoherenceModel(
        model=model,
        texts=dictionary_corpus.tokenized_texts,
        dictionary=dictionary_corpus.dictionary,
        coherence="c_v",
        processes=1,
    )
    return float(coherence_model.get_coherence())


def get_dominant_topic(model: object, bow: list[tuple[int, int]]) -> int:
    if not bow:
        return -1
    distribution = model.get_document_topics(bow, minimum_probability=0.0)
    topic_id, _ = max(distribution, key=lambda item: item[1])
    return int(topic_id)


def topic_distribution_metrics(model: object, dictionary_corpus: DictionaryCorpus, num_topics: int) -> tuple[dict[int, int], float, float]:
    topic_counts = {topic_id: 0 for topic_id in range(num_topics)}
    for bow in dictionary_corpus.corpus:
        topic_id = get_dominant_topic(model, bow)
        if topic_id >= 0:
            topic_counts[topic_id] += 1

    assigned_docs = sum(topic_counts.values())
    if assigned_docs == 0:
        return topic_counts, 0.0, 0.0

    percents = [(count / assigned_docs) * 100.0 for count in topic_counts.values()]
    return topic_counts, max(percents), min(percents)


def topic_words_summary(model: object, num_topics: int) -> str:
    chunks = []
    for topic_id in range(num_topics):
        words = [word for word, _ in model.show_topic(topic_id, topn=TOP_WORDS_COUNT)]
        chunks.append(f"T{topic_id}: {', '.join(words)}")
    return " | ".join(chunks)


def run_experiments(base_tokens: list[list[str]]) -> pd.DataFrame:
    ensure_gensim_available()
    variants = build_token_variants(base_tokens)
    rows: list[dict[str, object]] = []
    experiment_id = 0
    total_experiments = (
        len(TOKEN_VARIANTS)
        * len(NO_BELOW_VALUES)
        * len(NO_ABOVE_VALUES)
        * len(NUM_TOPICS_VALUES)
        * len(ALPHA_VALUES)
        * len(ETA_VALUES)
        * len(PASSES_VALUES)
    )

    for variant in variants:
        for no_below, no_above in product(NO_BELOW_VALUES, NO_ABOVE_VALUES):
            dictionary_corpus = build_dictionary_corpus(variant, no_below, no_above)
            if len(dictionary_corpus.dictionary) == 0:
                continue
            for num_topics, alpha, eta, passes in product(
                NUM_TOPICS_VALUES,
                ALPHA_VALUES,
                ETA_VALUES,
                PASSES_VALUES,
            ):
                experiment_id += 1
                print(
                    f"[{experiment_id}/{total_experiments}] "
                    f"{variant.token_variant} topics={num_topics} no_below={no_below} "
                    f"no_above={no_above} alpha={alpha} eta={eta} passes={passes}",
                    flush=True,
                )
                try:
                    model = train_lda(dictionary_corpus, num_topics, alpha, eta, passes)
                    coherence = compute_coherence(model, dictionary_corpus)
                    topic_counts, largest_percent, smallest_percent = topic_distribution_metrics(
                        model,
                        dictionary_corpus,
                        num_topics,
                    )
                    rows.append(
                        {
                            "experiment_id": experiment_id,
                            "token_variant": variant.token_variant,
                            "num_topics": num_topics,
                            "no_below": no_below,
                            "no_above": no_above,
                            "alpha": alpha,
                            "eta": eta,
                            "passes": passes,
                            "coherence_cv": coherence,
                            "vocabulary_size": len(dictionary_corpus.dictionary),
                            "num_docs_used": len(dictionary_corpus.tokenized_texts),
                            "empty_bow_count": dictionary_corpus.empty_bow_count,
                            "largest_topic_percent": largest_percent,
                            "smallest_topic_percent": smallest_percent,
                            "topic_words_summary": topic_words_summary(model, num_topics),
                            "topic_distribution": "; ".join(
                                f"T{topic_id}: {count}" for topic_id, count in topic_counts.items()
                            ),
                        }
                    )
                except Exception as exc:
                    print(f"Warning: experiment {experiment_id} failed: {exc}", file=sys.stderr)
                    rows.append(
                        {
                            "experiment_id": experiment_id,
                            "token_variant": variant.token_variant,
                            "num_topics": num_topics,
                            "no_below": no_below,
                            "no_above": no_above,
                            "alpha": alpha,
                            "eta": eta,
                            "passes": passes,
                            "coherence_cv": "",
                            "vocabulary_size": len(dictionary_corpus.dictionary),
                            "num_docs_used": len(dictionary_corpus.tokenized_texts),
                            "empty_bow_count": dictionary_corpus.empty_bow_count,
                            "largest_topic_percent": "",
                            "smallest_topic_percent": "",
                            "topic_words_summary": "",
                            "topic_distribution": "",
                        }
                    )
    return pd.DataFrame(rows)


def markdown_table(headers: list[str], rows: Iterable[Iterable[object]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(value) for value in row) + " |")
    return "\n".join(lines)


def compact_summary(value: object, max_chars: int = 220) -> str:
    text = "" if pd.isna(value) else str(value)
    return text if len(text) <= max_chars else text[: max_chars - 3] + "..."


def result_rows(df: pd.DataFrame) -> list[list[object]]:
    columns = [
        "experiment_id",
        "token_variant",
        "num_topics",
        "no_below",
        "no_above",
        "alpha",
        "eta",
        "passes",
        "coherence_cv",
        "largest_topic_percent",
        "smallest_topic_percent",
        "empty_bow_count",
        "topic_words_summary",
    ]
    rows = []
    for row in df[columns].itertuples(index=False):
        values = list(row)
        values[8] = f"{float(values[8]):.4f}"
        values[9] = f"{float(values[9]):.2f}"
        values[10] = f"{float(values[10]):.2f}"
        values[12] = compact_summary(values[12])
        rows.append(values)
    return rows


def build_report(results_df: pd.DataFrame) -> str:
    valid = results_df.copy()
    valid["coherence_cv"] = pd.to_numeric(valid["coherence_cv"], errors="coerce")
    valid["largest_topic_percent"] = pd.to_numeric(valid["largest_topic_percent"], errors="coerce")
    valid["smallest_topic_percent"] = pd.to_numeric(valid["smallest_topic_percent"], errors="coerce")
    valid = valid.loc[valid["coherence_cv"].notna()].copy()

    top_coherence = valid.sort_values("coherence_cv", ascending=False).head(10)
    balanced = valid.loc[
        valid["largest_topic_percent"].lt(BALANCED_LARGEST_TOPIC_MAX)
        & valid["smallest_topic_percent"].gt(BALANCED_SMALLEST_TOPIC_MIN)
    ].sort_values("coherence_cv", ascending=False).head(10)

    best = valid.sort_values("coherence_cv", ascending=False).head(1)
    best_balanced = balanced.head(1)
    recommendation = (
        "Scegliere una configurazione solo se migliora coherence senza produrre "
        "topic troppo sbilanciati. Confrontare sempre top words e distribuzioni "
        "prima di sostituire il modello live corrente."
    )
    if not best_balanced.empty:
        row = best_balanced.iloc[0]
        recommendation += (
            f" Migliore candidata bilanciata: experiment_id={int(row.experiment_id)}, "
            f"{row.token_variant}, {int(row.num_topics)} topic, coherence={row.coherence_cv:.4f}."
        )

    target_reached = bool(not best.empty and float(best.iloc[0]["coherence_cv"]) >= TARGET_COHERENCE)

    sections = [
        "# Live LDA Tuning Experiments",
        "Experimental tuning report. No official live LDA model or official 04 outputs are overwritten.",
        "## Baseline Comparison",
        markdown_table(
            ["baseline_config", "coherence_cv"],
            [
                ["current 10 topics", f"{BASELINE_10_COHERENCE:.4f}"],
                ["current 12 topics", f"{BASELINE_12_COHERENCE:.4f}"],
            ],
        ),
        "## Target",
        f"Target coherence: {TARGET_COHERENCE:.2f}. Target reached: {'yes' if target_reached else 'no'}.",
        "## Top 10 Configurations by Coherence",
        markdown_table(
            [
                "experiment_id",
                "token_variant",
                "num_topics",
                "no_below",
                "no_above",
                "alpha",
                "eta",
                "passes",
                "coherence_cv",
                "largest_topic_percent",
                "smallest_topic_percent",
                "empty_bow_count",
                "topic_words_summary",
            ],
            result_rows(top_coherence),
        ),
        "## Top 10 Balanced Configurations",
        markdown_table(
            [
                "experiment_id",
                "token_variant",
                "num_topics",
                "no_below",
                "no_above",
                "alpha",
                "eta",
                "passes",
                "coherence_cv",
                "largest_topic_percent",
                "smallest_topic_percent",
                "empty_bow_count",
                "topic_words_summary",
            ],
            result_rows(balanced),
        )
        if not balanced.empty
        else "No balanced configurations matched largest_topic_percent < 30 and smallest_topic_percent > 1.",
        "## Recommendation",
        recommendation,
        "## Methodological Note",
        METHODOLOGICAL_NOTE,
    ]
    return "\n\n".join(sections) + "\n"


def write_outputs(results_df: pd.DataFrame, report: str, results_path: Path, report_path: Path) -> None:
    results_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    results_df.to_csv(results_path, index=False, encoding="utf-8")
    report_path.write_text(report, encoding="utf-8")


def print_summary(results_df: pd.DataFrame, results_path: Path, report_path: Path) -> None:
    valid = results_df.copy()
    valid["coherence_cv"] = pd.to_numeric(valid["coherence_cv"], errors="coerce")
    valid["largest_topic_percent"] = pd.to_numeric(valid["largest_topic_percent"], errors="coerce")
    valid["smallest_topic_percent"] = pd.to_numeric(valid["smallest_topic_percent"], errors="coerce")
    valid = valid.loc[valid["coherence_cv"].notna()].copy()
    best = valid.sort_values("coherence_cv", ascending=False).iloc[0]
    balanced = valid.loc[
        valid["largest_topic_percent"].lt(BALANCED_LARGEST_TOPIC_MAX)
        & valid["smallest_topic_percent"].gt(BALANCED_SMALLEST_TOPIC_MIN)
    ].sort_values("coherence_cv", ascending=False)

    print("Live LDA tuning experiments")
    print("===========================")
    print(f"Experiments run: {len(results_df)}")
    print(
        "Best coherence: "
        f"{best.coherence_cv:.4f} | experiment_id={int(best.experiment_id)} | "
        f"{best.token_variant} | topics={int(best.num_topics)}"
    )
    if not balanced.empty:
        row = balanced.iloc[0]
        print(
            "Best balanced: "
            f"{row.coherence_cv:.4f} | experiment_id={int(row.experiment_id)} | "
            f"{row.token_variant} | topics={int(row.num_topics)} | "
            f"largest={row.largest_topic_percent:.2f}% | smallest={row.smallest_topic_percent:.2f}%"
        )
    else:
        print("Best balanced: n/a")
    print(f"Target >= {TARGET_COHERENCE:.2f}: {'yes' if best.coherence_cv >= TARGET_COHERENCE else 'no'}")
    print(f"Results CSV: {results_path}")
    print(f"Report: {report_path}")


def main() -> int:
    args = parse_args()
    input_path = resolve_project_path(args.input)
    results_path = resolve_project_path(args.results_output)
    report_path = resolve_project_path(args.report)

    try:
        validate_file(input_path, "Input CSV")
        df, _ = read_csv_with_encoding_fallback(input_path)
        ensure_gensim_available()
        base_tokens = load_tokenized_texts(df)
        results_df = run_experiments(base_tokens)
        report = build_report(results_df)
        write_outputs(results_df, report, results_path, report_path)
        print_summary(results_df, results_path, report_path)
    except Exception as exc:
        print(f"Live LDA tuning error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
