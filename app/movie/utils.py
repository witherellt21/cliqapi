import requests

from rest_framework import exceptions
from app.exceptions import InternalServerError
from app.settings import env


UTELLY_API_HOST = "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com"
UTELLY_API_ROOT = f"https://{UTELLY_API_HOST}"


def search_utelly_movies_by_keyword(request, *args, **kwargs) -> list:
    """utility function for query the Utelly movie database"""
    # configure the request
    request.query_params._mutable = True
    request.query_params.setdefault("country", "us")
    request.query_params._mutable = False

    url = f"{UTELLY_API_ROOT}/lookup"
    headers = {
        "X-RapidAPI-Key": env("RAPID_API_KEY"),
        "X-RapidAPI-Host": UTELLY_API_HOST,
    }

    response = requests.get(url, headers=headers, params=request.query_params)

    # parse the response
    if 200 <= response.status_code <= 400:
        return response

    elif 400 <= response.status_code <= 500:
        raise exceptions.ParseError()

    elif 500 <= response.status_code:
        raise InternalServerError()
