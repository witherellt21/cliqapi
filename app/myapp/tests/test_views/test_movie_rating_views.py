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
        cls.list_view = resolve(
            reverse("movie-ratings", kwargs={"user_id": cls.user.id})
        ).func
        cls.MovieRating = MovieRatingFactory

    def test_list_movie_ratings_return_format(self):
        ratings = self.MovieRating.create_batch(10, user=self.user)
        request = self.factory.get(
            reverse("movie-ratings", kwargs={"user_id": self.user.id})
        )
        # request = self.factory.get(
        #     f"http://localhost:8002/api/v1/users/{self.user.id}/ratings/"
        # )
        response = self.list_view(request, user_id=self.user.id)
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
        response = self.list_view(request, user_id=self.user.id)
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

    def test_get_rating_DNE_raises_NotFound(self):
        ratings = self.MovieRating.create_batch(5, user=self.user)
        request = self.factory.get(
            reverse("movie-ratings", kwargs={"user_id": self.user.id})
        )
        response = self.list_view(request, user_id=self.user.id, pk="notaratingid")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
