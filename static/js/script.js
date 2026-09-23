const recommendBtn = document.getElementById("recommendBtn");
const bookIdInput = document.getElementById("bookId");
const recommendationsContainer =
    document.getElementById("recommendations");
const message = document.getElementById("message");

recommendBtn.addEventListener("click", getRecommendations);


async function getRecommendations() {

    const bookId = bookIdInput.value.trim();

    if (!bookId) {
        message.textContent = "Please enter a Book ID.";
        recommendationsContainer.innerHTML = "";
        return;
    }

    message.textContent = "Finding recommendations...";
    recommendationsContainer.innerHTML = "";

    try {

        const response = await fetch(
            `/api/recommend?book_id=${bookId}&top_n=5`
        );

        const data = await response.json();

        if (!response.ok || data.status === "error") {
            message.textContent =
                data.message || "Unable to find recommendations.";
            return;
        }

        message.textContent =
            `Found ${data.recommendations.length} recommendations.`;

        displayRecommendations(data.recommendations);

    } catch (error) {

        console.error(error);

        message.textContent =
            "Unable to connect to the recommendation server.";
    }
}


function displayRecommendations(books) {

    recommendationsContainer.innerHTML = "";

    books.forEach((book, index) => {

        const card = document.createElement("div");

        card.className = "book-card";

        const coverImage = book.cover_img
            ? `
                <img
                    src="${escapeHTML(book.cover_img)}"
                    alt="${escapeHTML(book.title)} cover"
                    class="book-cover-image"
                    loading="lazy"
                    onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';"
                >
                <div class="no-cover" style="display: none;">
                    No Cover Available
                </div>
              `
            : `
                <div class="no-cover">
                    No Cover Available
                </div>
              `;

        card.innerHTML = `

            <div class="book-cover">
                ${coverImage}
            </div>

            <div class="book-number">
                Recommendation #${index + 1}
            </div>

            <h3>${escapeHTML(book.title)}</h3>

            <div class="book-info">
                Book ID: ${book.id}
            </div>

            <div class="book-info">
                Author: ${escapeHTML(book.author || "Unknown")}
            </div>

            
        `;

        recommendationsContainer.appendChild(card);
    });
}


function escapeHTML(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}