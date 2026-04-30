"""
Train an unsupervised LDA topic model on preprocessed cybersecurity text.

Only text_clean is used as the modeling feature. Qualitative metadata columns
such as original_type, annotation, and relevant are preserved in the enriched
dataset for ex post evaluation, but are not used to train LDA.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import sys
from pathlib import Path

import pandas as pd

try:
    from gensim import corpora
    from gensim.corpora import MmCorpus
    from gensim.models import LdaModel
except ImportError as exc:
    corpora = None
    MmCorpus = None
    LdaModel = None
    GENSIM_IMPORT_ERROR = exc
else:
    GENSIM_IMPORT_ERROR = None


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
MODEL_DIR = PROJECT_ROOT / "models" / "lda_model"

DEFAULT_INPUT_PATH = PROCESSED_DIR / "03b_cyber_relevant_dataset.csv"
DEFAULT_TOPICS_DATASET_PATH = PROCESSED_DIR / "04_lda_topics_dataset.csv"
DEFAULT_TOPIC_WORDS_PATH = PROCESSED_DIR / "04_lda_topic_words.csv"
DEFAULT_MODEL_PATH = MODEL_DIR / "lda_model.gensim"
DEFAULT_DICTIONARY_PATH = MODEL_DIR / "dictionary.gensim"
DEFAULT_CORPUS_PATH = MODEL_DIR / "corpus.mm"

REQUIRED_COLUMNS = {"text_clean"}
ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")

NO_BELOW = 5
NO_ABOVE = 0.5
NUM_TOPICS = 10
RANDOM_STATE = 42
PASSES = 10
ITERATIONS = 100
TOP_WORDS_COUNT = 10


@dataclass(frozen=True)
class LdaReport:
    documents_used: int
    vocabulary_size: int
    num_topics: int
    topic_document_counts: dict[int, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Train a gensim LDA model on text_clean and save topic outputs."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="Path to the preprocessed CSV.",
    )
    parser.add_argument(
        "--topics-output",
        type=Path,
        default=DEFAULT_TOPICS_DATASET_PATH,
        help="Path for the document-level topic dataset.",
    )
    parser.add_argument(
        "--topic-words-output",
        type=Path,
        default=DEFAULT_TOPIC_WORDS_PATH,
        help="Path for the topic words CSV.",
    )
    return parser.parse_args()


def resolve_project_path(path: Path) -> Path:
    return path if path.is_absolute() else PROJECT_ROOT / path


def validate_input_path(input_path: Path) -> None:
    if not input_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {input_path}")
    if not input_path.is_file():
        raise FileNotFoundError(f"Input path is not a file: {input_path}")
    if input_path.suffix.lower() != ".csv":
        raise ValueError(f"Input file must be a CSV: {input_path}")


def ensure_gensim_available() -> None:
    if GENSIM_IMPORT_ERROR is not None:
        raise RuntimeError(
            "The 'gensim' package is not installed. Install it with "
            "'pip install gensim' and rerun this script."
        ) from GENSIM_IMPORT_ERROR


def read_csv_with_encoding_fallback(input_path: Path) -> tuple[pd.DataFrame, str]:
    last_error: UnicodeDecodeError | None = None

    for encoding in ENCODINGS_TO_TRY:
        try:
            df = pd.read_csv(
                input_path,
                dtype={"text_clean": "string"},
                encoding=encoding,
                low_memory=False,
            )
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

    missing_columns = sorted(REQUIRED_COLUMNS.difference(df.columns))
    if missing_columns:
        available = ", ".join(df.columns)
        missing = ", ".join(missing_columns)
        raise ValueError(
            f"Missing required column(s): {missing}\nAvailable columns: {available}"
        )


def tokenize_texts(df: pd.DataFrame) -> tuple[list[int], list[list[str]]]:
    text_clean = df["text_clean"].astype("string").fillna("").str.strip()
    document_indices = []
    tokenized_texts = []

    for row_index, text in text_clean.items():
        tokens = text.split()
        if tokens:
            document_indices.append(row_index)
            tokenized_texts.append(tokens)

    if not tokenized_texts:
        raise ValueError("Corpus is empty: no tokens found in text_clean.")

    return document_indices, tokenized_texts


def build_dictionary_and_corpus(tokenized_texts: list[list[str]]):
    dictionary = corpora.Dictionary(tokenized_texts)
    dictionary.filter_extremes(no_below=NO_BELOW, no_above=NO_ABOVE)

    if len(dictionary) == 0:
        raise ValueError(
            "Corpus is empty after dictionary filtering. Try lowering no_below "
            "or increasing no_above."
        )

    corpus_with_positions = [
        (position, dictionary.doc2bow(tokens))
        for position, tokens in enumerate(tokenized_texts)
    ]
    corpus_with_positions = [
        (position, doc_bow) for position, doc_bow in corpus_with_positions if doc_bow
    ]

    if not corpus_with_positions:
        raise ValueError("Corpus is empty after bag-of-words conversion.")

    used_positions = [position for position, _ in corpus_with_positions]
    corpus = [doc_bow for _, doc_bow in corpus_with_positions]

    return dictionary, corpus, used_positions


def train_lda_model(corpus, dictionary):
    return LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=NUM_TOPICS,
        random_state=RANDOM_STATE,
        passes=PASSES,
        iterations=ITERATIONS,
        alpha="auto",
        eta="auto",
    )


def get_dominant_topic(lda_model, doc_bow) -> tuple[int | None, float]:
    topic_distribution = lda_model.get_document_topics(doc_bow, minimum_probability=0.0)
    if not topic_distribution:
        return None, 0.0

    topic_id, probability = max(topic_distribution, key=lambda item: item[1])
    return int(topic_id), float(probability)


def create_topic_words_table(lda_model) -> pd.DataFrame:
    rows = []
    for topic_id in range(NUM_TOPICS):
        top_words = [word for word, _ in lda_model.show_topic(topic_id, topn=TOP_WORDS_COUNT)]
        rows.append({"topic_id": topic_id, "top_words": ", ".join(top_words)})
    return pd.DataFrame(rows)


def run_lda(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, object, object, list, LdaReport]:
    validate_columns(df)
    ensure_gensim_available()

    modeling_df = df.copy()
    modeling_df["text_clean"] = modeling_df["text_clean"].astype("string").fillna("").str.strip()
    modeling_df = modeling_df.loc[modeling_df["text_clean"] != ""].reset_index(drop=True)

    document_indices, tokenized_texts = tokenize_texts(modeling_df)
    dictionary, corpus, used_positions = build_dictionary_and_corpus(tokenized_texts)
    lda_model = train_lda_model(corpus, dictionary)

    dominant_topics = []
    dominant_probabilities = []
    for doc_bow in corpus:
        topic_id, probability = get_dominant_topic(lda_model, doc_bow)
        dominant_topics.append(topic_id)
        dominant_probabilities.append(probability)

    used_document_indices = [document_indices[position] for position in used_positions]
    topics_df = modeling_df.loc[used_document_indices].copy().reset_index(drop=True)
    topics_df["dominant_topic"] = dominant_topics
    topics_df["dominant_topic_probability"] = dominant_probabilities

    topic_words_df = create_topic_words_table(lda_model)
    topic_document_counts = (
        topics_df["dominant_topic"].value_counts().sort_index().astype(int).to_dict()
    )
    topic_document_counts = {
        topic_id: int(topic_document_counts.get(topic_id, 0))
        for topic_id in range(NUM_TOPICS)
    }

    report = LdaReport(
        documents_used=len(topics_df),
        vocabulary_size=len(dictionary),
        num_topics=NUM_TOPICS,
        topic_document_counts=topic_document_counts,
    )

    return topics_df, topic_words_df, lda_model, dictionary, corpus, report


def save_outputs(
    topics_df: pd.DataFrame,
    topic_words_df: pd.DataFrame,
    lda_model,
    dictionary,
    corpus,
    topics_output_path: Path,
    topic_words_output_path: Path,
) -> None:
    topics_output_path.parent.mkdir(parents=True, exist_ok=True)
    topic_words_output_path.parent.mkdir(parents=True, exist_ok=True)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    topics_df.to_csv(topics_output_path, index=False)
    topic_words_df.to_csv(topic_words_output_path, index=False)
    lda_model.save(str(DEFAULT_MODEL_PATH))
    dictionary.save(str(DEFAULT_DICTIONARY_PATH))
    MmCorpus.serialize(str(DEFAULT_CORPUS_PATH), corpus)


def print_final_report(report: LdaReport, topic_words_df: pd.DataFrame) -> None:
    print("\nLDA topic modeling report")
    print("-------------------------")
    print(f"Documents used: {report.documents_used}")
    print(f"Vocabulary size: {report.vocabulary_size}")
    print(f"Number of topics: {report.num_topics}")
    print(
        "Configuration note: num_topics=10 was selected after comparison with "
        "8, 12, and 15 topics because it offered the best qualitative "
        "interpretability."
    )

    print("\nTop words per topic")
    print("-------------------")
    for row in topic_words_df.itertuples(index=False):
        print(f"Topic {row.topic_id}: {row.top_words}")

    print("\nDocument count by dominant topic")
    print("--------------------------------")
    for topic_id, count in report.topic_document_counts.items():
        print(f"Topic {topic_id}: {count}")


def main() -> int:
    args = parse_args()

    try:
        input_path = resolve_project_path(args.input)
        topics_output_path = resolve_project_path(args.topics_output)
        topic_words_output_path = resolve_project_path(args.topic_words_output)

        validate_input_path(input_path)

        print(f"Loading CSV: {input_path}")
        df, encoding_used = read_csv_with_encoding_fallback(input_path)
        print(f"Encoding used: {encoding_used}")
        print(f"Available columns: {', '.join(df.columns)}")
        print(f"Initial rows: {len(df)}")

        topics_df, topic_words_df, lda_model, dictionary, corpus, report = run_lda(df)
        save_outputs(
            topics_df,
            topic_words_df,
            lda_model,
            dictionary,
            corpus,
            topics_output_path,
            topic_words_output_path,
        )

        print_final_report(report, topic_words_df)
        print(f"\nSaved topic dataset: {topics_output_path}")
        print(f"Saved topic words: {topic_words_output_path}")
        print(f"Saved model: {DEFAULT_MODEL_PATH}")
        print(f"Saved dictionary: {DEFAULT_DICTIONARY_PATH}")
        print(f"Saved corpus: {DEFAULT_CORPUS_PATH}")

    except FileNotFoundError as exc:
        print(f"File error: {exc}", file=sys.stderr)
        return 1
    except UnicodeDecodeError as exc:
        print(f"Encoding error: {exc}", file=sys.stderr)
        return 1
    except pd.errors.EmptyDataError:
        print("Data validation error: Input CSV is empty.", file=sys.stderr)
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
