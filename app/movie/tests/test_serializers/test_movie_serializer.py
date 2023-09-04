from django.test import TestCase
from rest_framework.exceptions import ValidationError

from ..factories import MovieFactory
from ...serializers import MovieSerializer


class MovieSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.instance = MovieFactory()
        cls.Serializer = MovieSerializer
        return super().setUpTestData()

    def test_invalid_genre_raises_ValidationError(self):
        serializer = self.Serializer(
            self.instance, data={"genres": ["notagenre"]}, partial=True
        )
        self.assertRaises(
            ValidationError, lambda: serializer.is_valid(raise_exception=True)
        )

    def test_empty_genres_raises_ValidationError(self):
        serializer = self.Serializer(self.instance, data={"genres": []}, partial=True)
        self.assertRaises(
            ValidationError, lambda: serializer.is_valid(raise_exception=True)
        )

    def test_invalid_streaming_service_raises_ValidationError(self):
        serializer = self.Serializer(
            self.instance,
            data={"streaming_options": ["NotAStreamingService"]},
            partial=True,
        )
        self.assertRaises(
            ValidationError, lambda: serializer.is_valid(raise_exception=True)
        )

    def test_empty_streaming_options_is_valid(self):
        serializer = self.Serializer(
            self.instance,
            data={"streaming_options": []},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        self.assertEqual(instance.streaming_options, [])

    def test_invalid_release_year_raises_ValidationError(self):
        serializer = self.Serializer(
            self.instance,
            data={"release_year": "string"},
            partial=True,
        )
        self.assertRaises(
            ValidationError, lambda: serializer.is_valid(raise_exception=True)
        )
