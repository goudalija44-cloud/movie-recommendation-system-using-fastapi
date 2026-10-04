# 🎬 CineMatch — Movie Recommendation System Using FastAPI

CineMatch is a machine-learning-based movie recommendation system that recommends movies similar to a user's selected movie.

The project uses **TF-IDF vectorization** and **Cosine Similarity** to identify movies with similar characteristics such as genres, keywords, cast, director, and movie overview.

The trained recommendation components are served through a **FastAPI REST API**, while a simple **HTML, CSS, and JavaScript frontend** provides an interactive user interface.

---

## 🚀 Live Demo

### 🎬 Frontend

[Open CineMatch Movie Recommendation Website](https://goudalija44-cloud.github.io/movie-recommendation-system-using-fastapi/)

### 🔗 FastAPI API

[Open FastAPI API](https://movie-recommendation-api-2671.onrender.com)

### 📚 Swagger API Documentation

[Open Swagger Documentation](https://movie-recommendation-api-2671.onrender.com/docs)

### ❤️ API Health Check

[Check API Health](https://movie-recommendation-api-2671.onrender.com/health?utm_source=chatgpt.com)

### 💻 GitHub Repository

[GitHub Repository](https://github.com/goudalija44-cloud/movie-recommendation-system-using-fastapi?utm_source=chatgpt.com)

---

## 📌 Project Overview

Movie recommendation systems are widely used by platforms such as Netflix, Amazon Prime Video, and other streaming services.

The goal of this project is to build a **content-based movie recommendation system** that recommends movies based on the characteristics of a movie selected by the user.

For example, if the user searches for:

> The Dark Knight

the system returns movies with similar content, such as:

* The Dark Knight Rises
* Batman Begins
* Batman Returns
* Batman Forever
* Batman v Superman: Dawn of Justice

---

## 🎯 Objectives

* Build a content-based movie recommendation system.
* Perform text-based feature engineering.
* Convert movie information into numerical features using TF-IDF.
* Calculate similarity using Cosine Similarity.
* Save trained ML components using Joblib.
* Build a REST API using FastAPI.
* Validate API requests using Pydantic.
* Create a frontend using HTML, CSS, and JavaScript.
* Connect the frontend with the FastAPI backend.
* Deploy the API using Render.

---

## 🧠 Machine Learning Approach

This project uses **content-based filtering**.

The recommendation system compares movies based on their available content rather than user ratings.

### Movie Features Used

The following information is combined to create the movie's textual representation:

* Genres
* Keywords
* Cast
* Director
* Movie Overview

These features are combined into a single `tags` field.

---

## 🔄 Machine Learning Workflow

```text
TMDB Movie Dataset
        ↓
Data Loading
        ↓
Merge Movies + Credits
        ↓
Data Cleaning
        ↓
Feature Extraction
        ↓
Create Movie Tags
        ↓
TF-IDF Vectorization
        ↓
Cosine Similarity
        ↓
Top 5 Similar Movies
        ↓
Save ML Components
        ↓
FastAPI Backend
        ↓
HTML + CSS + JavaScript Frontend
```

---

## 📊 Dataset

The project uses the **TMDB 5000 Movie Dataset**.

The dataset contains movie information such as:

* Movie title
* Genres
* Keywords
* Overview
* Cast
* Crew
* Movie ID

The original dataset consists of:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

After processing, the recommendation system contains approximately **4,803 movies**.

---

## 🛠️ Technologies Used

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* TF-IDF
* Cosine Similarity

### Backend

* FastAPI
* Uvicorn
* Pydantic

### Model Persistence

* Joblib
* PyArrow

### Frontend

* HTML5
* CSS3
* JavaScript

### Deployment

* Render

### Development Tools

* VS Code
* Git
* GitHub
* Swagger UI

---

## 🤖 Recommendation Algorithm

### 1. TF-IDF

TF-IDF converts movie text information into numerical vectors.

```python
tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

tfidf_matrix = tfidf.fit_transform(movies["tags"])
```

### 2. Cosine Similarity

Cosine similarity is used to compare the selected movie with all other movies.

```python
similarity_scores = cosine_similarity(
    tfidf_matrix[movie_index],
    tfidf_matrix
).flatten()
```

The five movies with the highest similarity scores are returned as recommendations.

---

# 🌐 FastAPI Backend

The machine learning recommendation system is exposed through a REST API using FastAPI.

## API Endpoints

| Method | Endpoint      | Description                           |
| ------ | ------------- | ------------------------------------- |
| GET    | `/`           | API welcome message                   |
| GET    | `/test-model` | Checks whether the ML model is loaded |
| GET    | `/movies`     | Returns the available movie list      |
| GET    | `/health`     | Checks API and model health           |
| POST   | `/recommend`  | Returns movie recommendations         |

---

## 🔍 Example API Request

### Endpoint

```text
POST /recommend
```

### Request

```json
{
    "movie": "The Dark Knight"
}
```

### Response

```json
{
    "movie": "The Dark Knight",
    "recommendations": [
        {
            "title": "The Dark Knight Rises",
            "genres": [
                "Action",
                "Crime",
                "Drama",
                "Thriller"
            ]
        },
        {
            "title": "Batman Begins",
            "genres": [
                "Action",
                "Crime",
                "Drama"
            ]
        },
        {
            "title": "Batman Returns",
            "genres": [
                "Action",
                "Fantasy"
            ]
        },
        {
            "title": "Batman Forever",
            "genres": [
                "Action",
                "Crime",
                "Fantasy"
            ]
        },
        {
            "title": "Batman v Superman: Dawn of Justice",
            "genres": [
                "Action",
                "Adventure",
                "Fantasy"
            ]
        }
    ]
}
```

---

# 🎨 Frontend

The project includes a simple responsive frontend built using:

* HTML
* CSS
* JavaScript

The frontend communicates with the deployed FastAPI backend using the JavaScript `fetch()` API.

### Frontend flow

```text
User enters movie name
        ↓
JavaScript sends POST request
        ↓
FastAPI /recommend endpoint
        ↓
TF-IDF + Cosine Similarity
        ↓
FastAPI returns JSON
        ↓
JavaScript processes response
        ↓
Movie recommendation cards displayed
```

---

## 📁 Project Structure

```text
movie-recommendation-system-using-fastapi/
├── index.html
├── style.css
├── script.js
│
├── models/
├── app.py
├── test_api.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 💾 Saved Machine Learning Components

The trained recommendation components are saved using Joblib.

### `movies.pkl`

Contains the processed movie DataFrame.

### `tfidf_vectorizer.pkl`

Contains the trained TF-IDF vectorizer.

### `tfidf_matrix.pkl`

Contains the TF-IDF representation of the movie tags.

These files allow the FastAPI application to load the already-trained components without retraining the model every time the API starts.

---

# 🖥️ Run the Project Locally

## 1. Clone the repository

```bash
git clone https://github.com/goudalija44-cloud/movie-recommendation-system-using-fastapi.git
```

```bash
cd movie-recommendation-system-using-fastapi
```

---

## 2. Install dependencies

```bash
py -m pip install -r requirements.txt
```

---

## 3. Start FastAPI

```bash
py -m uvicorn app:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

---

## 4. Open Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test the API directly from the browser.

---

# 🌐 Run the Frontend Locally

Open another terminal in the project folder and run:

```bash
py -m http.server 5500 --directory frontend
```

Then open:

```text
http://127.0.0.1:5500
```

The frontend sends requests to the deployed FastAPI backend.

---

# 🧪 API Testing

The project includes `test_api.py` for testing the recommendation endpoint.

Run:

```bash
py test_api.py
```

Example:

```text
Status Code: 200
Response:
{
    "movie": "The Dark Knight",
    "recommendations": [...]
}
```

---

# ☁️ Deployment

The FastAPI backend is deployed using Render.

### Production API

```text
https://movie-recommendation-api-2671.onrender.com
```

### Production API Documentation

```text
https://movie-recommendation-api-2671.onrender.com/docs
```

The application uses the following Render start command:

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

---

# 🔐 API Keys

This project **does not require an API key**.

The recommendation system works using locally saved machine learning components:

* `movies.pkl`
* `tfidf_matrix.pkl`
* `tfidf_vectorizer.pkl`

No external movie API is called during recommendation.

---

# ✨ Key Features

* 🎬 Content-based movie recommendations
* 🧠 TF-IDF text vectorization
* 📐 Cosine similarity
* 🔎 Case-insensitive movie search
* ⭐ Top 5 recommendations
* 🌐 FastAPI REST API
* 📋 Pydantic request validation
* 📚 Swagger API documentation
* 🎨 HTML/CSS/JavaScript frontend
* 🔗 Frontend and backend integration
* ☁️ Render deployment
* ❤️ API health monitoring

---

# 📚 What I Learned

Through this project, I learned how to:

* Work with real-world movie datasets.
* Perform data preprocessing.
* Extract useful features from text data.
* Build a content-based recommendation system.
* Use TF-IDF for text representation.
* Calculate Cosine Similarity.
* Save and load ML components using Joblib.
* Build REST APIs using FastAPI.
* Create API request and response schemas using Pydantic.
* Test APIs using Swagger and Python Requests.
* Connect JavaScript frontend applications with REST APIs.
* Configure CORS for frontend-backend communication.
* Deploy a machine learning API using Render.
* Organize an ML project for GitHub.

---

# 🔮 Future Improvements

Possible future improvements include:

* Add movie posters using a movie API.
* Add movie descriptions and release dates.
* Add recommendation similarity scores.
* Improve recommendation quality using additional features.
* Add user-based recommendations.
* Add collaborative filtering.
* Add a database for storing user preferences.
* Add user accounts and personalized recommendations.
* Deploy the frontend publicly.
* Add automated testing and CI/CD.

---

# 📜 License

This project is created for educational and portfolio purposes.

---

## 👤 Project

**CineMatch — Movie Recommendation System**

Built using:

```text
Python + Scikit-learn + FastAPI + HTML + CSS + JavaScript
```
