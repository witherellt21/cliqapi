from django.test import TestCase
from django.contrib.auth.views import LoginView

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIRequestFactory, force_authenticate

from ..users.tests.constants import TEST_EMAIL, TEST_PASSWORD


class LoginViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.view = LoginView.as_view()

    def test_view_url_exists(self):
        request = self.factory.post(
            reverse("login"), data={"email": TEST_EMAIL, "password": TEST_PASSWORD}
        )
        force_authenticate(request)
        response = self.view(request)

        self.assertNotEqual(response.status_code, 404)
