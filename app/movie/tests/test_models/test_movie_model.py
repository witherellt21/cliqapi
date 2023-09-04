from django.test import TestCase
from ..factories import MovieFactory


class MovieModelTestCase(TestCase):
    def test_movie_model_creation(self):
        movie = MovieFactory()

        # check out the title
        self.assertIsInstance(movie.title, str)
        self.assertNotEqual(movie.title, "")

        # check out the release year
        self.assertIsInstance(movie.release_year, int)

        # check out the genre
        self.assertIsInstance(movie.genres, list)
        self.assertNotEqual(movie.genres, [])

        # check out the streaming options
        self.assertIsInstance(movie.streaming_options, list)
        self.assertNotEqual(movie.streaming_options, [])

        # check out the duration
        self.assertIsInstance(movie.duration, int)
        self.assertNotEqual(movie.duration, 0)
