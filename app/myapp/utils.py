from random import choices
import string

import requests

from rest_framework import exceptions
from app.exceptions import InternalServerError
from app.settings import env


def generate_user_identifier():
    return "user_" + "".join(choices(string.ascii_letters + string.digits, k=27))


UTELLY_API_HOST = "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com"
UTELLY_API_ROOT = f"https://{UTELLY_API_HOST}"


def search_utelly_movies_by_keyword(keyword: str = "", country: str = "us") -> list:
    """utility function for query the Utelly movie database"""
    # configure the request
    url = f"{UTELLY_API_ROOT}/lookup"
    querystring = {"term": keyword, "country": country}
    headers = {
        "X-RapidAPI-Key": env("RAPID_API_KEY"),
        "X-RapidAPI-Host": UTELLY_API_HOST,
    }

    response = requests.get(url, headers=headers, params=querystring)

    # parse the response
    if 200 <= response.status_code <= 400:
        return response.json().get("results", [])

    elif 400 <= response.status_code <= 500:
        raise exceptions.ParseError()

    elif 500 <= response.status_code:
        raise InternalServerError()
