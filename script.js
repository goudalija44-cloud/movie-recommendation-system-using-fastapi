const API_URL = "https://movie-recommendation-api-2671.onrender.com";

const movieInput = document.getElementById("movieInput");
const recommendBtn = document.getElementById("recommendBtn");

const recommendationsContainer =
    document.getElementById("recommendations");

const message =
    document.getElementById("message");

const resultCount =
    document.getElementById("resultCount");


// Button click
recommendBtn.addEventListener("click", getRecommendations);


// Press Enter in the input
movieInput.addEventListener("keydown", function (event) {

    if (event.key === "Enter") {
        getRecommendations();
    }

});


// Get recommendations
async function getRecommendations() {

    // Get movie name INSIDE the function
    const movieName = movieInput.value.trim();

    // Clear previous messages
    message.textContent = "";
    resultCount.textContent = "";


    // Check empty input
    if (!movieName) {

        message.textContent =
            "Please enter a movie name.";

        return;
    }


    // Loading state
    recommendBtn.disabled = true;
    recommendBtn.textContent = "Finding...";


    recommendationsContainer.innerHTML = `
        <div class="loading">
            🎬 Finding movies similar to "${movieName}"...
        </div>
    `;


    try {

        // Call FastAPI
        const response = await fetch(
            `${API_URL}/recommend`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    movie: movieName
                })
            }
        );


        const data = await response.json();


        // Handle API errors
        if (!response.ok) {

            throw new Error(
                data.detail || "Something went wrong."
            );
        }


        // Display recommendations
        displayRecommendations(data);


    } catch (error) {

        recommendationsContainer.innerHTML = `
            <div class="empty-state">

                <div class="empty-icon">⚠️</div>

                <h3>Unable to Get Recommendations</h3>

                <p>${error.message}</p>

            </div>
        `;

    } finally {

        // Reset button
        recommendBtn.disabled = false;
        recommendBtn.textContent = "Recommend";

    }

}


// Display movie recommendations
function displayRecommendations(data) {

    resultCount.textContent =
        `${data.recommendations.length} movies found`;


    recommendationsContainer.innerHTML = "";


    data.recommendations.forEach(
        (movie, index) => {

            const card =
                document.createElement("div");

            card.className = "movie-card";


            // Create genre badges
            const genres =
                movie.genres
                    .map(
                        genre =>
                            `<span class="genre">${genre}</span>`
                    )
                    .join("");


            card.innerHTML = `

                <div class="movie-number">
                    ${index + 1}
                </div>

                <h3>
                    ${movie.title}
                </h3>

                <div class="genres">
                    ${genres}
                </div>

            `;


            recommendationsContainer.appendChild(card);

        }
    );

}