from src.recommender import recommend_books


# Test with The Hunger Games
result = recommend_books(1, top_n=5)


print("\nRecommendation Result")
print("=====================")

print("Status:", result["status"])

if result["status"] == "success":

    print("Selected Book ID:", result["book_id"])

    print("\nRecommended Books:")

    for i, book in enumerate(result["recommendations"], start=1):

        print(
            f"{i}. {book['title']} "
            f"(ID: {book['id']}, "
            f"Similarity: {book['similarity']})"
        )

else:
    print(result["message"])