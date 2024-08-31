#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install pandas')


# In[5]:


# Import necessary libraries
import pandas as pd

# Load the CSV files
links_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\links.csv')
movies_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\movies.csv')
ratings_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\ratings.csv')
tags_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\tags.csv')

# Display the shape of each dataframe
print("Shape of links.csv:", links_df.shape)
print("Shape of movies.csv:", movies_df.shape)
print("Shape of ratings.csv:", ratings_df.shape)
print("Shape of tags.csv:", tags_df.shape)

# Check the first few rows of movies.csv to understand its structure
print("\nFirst few rows of movies.csv:")
print(movies_df.head())

# Additional details about the 'movies.csv'
print("\nDetails of movies.csv:")
print(movies_df.info())



# In[6]:


import pandas as pd

# Load the movies.csv file from an absolute path
movies_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\movies.csv')

# Display the shape of the movies dataframe
print("Shape of movies.csv:", movies_df.shape)


# In[7]:


import pandas as pd

# Load the ratings.csv file
ratings_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\ratings.csv')

# Display the shape of the ratings dataframe
print("Shape of ratings.csv:", ratings_df.shape)


# In[8]:


import pandas as pd

# Load the ratings.csv file
ratings_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\ratings.csv')

# Get the number of unique userId values
unique_user_ids = ratings_df['userId'].nunique()

print("Number of unique userId in ratings.csv:", unique_user_ids)


# In[9]:


import pandas as pd

# Load the necessary CSV files
movies_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\movies.csv')
ratings_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\ratings.csv')

# Count the number of ratings for each movieId
ratings_count = ratings_df['movieId'].value_counts()

# Find the movieId with the maximum number of ratings
most_rated_movie_id = ratings_count.idxmax()

# Get the title of the movie with the maximum number of ratings
most_rated_movie_title = movies_df[movies_df['movieId'] == most_rated_movie_id]['title'].values[0]

print("The movie with the maximum number of user ratings is:", most_rated_movie_title)


# In[11]:


# Display the first few rows of the movies DataFrame to check titles
print(movies_df.head(10))



# In[12]:


# Search for titles containing 'Matrix'
matrix_titles = movies_df[movies_df['title'].str.contains('Matrix', case=False, na=False)]
print("Matching titles:", matrix_titles)


# In[13]:


# Strip any leading or trailing spaces in the titles
movies_df['title'] = movies_df['title'].str.strip()

# Search again after cleaning
matrix_titles_cleaned = movies_df[movies_df['title'].str.contains('Matrix', case=False, na=False)]
print("Matching titles after cleaning:", matrix_titles_cleaned)



# In[14]:


import pandas as pd

# Load the necessary CSV files
movies_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\movies.csv')
tags_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\tags.csv')

# Strip any leading or trailing spaces in the titles
movies_df['title'] = movies_df['title'].str.strip()

# Find the movieId for "Matrix, The (1999)"
matrix_movie_id = movies_df[movies_df['title'] == 'Matrix, The (1999)']['movieId'].values[0]

# Get the tags associated with the movieId
matrix_tags = tags_df[tags_df['movieId'] == matrix_movie_id]['tag'].unique()

print("Tags for 'Matrix, The (1999)':", matrix_tags)


# In[16]:


import pandas as pd

# Load the necessary CSV files
movies_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\movies.csv')
ratings_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\ratings.csv')

# Strip any leading or trailing spaces in the titles
movies_df['title'] = movies_df['title'].str.strip()

# Get the movieId for "Terminator 2: Judgment Day (1991)"
terminator_movie_id = movies_df[movies_df['title'] == 'Terminator 2: Judgment Day (1991)']['movieId'].values[0]

# Filter ratings for this movieId
terminator_ratings = ratings_df[ratings_df['movieId'] == terminator_movie_id]

# Calculate the average rating
average_rating = terminator_ratings['rating'].mean()

print("Average rating for 'Terminator 2: Judgment Day (1991)':", average_rating)


# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the necessary CSV files
movies_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\movies.csv')
ratings_df = pd.read_csv('C:\\Users\\B VENKATA RAMANA\\Downloads\\movie_data\\ratings.csv')

# Strip any leading or trailing spaces in the titles
movies_df['title'] = movies_df['title'].str.strip()

# Get the movieId for "Fight Club (1999)"
fight_club_movie_id = movies_df[movies_df['title'] == 'Fight Club (1999)']['movieId'].values[0]

# Filter ratings for this movieId
fight_club_ratings = ratings_df[ratings_df['movieId'] == fight_club_movie_id]

# Plot the distribution of ratings
plt.figure(figsize=(10, 6))
sns.histplot(fight_club_ratings['rating'], bins=10, kde=True)
plt.title('Distribution of Ratings for "Fight Club (1999)"')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()


# In[18]:


import pandas as pd

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



# In[19]:


import pandas as pd

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

# Find the movie with the highest average rating
most_popular_movie = movies_filtered.loc[movies_filtered['average_rating'].idxmax()]

print("Most popular movie based on average user ratings:")
print(f"Title: {most_popular_movie['title']}")
print(f"Average Rating: {most_popular_movie['average_rating']}")


# In[20]:


import pandas as pd

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

# Find the top 5 movies based on number of ratings
top_5_movies = movies_filtered.nlargest(5, 'rating_count')

# List of provided movie titles
provided_titles = [
    'Pulp Fiction (1994)',
    'Bad Boys (1995)',
    'Silence of the Lambs, The (1991)',
    'Matrix, The (1999)'
]

# Check which of the provided movies are in the top 5
top_movies_titles = top_5_movies['title'].tolist()
correct_options = [title for title in provided_titles if title in top_movies_titles]

print("Top 5 popular movies based on number of user ratings:")
print(top_movies_titles)

print("\nCorrect options among the provided list:")
print(correct_options)


# In[21]:


import pandas as pd

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

# Filter Sci-Fi movies
sci_fi_movies = movies_filtered[movies_filtered['genres'].str.contains('Sci-Fi', case=False, na=False)]

# Find the third most popular Sci-Fi movie based on the number of ratings
third_most_popular_sci_fi = sci_fi_movies.nlargest(3, 'rating_count').iloc[2]

print("Third most popular Sci-Fi movie based on number of user ratings:")
print(f"Title: {third_most_popular_sci_fi['title']}")
print(f"Number of Ratings: {third_most_popular_sci_fi['rating_count']}")


# In[ ]:


import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


# In[ ]:


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


# In[ ]:


# Example usage
imdb_ids = ['tt114709', 'tt113497', 'tt113228']
for imdb_id in imdb_ids:
    rating = scrapper(imdb_id)
    print(f"IMDb ID: {imdb_id}, Rating: {rating}")


# In[ ]:


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
movies_filtered.head()


# In[ ]:


# Find the movie with the highest average rating
highest_rated_movie = movies_filtered.loc[movies_filtered['average_rating'].idxmax()]
print(f"The movie with the highest IMDB rating is movieId {highest_rated_movie['movieId']}")

# Filter Sci-Fi movies
sci_fi_movies = movies_filtered[movies_filtered['genres'].str.contains('Sci-Fi')]

# Find the Sci-Fi movie with the highest average rating
highest_rated_sci_fi_movie = sci_fi_movies.loc[sci_fi_movies['average_rating'].idxmax()]
print(f"The Sci-Fi movie with the highest IMDB rating is movieId {highest_rated_sci_fi_movie['movieId']}")


# In[ ]:




