from django.test import TestCase
from django.urls import reverse, resolve

from rest_framework import exceptions, status
from rest_framework.test import APIRequestFactory, force_authenticate

from ..constants import TEST_EMAIL_ADDRESS, TEST_PASSWORD, TEST_USERNAME

AUTHENTICATION_CREDENTIALS = {
    "token": {"username": TEST_USERNAME, "email": TEST_EMAIL_ADDRESS},
}


class UserCreateViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.view = resolve(reverse("user-create")).func

    def test_view_url_exists(self):
        request = self.factory.post(reverse("user-create"))
        force_authenticate(request)
        response = self.view(request)
        self.assertNotEqual(response.status_code, 404)

    def test_create_user_unauthenticated_requires_email(self):
        request = self.factory.post(
            reverse("user-create"),
            data={
                "username": TEST_USERNAME,
                "password": TEST_PASSWORD,
            },
        )
        force_authenticate(request)
        response = self.view(request)
        self.assertEqual(response.status_code, exceptions.ValidationError.status_code)

    def test_create_user_unauthenticated_requires_username(self):
        request = self.factory.post(
            reverse("user-create"),
            data={
                "email": TEST_EMAIL_ADDRESS,
                "password": TEST_PASSWORD,
            },
        )
        force_authenticate(request)
        response = self.view(request)
        self.assertEqual(response.status_code, exceptions.ValidationError.status_code)

    def test_create_user_unauthenticated_requires_password(self):
        request = self.factory.post(
            reverse("user-create"),
            data={
                "email": TEST_EMAIL_ADDRESS,
                "username": TEST_USERNAME,
            },
        )
        force_authenticate(request)
        response = self.view(request)
        self.assertEqual(response.status_code, exceptions.ValidationError.status_code)

    def test_create_user_unauthenticated_success(self):
        request = self.factory.post(
            reverse("user-create"),
            data={
                "email": TEST_EMAIL_ADDRESS,
                "username": TEST_USERNAME,
                "password": TEST_PASSWORD,
            },
        )
        force_authenticate(request)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("email"), TEST_EMAIL_ADDRESS)
        self.assertEqual(response.data.get("username"), TEST_USERNAME)
        self.assertEqual(response.data.get("is_superuser"), False)
        self.assertEqual(response.data.get("is_staff"), False)

    def test_create_multiple_unauthenticated_users(self):
        request = self.factory.post(
            reverse("user-create"),
            data={
                "email": TEST_EMAIL_ADDRESS,
                "username": TEST_USERNAME,
                "password": TEST_PASSWORD,
            },
        )
        force_authenticate(request)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        request = self.factory.post(
            reverse("user-create"),
            data={
                "email": "differentemail@domain.com",
                "username": "ilovemovies24",
                "password": TEST_PASSWORD,
            },
        )
        force_authenticate(request)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_authenticated_uses_authenticated_data(self):
        # show that if the request is made with an authentication, it uses the authenticated id
        request = self.factory.post(reverse("user-create"))
        force_authenticate(request, **AUTHENTICATION_CREDENTIALS)
        response = self.view(request)
        self.assertEqual(response.data.get("username"), TEST_USERNAME)
        self.assertEqual(response.data.get("email"), TEST_EMAIL_ADDRESS)
        self.assertEqual(response.data.get("is_superuser"), False)
        self.assertEqual(response.data.get("is_staff"), False)

    def test_create_user_authenticated_does_not_require_password(self):
        # show that if the request is made with an authentication, it uses the authenticated id
        request = self.factory.post(reverse("user-create"))
        force_authenticate(request, **AUTHENTICATION_CREDENTIALS)
        response = self.view(request)
        self.assertEqual(response.data.get("username"), TEST_USERNAME)
        self.assertEqual(response.data.get("email"), TEST_EMAIL_ADDRESS)
