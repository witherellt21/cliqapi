from django.test import TestCase
from rest_framework.exceptions import ValidationError

from ...serializers import MovieRatingSerializer
from ..factories import UserFactory, MovieRatingFactory


class MovieRatingSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.Serializer = MovieRatingSerializer
        cls.instance = MovieRatingFactory()
        cls.UserFactory = UserFactory

    def test_invalid_rating_raises_ValidationError(self):
        serializer = self.Serializer(
            self.instance, data={"rating": "string"}, partial=True
        )
        self.assertRaises(
            ValidationError, lambda: serializer.is_valid(raise_exception=True)
        )

    def test_rated_on_cannot_be_edited(self):
        serializer = self.Serializer(
            self.instance, data={"rated_on": "123"}, partial=True
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        self.assertNotEqual(instance.rated_on, "123")

    def test_create_with_serializer(self):
        movie = self.Movie()
        user = self.UserFactory()
        serializer = self.Serializer(
            data={"movie": movie.id, "user": user.id, "rating": 8.1}
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        self.assertEqual(instance.movie, movie)
        self.assertEqual(instance.user, user)
        self.assertEqual(float(instance.rating), 8.1)
        self.assertNotEqual(instance.rated_on, None)
