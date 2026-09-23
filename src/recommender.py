import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity


DATA_FILE = "data/clean_books.csv"
TFIDF_MATRIX_FILE = "model/tfidf_matrix.pkl"
BOOK_INDEX_FILE = "model/book_index.pkl"


# Load data and trained model
books = pd.read_csv(DATA_FILE)
tfidf_matrix = joblib.load(TFIDF_MATRIX_FILE)
book_index = joblib.load(BOOK_INDEX_FILE)


def recommend_books(book_id, top_n=5):

    matching_books = books[books["id"] == book_id]

    if matching_books.empty:
        return {
            "status": "error",
            "message": f"Book ID {book_id} not found."
        }

    book_position = matching_books.index[0]

    similarity_scores = cosine_similarity(
        tfidf_matrix[book_position],
        tfidf_matrix
    ).flatten()

    similar_indices = similarity_scores.argsort()[::-1]

    recommendations = []

    for index in similar_indices:

        if index == book_position:
            continue

        recommendations.append({
            "id": int(book_index.iloc[index]["id"]),
            "title": book_index.iloc[index]["title"],
            "author": book_index.iloc[index]["author"],
            "cover_img": book_index.iloc[index]["cover_img"],
            "similarity": round(
                float(similarity_scores[index]),
                4
            )
        })

        if len(recommendations) == top_n:
            break

    return {
        "status": "success",
        "book_id": int(book_id),
        "recommendations": recommendations
    }