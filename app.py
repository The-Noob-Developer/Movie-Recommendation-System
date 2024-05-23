import streamlit as st
import pickle
import pandas as pd
import requests
def fetchPoster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=fd64c62e8fb63031c8792535e5742581&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

def load_data(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# Number of chunks
num_chunks = 11

# Load data from each part
all_data = []
for i in range(num_chunks):
    filename = f'chunk_{i}.pkl'
    part_data = load_data(filename)
    all_data.extend(part_data)

similarity =all_data
st.title("Movie Recommendation System by HRG")
selected_movie_name = st.selectbox('Which movie do you want to get suggestions for?', movies['title'].values)
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster via API
        recommended_movies_posters.append(fetchPoster(movie_id))
    return recommended_movies, recommended_movies_posters
if st.button('Recommend'):
    movies, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movies[0])
        st.image(posters[0])
    with col2:
        st.text(movies[1])
        st.image(posters[1])
    with col3:
        st.text(movies[2])
        st.image(posters[2])
    with col4:
        st.text(movies[3])
        st.image(posters[3])
    with col5:
        st.text(movies[4])
        st.image(posters[4])
