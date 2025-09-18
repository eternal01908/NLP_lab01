import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.preprocessing.regex_tokenizer import RegexTokenizer
from src.representations.count_vectorizer import CountVectorizer
from src.core.dataset_loaders import load_raw_text_data

if __name__ == "__main__":
    tokenizer = RegexTokenizer()

    vectorizer = CountVectorizer(tokenizer)

    # -------------------------------
    # Test 1: Corpus mẫu
    # -------------------------------
    corpus = [
        "I love NLP.",
        "I love programming.",
        "NLP is a subfield of AI."
    ]

    vectors = vectorizer.fit_transform(corpus)

    print("\n=== Test with given corpus ===")
    print("--- Vocabulary ---")
    print(vectorizer.vocabulary_)

    print("\n--- Document-Term Matrix ---")
    for vec in vectors:
        print(vec)

    # -------------------------------
    # Test 2: Dataset UD English EWT
    # -------------------------------
    dataset_path = "en_ewt-ud-train.txt"
    raw_text = load_raw_text_data(dataset_path)

    sample_text = raw_text[:500]

    documents = [doc.strip() for doc in sample_text.split(".") if doc.strip()]

    vectors_dataset = vectorizer.fit_transform(documents)

    print("\n=== Test with Dataset UD English EWT ===")
    print("--- Vocabulary (first 30 tokens) ---")
    vocab_items = list(vectorizer.vocabulary_.items())[:30]
    print(dict(vocab_items))

    print("\n--- Document-Term Matrix (first 5 docs) ---")
    for vec in vectors_dataset[:5]:
        print(vec)
