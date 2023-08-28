import pytest

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.validators import EMPTY_VALUES

from .. import constants
from ...models import Profile


class UserModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.User = get_user_model()
        cls.Profile = Profile
        return super().setUpClass()

    @pytest.mark.db_check
    def test_view_db_users(self):
        # print out all users in db
        print(f"All users: {self.User.objects.all()}")
        print(f"Superusers: {self.User.objects.filter(is_superuser=True)}")

    def test_create_superuser(self):
        # test that the user object contains all the necessary fields
        superuser = self.User.objects.create_superuser(
            email=constants.TEST_EMAIL, password=constants.TEST_PASSWORD
        )
        self.assertEqual(superuser.email, constants.TEST_EMAIL)
        self.assertEqual(superuser.first_name, "")
        self.assertEqual(superuser.last_name, "")
        # self.assertEqual(superuser.avatar, "")
        self.assertEqual(superuser.is_active, True)
        self.assertNotIn(superuser.date_joined, EMPTY_VALUES)

    def test_create_user_creates_profile(self):
        user = self.User.objects.create()
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile, user.profile)
