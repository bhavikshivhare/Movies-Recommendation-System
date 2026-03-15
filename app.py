import streamlit as st
import nltk
import sklearn
import pandas as pd
import pickle
import joblib

st.title("Movie Recommendation System")

with open('movie.pickle','rb') as m:
    movies = pickle.load(m)

similarities = joblib.load('similarity.joblib')

movies_name = movies['title'].values

def recommend(name_movie):

    movie_index = movies[movies['title']==name_movie].index[0]
    recommendation=similarities[movie_index]
    movie_list = sorted(enumerate(recommendation),reverse=True,key= lambda x:x[1])[1:6]   # sorting to get the movie list has per similarity
    
    recommend_movies = []
    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    
    return recommend_movies
        

name_movie = st.selectbox('Enter the Movie name:',movies_name)

if st.button('Recommed'):
    r = recommend(name_movie)
    st.write('The Recommendated Movies are: ')
    for i in r:
        st.write(i)




