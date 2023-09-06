from django.test import TestCase
from django.urls import reverse, resolve, NoReverseMatch

from rest_framework.test import APIRequestFactory
from rest_framework import status

from ..factories import MovieRatingFactory
from ..factories import UserFactory


class MovieRatingsListTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.factory = APIRequestFactory()
        cls.user = UserFactory()
        cls.view = resolve(
            reverse("movie-ratings", kwargs={"user_id": cls.user.id})
        ).func
        cls.MovieRating = MovieRatingFactory

    def test_list_movie_ratings_return_format(self):
        ratings = self.MovieRating.create_batch(10, user=self.user)
        request = self.factory.get(
            reverse("movie-ratings", kwargs={"user_id": self.user.id})
        )
        response = self.view(request, user_id=self.user.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertIn("count", response.data)
        self.assertEqual(len(response.data["results"]), response.data["count"])
        self.assertEqual(response.data["count"], 10)

    def test_list_movie_ratings_multiple_users(self):
        ratings = self.MovieRating.create_batch(5, user=self.user)
        other_ratings = self.MovieRating.create_batch(10)
        request = self.factory.get(
            reverse("movie-ratings", kwargs={"user_id": self.user.id})
        )
        response = self.view(request, user_id=self.user.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 5)

    def test_list_movie_ratings_user_DNE_raises_NotFound(self):
        ratings = self.MovieRating.create_batch(5, user=self.user)
        other_ratings = self.MovieRating.create_batch(10)
        self.assertRaises(
            NoReverseMatch,
            lambda: self.factory.get(
                reverse("movie-ratings", kwargs={"user_id": "notauser"})
            ),
        )

    def test_get_rating_DNE_returns_404(self):
        ratings = self.MovieRating.create_batch(5, user=self.user)
        request = self.factory.get(
            reverse("movie-ratings", kwargs={"user_id": self.user.id})
        )
        response = self.view(request, user_id=self.user.id, pk="notaratingid")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # TODO: make this test work more intelligently
    def test_get_rating_return_format(self):
        ratings = self.MovieRating.create_batch(5, user=self.user)
        request = self.factory.get(
            reverse("movie-ratings", kwargs={"user_id": self.user.id})
        )
        response = self.view(request, user_id=self.user.id, pk=ratings[0].id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("movie", response.data)
        self.assertIn("user", response.data)
        self.assertIn("rating", response.data)
        self.assertIn("rated_on", response.data)
        self.assertIsInstance(response.data.get("movie"), dict)
        self.assertIsInstance(response.data.get("user"), dict)

    def test_create_movie_rating_success(self):
        rating = self.MovieRating()
        request = self.factory.post(
            reverse(
                "movie-ratings",
                kwargs={"user_id": self.user.id},
                data={
                    "movie": rating.movie,
                },
            )
        )
        response = self.view(request, user_id=self.user.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_movie_requires_movie(self):
        request = self.factory.post(
            reverse("movie-ratings", kwargs={"user_id": self.user.id})
        )
        response = self.view(request, user_id=self.user.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
