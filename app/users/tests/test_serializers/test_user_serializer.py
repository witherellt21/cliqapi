from django.test import TestCase

from rest_framework.exceptions import ValidationError

from ..constants import *
from ...serializers import UserSerializer
from ...models import User


class UserSerializerCreationTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.UserSerializer = UserSerializer
        cls.User = User
        return super().setUpClass()

    def test_user_serializer_requires_id(self):
        data = TEST_USER.copy()
        data.pop("id")
        serializer = self.UserSerializer(data=data)
        self.assertRaises(
            ValidationError, lambda: serializer.is_valid(raise_exception=True)
        )

    def test_user_serializer_creation(self):
        # test that the serializer creates a user
        data = TEST_USER.copy()
        serializer = self.UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        self.assertEqual(user.first_name, TEST_USER.get("first_name"))
        self.assertEqual(user.last_name, TEST_USER.get("last_name"))
        self.assertEqual(user.username, TEST_USER.get("username"))
        self.assertEqual(user.id, TEST_USER.get("id"))
        self.assertEqual(user.email_address, TEST_USER.get("email_address"))
        self.assertEqual(user, self.User.objects.get(pk=TEST_USER.get("id")))


class UserSerializerUpdateTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.Serializer = UserSerializer
        cls.UserModel = User
        return super().setUpClass()

    @classmethod
    def setUpTestData(cls) -> None:
        data = TEST_USER.copy()
        serializer = cls.Serializer(data=data)
        serializer.is_valid(raise_exception=True)
        cls.instance = serializer.save()
        # return super().setUpTestData()

    def test_username_cannot_be_changed(self):
        serializer = self.Serializer(
            instance=self.instance, data={"username": "changed_name"}, partial=True
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        self.assertEqual(instance.username, TEST_USER.get("username"))
