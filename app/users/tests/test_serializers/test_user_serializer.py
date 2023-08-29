from django.test import TestCase

from ..constants import *
from ...serializers import UserSerializer
from ...models import User


class UserSerializerCreationTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.UserSerializer = UserSerializer
        cls.User = User
        return super().setUpClass()

    def test_user_serializer_creation(self):
        # test that the serializer creates a user
        serializer = self.UserSerializer(data=TEST_USER)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        self.assertEqual(user.first_name, TEST_USER.get("first_name"))
        self.assertEqual(user.last_name, TEST_USER.get("last_name"))
        self.assertEqual(user.username, TEST_USER.get("username"))
        self.assertEqual(user, self.User.objects.get(pk=TEST_USER.get("username")))


class UserSerializerUpdateTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.Serializer = UserSerializer
        cls.UserModel = User
        return super().setUpClass()

    @classmethod
    def setUpTestData(cls) -> None:
        serializer = cls.Serializer()
        return super().setUpTestData()

    def test_username_cannot_be_changed(self):
        pass
