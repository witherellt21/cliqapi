import factory
from faker import Faker
from random import uniform
from app.movie.tests.factories import MovieFactory

from ..factories import UserFactory
from ...movie_ratings import MovieRating

fake = Faker()


class MovieRatingFactory(factory.django.DjangoModelFactory):
    movie = factory.SubFactory(MovieFactory)
    user = factory.SubFactory(UserFactory)
    rating = factory.LazyAttribute(lambda o: uniform(0.1, 10.0))

    class Meta:
        model = MovieRating
