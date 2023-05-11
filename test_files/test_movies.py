import requests, environ, os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

API_ROOT = f"http://localhost:{env('SERVER_PORT')}/api/v1"


def get_health():
    endpoint = f"{API_ROOT}/get-health"
    return requests.get(endpoint)


def list_movies():
    endpoint = f"{API_ROOT}/movie"
    response = requests.get(endpoint)
    return response


if __name__ == "__main__":
    from pprint import PrettyPrinter

    pp = PrettyPrinter(depth=10)

    health = get_health()
    pp.pprint(health.json())

    # movie = list_movies()
    # pp.pprint(movie.json())
