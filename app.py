from flask import Flask, jsonify, request, render_template
from src.recommender import recommend_books

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/recommend", methods=["GET"])
def recommend():
    book_id = request.args.get("book_id", type=int)
    top_n = request.args.get("top_n", default=5, type=int)

    if book_id is None:
        return jsonify({
            "status": "error",
            "message": "book_id is required"
        }), 400

    result = recommend_books(book_id, top_n)

    if result["status"] == "error":
        return jsonify(result), 404

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)