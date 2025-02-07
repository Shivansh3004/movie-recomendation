import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from feedback_logger import log_feedback, update_recommendations_based_on_feedback

def recommend_by_content(df):
    # Input from the user
    movie_title = st.text_input("Enter a movie title:").strip()  # Remove leading/trailing whitespace

    # Display available titles for debugging (comment out in production)
    if st.checkbox("Show available titles for debugging"):
        st.write(df['title'].unique())

    # Check if the movie_title exists in the dataset
    if movie_title:  # Proceed only if there is a title entered
        # Normalize the titles in the DataFrame for comparison
        df['normalized_title'] = df['title'].str.strip().str.lower()  # Normalize titles

        # Check for the movie
        if movie_title.lower() not in df['normalized_title'].values:
            st.error("Movie not found in the dataset.")
            return

        # Retrieve the movie overview and genres
        movie_overview = df[df['normalized_title'] == movie_title.lower()]['overview'].values[0]
        movie_genres = df[df['normalized_title'] == movie_title.lower()]['genres'].values[0]

        # Convert the genres string to a list
        movie_genres = [genre.strip() for genre in movie_genres.split(',')]  # Split and strip whitespace

        # Create a copy of the dataframe to avoid modifying the original
        df_copy = df.copy()

        # Fill NaN values in overview and genres with empty strings
        df_copy['overview'] = df_copy['overview'].fillna('')
        df_copy['genres'] = df_copy['genres'].fillna('')

        # Combine overview and genres for TF-IDF
        df_copy['combined'] = df_copy['overview'] + ' ' + df_copy['genres']  # Keep genres as is

        # Create the TF-IDF vectorizer
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(df_copy['combined'])

        # Compute cosine similarity matrix
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        # Get the index of the movie that matches the title
        idx = df_copy.index[df_copy['normalized_title'] == movie_title.lower()].tolist()[0]

        # Get the pairwise similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the top 10 most similar movies
        sim_scores = sim_scores[1:11]  # Exclude the first one (itself)

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Get the recommended movies
        recommended_movies = df_copy.iloc[movie_indices]

        # Exclude the selected movie from the recommendations
        recommended_movies = recommended_movies[recommended_movies['title'] != movie_title]

        # Display recommendations
        if not recommended_movies.empty:
            st.subheader("Recommended Movies:")
            feedback_scores = {}
            for index, row in recommended_movies.iterrows():
                st.write(f"**Title:** {row['title']}")
                st.write(f"**Overview:** {row['overview']}")
                st.image(row['poster_path'], width=200)  # Display the movie poster

                # Add a slider for feedback rating (1-10) under each recommendation
                feedback_score = st.slider(f"Rate this recommendation for '{row['title']}':", 1, 10, 5)
                feedback_scores[row['title']] = feedback_score

            # Log feedback for reinforcement learning
            if st.button("Submit Feedback"):
                log_feedback(movie_title, feedback_scores)
                st.success("Feedback submitted!")

                # Update recommendations based on feedback
                new_recommendations = update_recommendations_based_on_feedback(df_copy, feedback_scores, movie_title)
                
                # Display updated recommendations
                st.subheader("Updated Recommendations Based on Feedback:")
                for index, row in new_recommendations.iterrows():
                    st.write(f"**Title:** {row['title']}")
                    st.write(f"**Overview:** {row['overview']}")
                    st.image(row['poster_path'], width=200)
        else:
            st.write("No similar movies found.")
    else:
        st.warning("Please enter a movie title to get recommendations.")
