import os

import pandas as pd
import requests

api_key = os.getenv("TMDB_API_KEY")
if not api_key:
    raise RuntimeError("Set the TMDB_API_KEY environment variable before running this script.")

pages = []
for page in range(1, 6):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/popular",
        params={"api_key": api_key, "language": "en-US", "page": page},
        headers={"accept": "application/json"},
        timeout=30,
    )
    response.raise_for_status()

    movies = pd.DataFrame(response.json()["results"])
    movies = movies.reindex(
        columns=["title", "release_date", "vote_average", "popularity", "adult", "id"]
    )
    movies = movies.rename(
        columns={
            "title": "Movie title",
            "release_date": "Release date",
            "vote_average": "Rating",
            "popularity": "Popularity",
            "adult": "Adult",
            "id": "Movie_Id",
        }
    )
    pages.append(movies)

final_data = pd.concat(pages, ignore_index=True)
print(final_data.head())

# Store to csv
# final_data.to_csv("tmdb_movies.csv", index=False)
