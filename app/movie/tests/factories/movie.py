import factory
from faker import Faker
from random import sample, randint

from app.options import StreamingService, Genre
from ...models import Movie

fake = Faker()


def sample_streaming_options():
    return sample(
        [choice[0] for choice in StreamingService.choices],
        randint(1, len(StreamingService.choices)),
    )


def sample_genres():
    return sample(
        [choice[0] for choice in Genre.choices], randint(1, len(Genre.choices))
    )


def random_duration():
    return randint(70, 140)


def random_title():
    return fake.text(50)


def random_year_as_int():
    return int(fake.year())


class MovieFactory(factory.django.DjangoModelFactory):
    title = factory.LazyFunction(random_title)
    release_year = factory.LazyFunction(random_year_as_int)
    genres = factory.LazyFunction(sample_genres)
    streaming_options = factory.LazyFunction(sample_streaming_options)
    duration = factory.LazyFunction(random_duration)

    class Meta:
        model = Movie
