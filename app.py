from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import joblib
from sklearn.metrics.pairwise import cosine_similarity


app = FastAPI(
    title="CineMatch Movie Recommendation API",
    description="Movie recommendation API using TF-IDF and Cosine Similarity.",
    version="1.0.0"
)


# Load saved ML components
movies = joblib.load("models/movies.pkl")
tfidf_matrix = joblib.load("models/tfidf_matrix.pkl")


# Request format
class MovieRequest(BaseModel):
    movie: str

class MovieRecommendation(BaseModel):
    title: str
    genres: List[str]


class RecommendationResponse(BaseModel):
    movie: str
    recommendations: List[MovieRecommendation]    


@app.get("/")
def home():
    return {
        "message": "Welcome to CineMatch Movie Recommendation API!",
        "status": "running"
    }


@app.get("/test-model")
def test_model():
    return {
        "message": "Movie recommendation model loaded successfully!",
        "number_of_movies": len(movies)
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "api": "running",
        "model": "loaded"
    }

@app.get("/movies")
def get_movies():
    movie_list = movies["title"].tolist()

    return {
        "total_movies": len(movie_list),
        "movies": movie_list
    }

@app.post("/recommend", response_model=RecommendationResponse)
def recommend_movie(request: MovieRequest):

    movie_name = request.movie.strip()

    # Check for empty input
    if not movie_name:
        raise HTTPException(
            status_code=400,
            detail="Movie name cannot be empty."
        )

    # Find movie index
    movie_indices = movies.index[
        movies["title"].str.lower() == movie_name.lower()
    ].tolist()

    # Movie not found
    if not movie_indices:
        raise HTTPException(
            status_code=404,
            detail=f"Movie '{movie_name}' not found."
        )

    movie_index = movie_indices[0]

    # Calculate similarity
    similarity_scores = cosine_similarity(
        tfidf_matrix[movie_index],
        tfidf_matrix
    ).flatten()

    # Ignore the selected movie itself
    similarity_scores[movie_index] = -1

    # Get top 5 recommendations
    recommended_indices = similarity_scores.argsort()[-5:][::-1]

    recommendations = []

    for index in recommended_indices:
        recommendations.append({
            "title": movies.iloc[index]["title"],
            "genres": movies.iloc[index]["genres"]
        })

    return {
        "movie": movies.iloc[movie_index]["title"],
        "recommendations": recommendations
    }