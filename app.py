import streamlit as st
import time
import pandas as pd
import requests


# api =96f4435c3877cc0cc8f5a0e831360ae6
# response = https://api.themoviedb.org/3/movie/{movie_id}?api_key=96f4435c3877cc0cc8f5a0e831360ae6&language=en-US

def fetch_poster(movie_id):
    try:
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=96f4435c3877cc0cc8f5a0e831360ae6&language=en-US'.format(movie_id))
        data = response.json()
        path = "https://image.tmdb.org/t/p/w500/" +data['poster_path']
    except:
        return ('connection error')
    return path




def recommend(movie):
    movie = movie.lower()
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[0:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id)) 
    return recommended_movies,recommended_movies_poster


placeholder = st.empty()
with placeholder.container():
    st.balloons()
time.sleep(1)
placeholder = st.empty()

import pickle
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict) 
st.title("Movie Recommendation System")


similarity = pickle.load(open('similarity.pkl', 'rb'))



selected_movie_name = st.selectbox('Hello.... buddy! \n select your favourite',movies['title'].values)

if st.button('Recommend'):
    name,poster = recommend(selected_movie_name)
    col1, col2, col3,col4,col5,col6 = st.columns(6)

    with col1:
        st.image(poster[0])
        st.text(name[0])
    with col2:
        st.image(poster[1])
        st.text(name[1])
    with col3:
        st.image(poster[2])
        st.text(name[2])
    with col4:
        st.image(poster[3])
        st.text(name[3])
    with col5:
        st.image(poster[4])
        st.text(name[4])
    
    with col6:
        st.image(poster[5])
        st.text(name[5])
    






