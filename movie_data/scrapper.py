# We thought of giving you a gift this new year by sharing the web scraping script
# Understanding the script before using is always appreciated
# We left few blanks in the script for your exploration
# Make sure to replace FILL_IN_THE_BLANK in the code to make it work

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def scrapper(imdbId):
    # Ensure the IMDb ID is correctly formatted
    if not str(imdbId).startswith('tt'):
        print(f"Invalid IMDb ID format: {imdbId}")
        return np.nan
    
    # Extract the numeric part of the IMDb ID
    id = str(imdbId)[2:]
    n_zeroes = 7 - len(id)
    new_id = "0" * n_zeroes + id
    URL = f"https://www.imdb.com/title/tt{new_id}/"
    request_header = {
        'Content-Type': 'text/html; charset=UTF-8', 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0', 
        'Accept-Encoding': 'gzip, deflate, br'
    }
    
    try:
        response = requests.get(URL, headers=request_header)
        response.raise_for_status()  # Check for HTTP errors
    except requests.HTTPError as http_err:
        if response.status_code == 404:
            print(f"IMDb ID not found: {imdbId}")
        else:
            print(f"HTTP error occurred: {http_err}")
        return np.nan
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return np.nan

    soup = BeautifulSoup(response.text, 'html.parser')

    # Example of finding the IMDb rating element
    imdb_rating = soup.find('span', {'itemprop': 'ratingValue'})
    
    if imdb_rating:
        return imdb_rating.text.strip()
    else:
        return np.nan

# Example usage
imdb_ids = ['tt114709', 'tt113497', 'tt113228']
for imdb_id in imdb_ids:
    rating = scrapper(imdb_id)
    print(f"IMDb ID: {imdb_id}, Rating: {rating}")

# Load the necessary CSV files
movies_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\movies.csv')
ratings_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\ratings.csv')

# Group by movieId and calculate the count and mean of ratings
ratings_grouped = ratings_df.groupby('movieId').agg(
    rating_count=('rating', 'count'),
    average_rating=('rating', 'mean')
).reset_index()

# Filter movies with more than 50 ratings
ratings_filtered = ratings_grouped[ratings_grouped['rating_count'] > 50]

# Join with the movies dataframe to get movie titles
movies_filtered = pd.merge(movies_df, ratings_filtered, on='movieId')

# Display the resulting dataframe
print(movies_filtered.head())

# Find the movie with the highest average rating
highest_rated_movie = movies_filtered.loc[movies_filtered['average_rating'].idxmax()]
print(f"The movie with the highest IMDB rating is movieId {highest_rated_movie['movieId']}")

# Filter Sci-Fi movies
sci_fi_movies = movies_filtered[movies_filtered['genres'].str.contains('Sci-Fi')]

# Find the Sci-Fi movie with the highest average rating
highest_rated_sci_fi_movie = sci_fi_movies.loc[sci_fi_movies['average_rating'].idxmax()]
print(f"The Sci-Fi movie with the highest IMDB rating is movieId {highest_rated_sci_fi_movie['movieId']}")
