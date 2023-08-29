from django.test import TestCase
from django.contrib.auth.views import LoginView

from rest_framework.authtoken import views as token_views
from rest_framework import exceptions


from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIRequestFactory, force_authenticate

from ..constants import TEST_EMAIL, TEST_PASSWORD

from ...views import *


class LoginViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.view = UserCreateAPIView.as_view()

        # cls.token_view = token_views.obtain_auth_token

    def test_view_url_exists(self):
        request = self.factory.post(
            reverse("user-create"),
            data={"email": TEST_EMAIL, "password": TEST_PASSWORD},
        )
        force_authenticate(request)
        response = self.view(request)
        self.assertNotEqual(response.status_code, 404)

    def test_user_creation(self):
        request = self.factory.post(
            reverse("user-create"),
            data={"email": TEST_EMAIL, "password": TEST_PASSWORD},
        )
        force_authenticate(request)
        response = self.view(request)
        self.assertEqual(response.data.get("email"), TEST_EMAIL)
        self.assertNotIn("password", response.data.keys())

    def test_user_creation_without_password(self):
        request = self.factory.post(reverse("user-create"), data={"email": TEST_EMAIL})
        force_authenticate(request)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
