import pandas as pd
import re

INPUT_FILE = "data/library_books.csv"
OUTPUT_FILE = "data/clean_books.csv"


# Load dataset
df = pd.read_csv(INPUT_FILE)

print("Original dataset shape:", df.shape)


# Keep only the columns needed for recommendation
required_columns = [
    "id",
    "title",
    "author",
    "primary_author",
    "description",
    "genres",
    "series",
    "language",
    "cover_img"
]

df = df[required_columns].copy()


# Fill missing text values
text_columns = [
    "author",
    "primary_author",
    "description",
    "genres",
    "series",
    "language"
]

for column in text_columns:
    df[column] = df[column].fillna("")


# Fill missing cover image URLs
df["cover_img"] = df["cover_img"].fillna("")


# Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


for column in text_columns + ["title"]:
    df[column] = df[column].apply(clean_text)


# Remove rows with empty titles
df = df[df["title"].str.strip() != ""]


# Remove duplicate book IDs
df = df.drop_duplicates(subset="id")


# Combine useful information for NLP
df["combined_text"] = (
    df["title"] + " " +
    df["author"] + " " +
    df["primary_author"] + " " +
    df["genres"] + " " +
    df["description"] + " " +
    df["series"] + " " +
    df["language"]
)


# Save cleaned dataset
df.to_csv(OUTPUT_FILE, index=False)


print("Cleaned dataset shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Saved to:", OUTPUT_FILE)
print("Data preparation completed successfully.")