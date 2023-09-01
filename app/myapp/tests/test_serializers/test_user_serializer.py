from django.test import TestCase

from rest_framework.exceptions import ValidationError

from ..constants import *
from ...serializers import UserSerializer, UserCreationSerializer
from ...models import User


class UserCreationSerializerTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.UserSerializer = UserCreationSerializer
        cls.User = User
        return super().setUpClass()

    def test_user_serializer_default_id(self):
        data = {
            "username": TEST_USERNAME,
            "email": TEST_EMAIL_ADDRESS,
            "password": TEST_PASSWORD,
        }
        serializer = self.UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        self.assertIsInstance(str(user.id), str)
        self.assertEqual(len(user.id), 32)
        self.assertTrue(user.id.startswith("user_"))

    def test_user_serializer_requires_email(self):
        data = {
            "id": TEST_ID,
            "username": TEST_USERNAME,
            "password": TEST_PASSWORD,
        }
        serializer = self.UserSerializer(data=data)
        self.assertRaises(
            ValidationError, lambda: serializer.is_valid(raise_exception=True)
        )

    def test_user_serializer_requires_username(self):
        data = {
            "id": TEST_ID,
            "email": TEST_EMAIL_ADDRESS,
            "password": TEST_PASSWORD,
        }
        serializer = self.UserSerializer(data=data)
        self.assertRaises(
            ValidationError, lambda: serializer.is_valid(raise_exception=True)
        )

    def test_user_serializer_requires_password(self):
        data = {
            "id": TEST_ID,
            "username": TEST_USERNAME,
            "email": TEST_EMAIL_ADDRESS,
        }
        serializer = self.UserSerializer(data=data)
        self.assertRaises(
            ValidationError, lambda: serializer.is_valid(raise_exception=True)
        )

    def test_user_serializer_creation(self):
        # test that the serializer creates a user
        data = {
            "id": TEST_ID,
            "username": TEST_USERNAME,
            "email": TEST_EMAIL_ADDRESS,
            "password": TEST_PASSWORD,
            "first_name": TEST_USER.get("first_name"),
            "last_name": TEST_USER.get("last_name"),
        }
        serializer = self.UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        self.assertEqual(user.first_name, TEST_USER.get("first_name"))
        self.assertEqual(user.last_name, TEST_USER.get("last_name"))
        self.assertEqual(user.username, TEST_USER.get("username"))
        self.assertEqual(user.id, TEST_USER.get("id"))
        self.assertEqual(user.email, TEST_USER.get("email"))
        self.assertEqual(
            user, self.User.objects.get(username=TEST_USER.get("username"))
        )

    def test_update_raises_attribute_error(self):
        data = {
            "id": TEST_ID,
            "username": TEST_USERNAME,
            "email": TEST_EMAIL_ADDRESS,
            "password": TEST_PASSWORD,
        }
        serializer = self.UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        serializer = self.UserSerializer(instance=user, data=data, partial=True)
        serializer.is_valid()
        self.assertRaises(AttributeError, lambda: serializer.save())


class UserSerializerUpdateTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.CreationSerializer = UserCreationSerializer
        cls.Serializer = UserSerializer
        cls.UserModel = User
        return super().setUpClass()

    @classmethod
    def setUpTestData(cls) -> None:
        data = TEST_USER.copy()
        data["password"] = TEST_PASSWORD
        serializer = cls.CreationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        cls.instance = serializer.save()

    def test_create_raises_attribute_error(self):
        new_data = {
            "username": "different_user",
            "id": "user_987654321",
            "email": "differentemail@domain.com",
        }
        serializer = self.Serializer(data=new_data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.assertRaises(AttributeError, lambda: serializer.save())

    def test_change_username(self):
        serializer = self.Serializer(
            instance=self.instance, data={"username": "changed_name"}, partial=True
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        self.assertEqual(instance.username, "changed_name")

    def test_change_email(self):
        serializer = self.Serializer(
            instance=self.instance,
            data={"email": "differentemail@domain.com"},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        self.assertEqual(instance.email, "differentemail@domain.com")

    def test_change_id_not_allowed(self):
        serializer = self.Serializer(
            instance=self.instance, data={"id": "user_987654321"}, partial=True
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        self.assertEqual(user.id, TEST_ID)

    def test_change_password_not_allowed(self):
        serializer = self.Serializer(
            instance=self.instance, data={"password": "newpassword"}, partial=True
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        self.assertEqual(user.id, TEST_ID)

    def test_username_already_exists_raises_ValidationError(self):
        # create new user with the same username as self.instance
        new_data = {
            "username": TEST_USERNAME,
            "id": "user_987654321",
            "email": "differentemail@domain.com",
        }
        serializer = self.CreationSerializer(data=new_data, partial=True)
        self.assertRaises(
            ValidationError, lambda: serializer.is_valid(raise_exception=True)
        )

    def test_email_already_exists_raises_ValidationError(self):
        new_data = {
            "username": "different_username",
            "id": "user_987654321",
            "email": TEST_EMAIL_ADDRESS,
        }
        serializer = self.CreationSerializer(data=new_data, partial=True)
        self.assertRaises(
            ValidationError, lambda: serializer.is_valid(raise_exception=True)
        )

    def test_id_already_exists_raises_ValidationError(self):
        new_data = {
            "username": "different_username",
            "id": TEST_ID,
            "email": "differentemail@domain.com",
        }
        serializer = self.CreationSerializer(data=new_data, partial=True)
        self.assertRaises(
            ValidationError, lambda: serializer.is_valid(raise_exception=True)
        )

    def test_change_username_already_exists_raises_ValidationError(self):
        # create new user with a different username as self.instance
        new_data = {
            "username": "different_name",
            "id": "user_987654321",
            "email": "different_email@domain.com",
        }
        serializer = self.CreationSerializer(data=new_data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        # check that changing the name to self.instance's username raises error
        serializer = self.Serializer(
            instance=instance, data={"username": TEST_USERNAME}, partial=True
        )
        self.assertRaises(
            ValidationError, lambda: serializer.is_valid(raise_exception=True)
        )

    def test_change_email_already_exists_raises_ValidationError(self):
        # create new user with a different username as self.instance
        new_data = {
            "username": "different_name",
            "id": "user_987654321",
            "email": "different_email@domain.com",
        }
        serializer = self.CreationSerializer(data=new_data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        # check that changing the name to self.instance's username raises error
        serializer = self.Serializer(
            instance=instance, data={"email": TEST_EMAIL_ADDRESS}, partial=True
        )
        self.assertRaises(
            ValidationError, lambda: serializer.is_valid(raise_exception=True)
        )
