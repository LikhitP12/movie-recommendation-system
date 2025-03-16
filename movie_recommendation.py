import streamlit as st
import pandas as pd
import sqlite3
import random

# Database setup for user authentication, reviews, and recommendation feedback
conn = sqlite3.connect("user_data.db", check_same_thread=False)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
c.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    movie TEXT,
    rating INTEGER,
    review TEXT
)
""")
c.execute("""
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    recommendation_rating INTEGER,
    disliked_movies TEXT
)
""")
c.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    searched_movie TEXT,
    recommended_movies TEXT
)
""")
conn.commit()

# Load movie dataset
movies_df = pd.read_csv("movies.csv")
movies_df["genres"] = movies_df["genres"].apply(lambda x: x.split('|'))

def register_user(username, password):
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except:
        return False

def authenticate_user(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone()

def get_recommendations(movie_title, disliked_movies=[]):
    matched_movies = movies_df[movies_df["title"].str.contains(movie_title, case=False, na=False)]
    matched_movies = matched_movies[~matched_movies["title"].isin(disliked_movies)]
    return matched_movies.sample(n=min(10, len(matched_movies))) if not matched_movies.empty else pd.DataFrame()

def get_sequels(movie_title):
    sequels = movies_df[movies_df["title"].str.contains(movie_title, case=False, na=False)]
    return sequels.sample(n=min(5, len(sequels)), replace=False) if not sequels.empty else pd.DataFrame()

def save_history(username, movie_title, recommended_movies):
    c.execute("INSERT INTO history (username, searched_movie, recommended_movies) VALUES (?, ?, ?)", 
              (username, movie_title, ", ".join(recommended_movies)))
    conn.commit()

def get_history(username):
    c.execute("SELECT searched_movie, recommended_movies FROM history WHERE username=?", (username,))
    return c.fetchall()

# Streamlit UI
st.set_page_config(page_title="Movie Recommendation System", layout="wide")
st.title("🎬 Movie Recommendation System")
st.sidebar.title("🔑 User Authentication")

menu = st.sidebar.selectbox("Menu", ["Login", "Sign Up", "Home", "History", "Logout"])

if menu == "Sign Up":
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Register"):
        if register_user(username, password):
            st.sidebar.success("Registered Successfully! Please Login.")
        else:
            st.sidebar.error("Username already exists!")

if menu == "Login":
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        user = authenticate_user(username, password)
        if user:
            st.session_state["user"] = username
            st.sidebar.success(f"Welcome {username}!")
        else:
            st.sidebar.error("Invalid Credentials")

if menu == "Home" and "user" in st.session_state:
    movie_input = st.text_input("Enter your favorite movie:")
    if "rec_rating" not in st.session_state:
        st.session_state["rec_rating"] = 3
    if "disliked_movies" not in st.session_state:
        st.session_state["disliked_movies"] = []

    if st.button("Get Recommendations") or "recommendations" in st.session_state:
        recommendations = get_recommendations(movie_input, st.session_state["disliked_movies"])
        st.session_state["recommendations"] = recommendations if not recommendations.empty else None
        if "user" in st.session_state:
            save_history(st.session_state["user"], movie_input, recommendations["title"].tolist())
        
    if "recommendations" in st.session_state and st.session_state["recommendations"] is not None:
        displayed_movies = []
        for _, row in st.session_state["recommendations"].iterrows():
            displayed_movies.append(row["title"])
            st.subheader(row["title"])
            st.write(f"**Genres:** {', '.join(row['genres'])}")

        # Sequel Recommendations
        st.write("## Sequel Recommendations:")
        sequels = get_sequels(movie_input)
        for _, row in sequels.iterrows():
            st.write(f"- {row['title']}")

        # Feedback on Recommendations
        st.write("## Rate the Recommendations:")
        rec_rating = st.selectbox("How good were the recommendations?", [1, 2, 3, 4, 5], index=st.session_state["rec_rating"]-1, key="rec_rating")
        disliked_movies = st.multiselect("Which movies did you not prefer?", displayed_movies, key="disliked_movies")

        if st.button("Submit Feedback"):
            if "rec_rating" in st.session_state and rec_rating != st.session_state["rec_rating"]:
                st.session_state["rec_rating"] = rec_rating
            if "disliked_movies" in st.session_state and disliked_movies != st.session_state["disliked_movies"]:
                st.session_state["disliked_movies"] = disliked_movies
            if rec_rating >= 4:
                st.success("Great! We'll keep suggesting similar movies.")
            elif rec_rating == 3:
                st.warning("We'll tweak some suggestions to improve recommendations.")
            else:
                st.error("We'll completely change the recommendations next time!")
                st.session_state["recommendations"] = get_recommendations(movie_input, disliked_movies)

if menu == "History" and "user" in st.session_state:
    st.write("## Search History")
    history = get_history(st.session_state["user"])
    for search in history:
        st.write(f"Movie: {search[0]} - Recommended: {search[1]}")

if menu == "Logout":
    st.session_state.clear()
    st.sidebar.success("Logged out successfully!")

# Footer
st.sidebar.write("Developed by **Peethala V Siva Sampath Likhit**")
st.sidebar.write("Roll No: 2024028407, MTech CSE")
