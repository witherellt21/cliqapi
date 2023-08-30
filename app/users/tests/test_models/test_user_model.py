import pytest

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.validators import EMPTY_VALUES

from .. import constants


class UserModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.User = get_user_model()
        return super().setUpClass()

    @pytest.mark.db_check
    def test_view_db_users(self):
        # print out all users in db
        print(f"All users: {self.User.objects.all()}")
        print(f"Superusers: {self.User.objects.filter(is_superuser=True)}")

    def test_create_user_requires_email(self):
        self.assertRaises(
            TypeError,
            lambda: self.User.objects.create_user(
                username=constants.TEST_USERNAME, password=constants.TEST_PASSWORD
            ),
        )

    def test_create_superuser(self):
        # test that the user object contains all the necessary fields
        superuser = self.User.objects.create_superuser(
            username=constants.TEST_USERNAME,
            email_address=constants.TEST_EMAIL_ADDRESS,
            password=constants.TEST_PASSWORD,
        )
        self.assertEqual(superuser.username, constants.TEST_USERNAME)
        self.assertEqual(superuser.email_address, constants.TEST_EMAIL_ADDRESS)
        self.assertEqual(superuser.first_name, "")
        self.assertEqual(superuser.last_name, "")
        # self.assertEqual(superuser.avatar, "")
        self.assertEqual(superuser.is_active, True)
        self.assertNotIn(superuser.date_joined, EMPTY_VALUES)
