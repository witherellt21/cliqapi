from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIRequestFactory

from ...views import search_movies_by_keyword


class MovieViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.factory = APIRequestFactory()
        cls.view = search_movies_by_keyword

    def test_view_url_exists(self):
        request = self.factory.get(reverse("search-movies"))
        response = self.view(request)
        self.assertNotEqual(response.status_code, 404)

    def test_search_movie_view(self):
        request = self.factory.get(reverse("search-movies"), QUERY_STRING="term=star")
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data.get("results")), 1)
