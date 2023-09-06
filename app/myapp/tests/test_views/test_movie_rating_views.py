from django.test import TestCase
from django.urls import reverse, resolve

from rest_framework.test import APIRequestFactory
from rest_framework import status

from ..factories import MovieRatingFactory, UserFactory


class MovieRatingsViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.factory = APIRequestFactory()
        cls.user = UserFactory()
        cls.view = resolve(reverse("movie-ratings")).func
        cls.MovieRatingFactory = MovieRatingFactory
        cls.MovieRating = cls.MovieRatingFactory._meta.model

    def test_list_view_exists(self):
        request = self.factory.get(reverse("movie-ratings"))
        response = self.view(request)
        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_view_exists(self):
        rating = self.MovieRatingFactory(user=self.user)
        request = self.factory.get(reverse("movie-rating", kwargs={"pk": rating.id}))
        response = self.view(request, pk=rating.id)
        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_view_exists(self):
        request = self.factory.post(reverse("movie-ratings"))
        response = self.view(request)
        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_view_exists(self):
        rating = self.MovieRatingFactory(user=self.user)
        request = self.factory.patch(reverse("movie-rating", kwargs={"pk": rating.id}))
        response = self.view(request, pk=rating.id)
        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    # def test_list_return_format(self):
    #     ratings = self.MovieRating.create_batch(10, user=self.user)
    #     request = self.factory.get(reverse("movie-ratings"))
    #     response = self.view(request)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn("results", response.data)
    #     self.assertIn("count", response.data)
    #     self.assertEqual(len(response.data["results"]), response.data["count"])
    #     self.assertEqual(response.data["count"], 10)

    # def test_list_multiple_users(self):
    #     ratings = self.MovieRating.create_batch(5, user=self.user)
    #     other_ratings = self.MovieRating.create_batch(10)
    #     request = self.factory.get(reverse("movie-ratings"))
    #     response = self.view(request)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data["count"], 5)

    def test_get_DNE_returns_404(self):
        rating = self.MovieRatingFactory(user=self.user)
        request = self.factory.get(reverse("movie-rating", kwargs={"pk": rating.id}))
        response = self.view(request, pk="notaratingid")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # TODO: make this test work more intelligently
    def test_get_return_format(self):
        rating = self.MovieRatingFactory(user=self.user)
        request = self.factory.get(reverse("movie-rating", kwargs={"pk": rating.id}))
        response = self.view(request, pk=rating.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("movie", response.data)
        self.assertIn("user", response.data)
        self.assertIn("rating", response.data)
        self.assertIn("rated_on", response.data)
        self.assertIsInstance(response.data.get("movie"), dict)
        self.assertIsInstance(response.data.get("user"), dict)

    def test_post_success(self):
        # create a movie rating to recursively create a movie
        movie = self.MovieRatingFactory().movie

        # create a new movie rating with shared details but a new rating
        request = self.factory.post(
            reverse("movie-ratings"),
            data={
                "user": self.user.id,
                "movie": movie.id,
                "rating": 9.1,
            },
            format="json",
        )
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_requires_movie(self):
        # raises Validation error because no movie was contained in the request
        request = self.factory.post(
            reverse("movie-ratings"),
            data={
                "user": self.user.id,
                "rating": 9.1,
            },
            format="json",
        )
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_requires_rating(self):
        # create a movie rating to recursively create a movie
        movie = self.MovieRatingFactory(rating=8.2).movie

        # raises Validation error because no rating was contained in the request
        request = self.factory.post(
            reverse("movie-ratings"),
            data={"user": self.user.id, "movie": movie.id},
            format="json",
        )
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_data_empty(self):
        # create a movie rating to recursively create a user and movie
        rating = self.MovieRatingFactory(rating=8.2)

        # raises Validation error because no rating was contained in the request
        request = self.factory.patch(
            reverse("movie-rating", kwargs={"pk": rating.id}),
            data={},
            format="json",
        )
        response = self.view(request, pk=rating.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_success(self):
        # create a movie rating to recursively create a user and movie
        rating = self.MovieRatingFactory(rating=8.2)

        # raises Validation error because no rating was contained in the request
        request = self.factory.patch(
            reverse("movie-rating", kwargs={"pk": rating.id}),
            data={"rating": 9.1},
            format="json",
        )
        response = self.view(request, pk=rating.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(response.data.get("rating")), 9.1)

    def test_patch_cannot_change_movie(self):
        # create a movie rating to recursively create a user and movie
        rating = self.MovieRatingFactory(rating=8.2)
        original_movie = rating.movie
        another_movie = self.MovieRatingFactory().movie

        # raises Validation error because no rating was contained in the request
        request = self.factory.patch(
            reverse("movie-rating", kwargs={"pk": rating.id}),
            data={"movie": another_movie.id},
            format="json",
        )
        response = self.view(request, pk=rating.id)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_DNE_returns_404(self):
        mr_id = MovieRatingFactory().id
        # raises Validation error because no rating was contained in the request
        request = self.factory.patch(
            reverse("movie-rating", kwargs={"pk": mr_id}),
            data={},
            format="json",
        )
        response = self.view(request, pk="notarating")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_success(self):
        mr_id = MovieRatingFactory().id
        # raises Validation error because no rating was contained in the request
        request = self.factory.delete(
            reverse("movie-rating", kwargs={"pk": mr_id}),
            data={},
            format="json",
        )
        response = self.view(request, pk=mr_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            self.MovieRating.DoesNotExist,
            lambda: self.MovieRating.objects.get(pk=mr_id),
        )

    def test_delete_DNE_returns_404(self):
        mr_id = MovieRatingFactory().id
        # raises Validation error because no rating was contained in the request
        request = self.factory.delete(
            reverse("movie-rating", kwargs={"pk": mr_id}),
            data={},
            format="json",
        )
        response = self.view(request, pk="notarating")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertRaises(
            self.MovieRating.DoesNotExist,
            lambda: self.MovieRating.objects.get(pk=mr_id),
        )
