import requests
from app.settings import env


UTELLY_API_HOST = "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com"
UTELLY_API_ROOT = f"https://{UTELLY_API_HOST}"


def search_movies_by_keyword(keyword: str = "", country: str = "us") -> list:
    url = f"{UTELLY_API_ROOT}/lookup"

    querystring = {"term": keyword, "country": country}

    headers = {
        "X-RapidAPI-Key": env("RAPID_API_KEY"),
        "X-RapidAPI-Host": UTELLY_API_HOST,
    }

    response = requests.get(url, headers=headers, params=querystring)

    # print(response.json())
    return []
