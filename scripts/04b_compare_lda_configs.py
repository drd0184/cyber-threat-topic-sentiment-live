"""
Compare multiple LDA topic-count configurations on cyber-relevant text.

Only text_clean is used as the modeling feature. original_type, annotation, and
relevant are preserved and summarized only after topic assignment as qualitative
ex post checks.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

try:
    from gensim import corpora
    from gensim.models import LdaModel
except ImportError as exc:
    corpora = None
    LdaModel = None
    GENSIM_IMPORT_ERROR = exc
else:
    GENSIM_IMPORT_ERROR = None


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
DEFAULT_INPUT_PATH = PROCESSED_DIR / "03b_cyber_relevant_dataset.csv"
DEFAULT_OUTPUT_PATH = PROCESSED_DIR / "04b_lda_config_comparison.csv"

REQUIRED_COLUMNS = {"text_clean"}
ENCODINGS_TO_TRY = ("utf-8", "utf-8-sig", "cp1252", "latin1")

NUM_TOPICS_OPTIONS = [8, 10, 12, 15]
NO_BELOW = 5
NO_ABOVE = 0.5
RANDOM_STATE = 42
PASSES = 10
ITERATIONS = 100
TOP_WORDS_COUNT = 10


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare gensim LDA configurations with different topic counts."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="Path to the cyber-relevant preprocessed CSV.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Path where the comparison CSV will be saved.",
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


def prepare_modeling_data(df: pd.DataFrame) -> tuple[pd.DataFrame, list[list[str]]]:
    modeling_df = df.copy()
    modeling_df["text_clean"] = modeling_df["text_clean"].astype("string").fillna("").str.strip()
    modeling_df = modeling_df.loc[modeling_df["text_clean"] != ""].reset_index(drop=True)

    tokenized_texts = [text.split() for text in modeling_df["text_clean"]]
    if not tokenized_texts:
        raise ValueError("Corpus is empty: no tokens found in text_clean.")

    return modeling_df, tokenized_texts


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


def train_lda_model(corpus, dictionary, num_topics: int):
    return LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        random_state=RANDOM_STATE,
        passes=PASSES,
        iterations=ITERATIONS,
        alpha="auto",
        eta="auto",
    )


def get_dominant_topic(lda_model, doc_bow) -> int:
    topic_distribution = lda_model.get_document_topics(doc_bow, minimum_probability=0.0)
    topic_id, _ = max(topic_distribution, key=lambda item: item[1])
    return int(topic_id)


def top_words_for_topic(lda_model, topic_id: int) -> str:
    words = [word for word, _ in lda_model.show_topic(topic_id, topn=TOP_WORDS_COUNT)]
    return ", ".join(words)


def dominant_ex_post_value(topic_df: pd.DataFrame, column: str) -> str:
    if column not in topic_df.columns:
        return ""

    counts = topic_df[column].dropna().astype(str).value_counts()
    if counts.empty:
        return ""

    return str(counts.index[0])


def compare_configs(df: pd.DataFrame) -> pd.DataFrame:
    validate_columns(df)
    ensure_gensim_available()

    modeling_df, tokenized_texts = prepare_modeling_data(df)
    dictionary, corpus, used_positions = build_dictionary_and_corpus(tokenized_texts)
    used_df = modeling_df.iloc[used_positions].reset_index(drop=True)
    total_docs = len(used_df)

    comparison_rows = []
    for num_topics in NUM_TOPICS_OPTIONS:
        print(f"\nTraining LDA with num_topics={num_topics}")
        lda_model = train_lda_model(corpus, dictionary, num_topics)

        assigned_topics = [get_dominant_topic(lda_model, doc_bow) for doc_bow in corpus]
        assigned_df = used_df.copy()
        assigned_df["dominant_topic"] = assigned_topics

        print(f"Topics for num_topics={num_topics}")
        print("-" * (22 + len(str(num_topics))))
        for topic_id in range(num_topics):
            topic_df = assigned_df.loc[assigned_df["dominant_topic"] == topic_id]
            docs_assigned = len(topic_df)
            top_words = top_words_for_topic(lda_model, topic_id)

            comparison_rows.append(
                {
                    "num_topics": num_topics,
                    "topic_id": topic_id,
                    "top_words": top_words,
                    "docs_assigned": docs_assigned,
                    "percent_docs": docs_assigned / total_docs * 100,
                    "dominant_original_type_ex_post": dominant_ex_post_value(
                        topic_df, "original_type"
                    ),
                    "dominant_annotation_ex_post": dominant_ex_post_value(
                        topic_df, "annotation"
                    ),
                }
            )

            print(
                f"Topic {topic_id}: {top_words} "
                f"({docs_assigned} docs, {docs_assigned / total_docs * 100:.2f}%)"
            )

    return pd.DataFrame(comparison_rows)


def main() -> int:
    args = parse_args()

    try:
        input_path = resolve_project_path(args.input)
        output_path = resolve_project_path(args.output)

        validate_input_path(input_path)

        print(f"Loading CSV: {input_path}")
        df, encoding_used = read_csv_with_encoding_fallback(input_path)
        print(f"Encoding used: {encoding_used}")
        print(f"Available columns: {', '.join(df.columns)}")
        print(f"Initial rows: {len(df)}")

        comparison_df = compare_configs(df)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        comparison_df.to_csv(output_path, index=False)
        print(f"\nSaved comparison table: {output_path}")

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
