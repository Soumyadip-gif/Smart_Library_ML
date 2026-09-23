import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

INPUT_FILE = "data/clean_books.csv"
MODEL_DIR = "model"

os.makedirs(MODEL_DIR, exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(INPUT_FILE)

print("Loading books...")
print("Total books:", len(df))

# TF-IDF
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=50000,
    ngram_range=(1, 2)
)

print("Training TF-IDF model...")

tfidf_matrix = vectorizer.fit_transform(
    df["combined_text"].fillna("")
)

print("TF-IDF training completed.")
print("Matrix shape:", tfidf_matrix.shape)

# Save vectorizer
joblib.dump(
    vectorizer,
    os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")
)

# Save TF-IDF matrix
joblib.dump(
    tfidf_matrix,
    os.path.join(MODEL_DIR, "tfidf_matrix.pkl")
)

# Save book IDs and indexes
book_index = df[
    ["id", "title", "author", "cover_img"]
].reset_index(drop=True)

joblib.dump(
    book_index,
    os.path.join(MODEL_DIR, "book_index.pkl")
)

print("Model files saved successfully.")