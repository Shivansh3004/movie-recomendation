# Movie Recommendation System

This is a **Movie Recommendation System** built using **Streamlit** and **Machine Learning** techniques, including **TF-IDF vectorization, Cosine Similarity, and Reinforcement Learning** for content-based recommendations. It also features **sentiment-based recommendations** using user moods and an API for fetching reviews.

## Features

- **Search Movie**: Search for movies by title.
- **Recommend by Genre**: Get recommendations based on selected genres.
- **Recommend by Mood**: Enter a mood (e.g., happy, sad) to get movie suggestions based on sentiment analysis of reviews.
- **Content-Based Recommendations**: Suggests movies based on TF-IDF and Reinforcement Learning.
- **Sentiment-Based Recommendations**: Uses external APIs to analyze user moods and recommend movies accordingly.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python (Pandas, Scikit-learn, Numpy, OpenAI Gym for RL)
- **Machine Learning**: TF-IDF Vectorization, Cosine Similarity, Reinforcement Learning
- **External API**: For fetching movie reviews

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Dataset

The project uses a filtered version of the **TMDb 1 Million Dataset**. The dataset includes:
- Movie title, genres, overview, popularity, and poster path.
- Sentiment-based recommendations use external movie reviews via API.

## Reinforcement Learning in Content-Based Recommendations

- A **Q-learning algorithm** is used to refine content-based recommendations.
- User interactions (clicks, likes) update the **Q-table** to improve suggestions over time.

## Sentiment Analysis

- User enters a mood (e.g., happy, sad, excited), and the system fetches recent reviews via an API.
- Reviews are analyzed using **TextBlob** or **VADER**.
- Recommended movies are filtered based on the dominant sentiment.

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make changes and commit:
   ```bash
   git commit -m "Added a new feature"
   ```
4. Push changes:
   ```bash
   git push origin feature-branch
   ```
5. Open a Pull Request.

## Future Enhancements

- **Graph Neural Networks (GNNs)** for improved content-based recommendations.
- **User-based Collaborative Filtering** using deep learning.
- **Improved Reinforcement Learning Model** to better adapt to user behavior.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Contact

For queries, contact [shivanshgandotra@gmail.com] or open an issue in the repository.

