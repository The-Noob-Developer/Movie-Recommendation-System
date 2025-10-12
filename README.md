# Content-Based Movie Recommendation System

A simple yet effective movie recommendation system that suggests movies based on their content (genres, keywords, cast, crew, etc.). This project is built using Python, Pandas, and Scikit-learn, with an interactive web interface created using Streamlit.

**✨ Live Demo:** [**https://hrg-movie-recommendation-system.streamlit.app/**](https://hrg-movie-recommendation-system.streamlit.app/)

**📂 GitHub Repository:** [**https://github.com/The-Noob-Developer/Movie-Recommendation-System**](https://github.com/The-Noob-Developer/Movie-Recommendation-System)



***

## 📋 Table of Contents
* [About The Project](#about-the-project)
* [How It Works](#how-it-works)
* [Tech Stack](#tech-stack)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Dataset](#dataset)

***

## 📖 About The Project

In an era of abundant digital content, finding the right movie to watch can be overwhelming. This project aims to solve that problem by providing users with personalized movie recommendations.

Unlike collaborative filtering systems that rely on user ratings, this is a **content-based filtering** system. It analyzes the intrinsic properties of movies—such as the plot summary, genres, main actors, and director—to find and recommend other movies with similar content.

The core idea is simple: **If you liked a particular movie, you might also like other movies that share similar characteristics.**

***

## 🧠 How It Works

The recommendation engine is built through a series of data processing and machine learning steps:

1.  **Data Loading and Merging**: The system starts by loading two datasets from TMDb: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`. These are merged into a single dataframe based on the movie title.

2.  **Data Cleaning and Preprocessing**:
    * **Feature Selection**: Only relevant columns (`movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`) are kept for the model.
    * **Parsing**: The stringified JSON in `genres`, `keywords`, `cast`, and `crew` is parsed to extract meaningful information. For instance, it extracts the top 3 actors from the cast and the director's name from the crew.
    * **Consolidation**: All extracted features (overview, genres, keywords, cast, and crew) are combined into a single text block for each movie, called `tags`.
    * **Text Normalization**: To ensure that names like "Sam Worthington" and "Sam Mendes" are treated as unique entities, spaces within them are removed (e.g., "SamWorthington", "SamMendes").

3.  **Vectorization**:
    * The textual `tags` for all movies are converted into numerical vectors using the **Bag of Words** technique via Scikit-learn's `CountVectorizer`.
    * This process creates a large matrix where each row represents a movie and each column represents a word from the corpus of all tags. The value in each cell is the frequency of that word in that movie's tags.

4.  **Similarity Calculation**:
    * **Cosine Similarity** is used to calculate the similarity between every pair of movie vectors. This metric measures the cosine of the angle between two vectors, where a value closer to 1 indicates higher similarity.
    * This results in a similarity matrix where each movie has a similarity score with every other movie.

5.  **Recommendation Function**:
    * When a user selects a movie, the system finds its index in the similarity matrix.
    * It then retrieves the similarity scores of this movie with all other movies and sorts them in descending order.
    * The top 5 most similar movies (excluding the movie itself) are returned as recommendations.

6.  **Web Application & Deployment**:
    * The final movie data and the similarity matrix are saved as pickle files (`.pkl`) for efficient loading.
    * A user-friendly web interface is built using **Streamlit**.
    * The application uses the **TMDb API** to fetch and display the official movie posters for a rich user experience.

***

## 🛠️ Tech Stack

* **Python**: Core programming language.
* **Pandas**: For data manipulation and analysis.
* **NumPy**: For numerical operations.
* **Scikit-learn**: For machine learning, specifically `CountVectorizer` and `cosine_similarity`.
* **Streamlit**: To create and deploy the interactive web application.
* **Requests**: To make API calls to TMDb for fetching movie posters.
* **Pickle**: For serializing and saving the trained model/data.

***

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.7+
* pip package manager

### Installation

1.  **Clone the repository:**
    ```sh
    
    git clone https://github.com/The-Noob-Developer/Movie-Recommendation-System.git
    cd Movie-Recommendation-System
    ```

2.  **Create a `requirements.txt` file and install the dependencies:**
    Create a file named `requirements.txt` with the following content:
    ```
    pandas
    numpy
    scikit-learn
    streamlit
    requests
    ```
    Then, install the packages:
    ```sh
    pip install -r requirements.txt
    ```

3.  **Get a TMDb API Key:**
    * Create an account on [The Movie Database (TMDb)](https://www.themoviedb.org/).
    * Go to your account settings, find the "API" section, and generate a new API key.
    * Copy this key and paste it into the `fetchPoster` function in your Streamlit app file (`app.py`):
        ```python
        # In app.py
        def fetchPoster(movie_id):
            response = requests.get('[https://api.themoviedb.org/3/movie/](https://api.themoviedb.org/3/movie/){}?api_key=YOUR_API_KEY_HERE&language=en-US'.format(movie_id))
            # ...
        ```

4.  **Download the Dataset:**
    * Download the dataset from [Kaggle: TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
    * Place `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` in the root directory of the project.

***

## 💻 Usage

1.  **Generate the Model Files**:
    Run the Jupyter Notebook or Python script that performs the data processing and calculates the similarity matrix. This will generate two essential files:
    * `movie_dict.pkl`: A dictionary containing movie IDs and titles.
    * `similarity.pkl`: The cosine similarity matrix.

2.  **Run the Streamlit App**:
    In your terminal, run the following command:
    ```sh
    streamlit run app.py
    ```

3.  **Interact with the App**:
    * Open your web browser and go to the local URL provided by Streamlit (usually `http://localhost:8501`).
    * Select a movie from the dropdown list.
    * Click the "Recommend" button to see the top 5 movie recommendations with their posters.

***

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset** available on Kaggle. It contains metadata for about 5,000 movies from The Movie Database (TMDb), including cast, crew, keywords, budget, revenue, genres, and more.
