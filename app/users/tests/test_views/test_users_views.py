from django.test import TestCase

# from django.contrib.auth.views import LoginView

# from django.contrib.auth import views as auth_views

from rest_framework.authtoken import views as token_views
from rest_framework import exceptions


from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIRequestFactory, force_authenticate

from ..constants import TEST_EMAIL_ADDRESS, TEST_PASSWORD

from ...views import *
from ...models import User


class UserCreateViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.view = UserCreateAPIView.as_view()
        cls.User = User

    def test_create_user_unauthenticated_requires_email():
        pass

    def test_create_user_unauthenticated_requires_username():
        pass

    def test_create_user_unauthenticated_requires_password():
        pass

    def test_create_user_authenticated_uses_id():
        # show that if the request is made with an authentication, it uses the authenticated id
        pass

    # def test_create_user_authenticated_not_requires_username():
    #     pass

    # def test_create_user_authenticated_not_requires_password():
    #     pass
