import pytest

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.validators import EMPTY_VALUES
from django.db.utils import IntegrityError

from .. import constants
from ..factories import UserFactory

pytestmark = pytest.mark.django_db


class UserModelCreateTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.User = get_user_model()
        return super().setUpClass()

    def test_create_user_requires_email(self):
        self.assertRaises(
            TypeError,
            lambda: self.User.objects.create_user(
                username=constants.TEST_USERNAME, password=constants.TEST_PASSWORD
            ),
        )

    def test_create_user_requires_username(self):
        self.assertRaises(
            TypeError,
            lambda: self.User.objects.create_user(
                email=constants.TEST_EMAIL_ADDRESS,
                password=constants.TEST_PASSWORD,
            ),
        )

    def test_create_user_does_not_require_password(self):
        user = self.User.objects.create_user(
            username=constants.TEST_USERNAME,
            email=constants.TEST_EMAIL_ADDRESS,
        )
        self.assertEqual(user.password, "")

    def test_create_user_with_password(self):
        user = self.User.objects.create_user(
            username=constants.TEST_USERNAME,
            email=constants.TEST_EMAIL_ADDRESS,
            password=constants.TEST_PASSWORD,
        )
        self.assertEqual(user.username, constants.TEST_USERNAME)
        self.assertEqual(user.email, constants.TEST_EMAIL_ADDRESS)
        self.assertNotEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.is_active, True)
        self.assertNotIn(user.date_joined, EMPTY_VALUES)

    def test_create_users_same_username_raises_IntegrityError(self):
        user = self.User.objects.create_user(
            username=constants.TEST_USERNAME,
            email=constants.TEST_EMAIL_ADDRESS,
        )

        self.assertRaises(
            IntegrityError,
            lambda: self.User.objects.create_user(
                username=user.username,
                email="differentemail@domain.com",
            ),
        )

    def test_create_users_same_email_raises_IntegrityError(self):
        user = self.User.objects.create_user(
            username=constants.TEST_USERNAME,
            email=constants.TEST_EMAIL_ADDRESS,
        )

        self.assertRaises(
            IntegrityError,
            lambda: self.User.objects.create_user(
                username="differentusername",
                email=user.email,
            ),
        )

    def test_create_multiple_users(self):
        user = self.User.objects.create_user(
            username=constants.TEST_USERNAME,
            email=constants.TEST_EMAIL_ADDRESS,
        )
        user2 = self.User.objects.create_user(
            username="differentusername", email="differentemail@domain.com"
        )
        self.assertNotEqual(user.id, user2.id)

    def test_create_superuser(self):
        # test that the user object contains all the necessary fields
        superuser = self.User.objects.create_superuser(
            username=constants.TEST_USERNAME,
            email=constants.TEST_EMAIL_ADDRESS,
            password=constants.TEST_PASSWORD,
        )
        self.assertEqual(superuser.username, constants.TEST_USERNAME)
        self.assertEqual(superuser.email, constants.TEST_EMAIL_ADDRESS)
        self.assertNotEqual(superuser.password, "")
        self.assertEqual(superuser.first_name, "")
        self.assertEqual(superuser.last_name, "")
        self.assertEqual(superuser.is_active, True)
        self.assertNotIn(superuser.date_joined, EMPTY_VALUES)

    def test_object_create_id_default(self):
        user = self.User.objects.create()
        self.assertIsInstance(user.id, int)

    def test_object_create_same_usernames_raises_IntegrityError(self):
        user = self.User.objects.create(username=constants.TEST_USERNAME)
        self.assertRaises(
            IntegrityError,
            lambda: self.User.objects.create(username=user.get_username()),
        )

    def test_object_create_same_email_raises_IntegrityError(self):
        user = self.User.objects.create(email=constants.TEST_EMAIL_ADDRESS)
        self.assertRaises(
            IntegrityError,
            lambda: self.User.objects.create(email=user.email),
        )

    def test_object_create_same_id_raises_IntegrityError(self):
        user = self.User.objects.create()
        self.assertRaises(
            IntegrityError,
            lambda: self.User.objects.create(id=user.id),
        )


def test_user_factory():
    user = UserFactory()
    print(user.username)
    assert user.username != None
