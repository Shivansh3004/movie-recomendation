import pandas as pd

# Dictionary to log feedback
feedback_data = {}

def log_feedback(movie_title, feedback_scores):
    """
    Log user feedback for each recommended movie.
    :param movie_title: Original movie title searched by user
    :param feedback_scores: Dictionary with movie titles and user feedback scores
    """
    global feedback_data
    feedback_data[movie_title] = feedback_scores

def update_recommendations_based_on_feedback(df, feedback_scores, movie_title, threshold=5):
    """
    Update recommendations based on feedback scores. Only movies with ratings below the threshold
    are replaced, while positively rated movies remain in the recommendations list.
    
    :param df: DataFrame containing all movies.
    :param feedback_scores: Dictionary of movie titles and feedback scores.
    :param movie_title: Title of the original movie.
    :param threshold: Minimum score for a movie to remain in recommendations (default is 5).
    :return: Updated recommendations DataFrame.
    """
    # Create a copy of the DataFrame to avoid modifying the original
    df_copy = df.copy()

    # Filter the movies that received positive feedback (above the threshold)
    positively_rated_movies = [movie for movie, score in feedback_scores.items() if score >= threshold]

    # Keep only the positively rated movies in the recommendations
    positive_recommendations = df_copy[df_copy['title'].isin(positively_rated_movies)]

    # Identify movies with negative feedback
    low_feedback_movies = [movie for movie, score in feedback_scores.items() if score < threshold]

    # Filter out low feedback movies from df_copy
    remaining_movies = df_copy[~df_copy['title'].isin(low_feedback_movies + [movie_title])]
    
    # Add additional recommendations to replace the negatively rated ones
    additional_recommendations = remaining_movies.head(len(low_feedback_movies))
    
    # Concatenate the positive recommendations with the additional ones
    updated_recommendations = pd.concat([positive_recommendations, additional_recommendations])

    # Limit the recommendations to the original recommendation count
    return updated_recommendations.head(10)
