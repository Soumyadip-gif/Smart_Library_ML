# Smart Library - ML Book Recommendation System

An AI-powered book recommendation system built using Python, Flask, NLP, and Machine Learning.

The system takes a Book ID and recommends 5 similar books using TF-IDF and Cosine Similarity.

## Features

- Book recommendation using Machine Learning
- TF-IDF based text representation
- Cosine Similarity
- Top 5 book recommendations
- Book cover images
- Flask REST API
- Interactive web interface
- Glassmorphism UI
- Smooth animations
- Responsive design
- Original book IDs are preserved

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- HTML
- CSS
- JavaScript
- NLP
- TF-IDF
- Cosine Similarity

## How It Works

1. The book dataset is cleaned and prepared.
2. Book information such as title, author, genres, description, series, and language is combined.
3. TF-IDF converts the book text into numerical vectors.
4. Cosine Similarity compares the selected book with other books.
5. The books are ranked according to similarity.
6. The top 5 books are returned as recommendations.

## Project Structure

```text
Smart-Library-ML/
│
├── data/
│   └── clean_books.csv
│
├── model/
│   ├── tfidf_vectorizer.pkl
│   ├── tfidf_matrix.pkl
│   └── book_index.pkl
│
├── src/
│   └── recommender.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── prepare_data.py
├── train_model.py
├── test_recommender.py
├── requirements.txt
├── .gitignore
└── README.md