import factory
from faker import Faker
from random import uniform, randint, choice

from ...movie_ratings import MovieRating

fake = Faker()


class MovieRatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MovieRating
