from django.test import TestCase

from ..constants import *
from ...models import Profile
from ...serializers import UserSerializer


class UserSerializerTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.UserSerializer = UserSerializer
        return super().setUpClass()

    def test_user_serializer_creation(self):
        # test that the serializer creates a user
        data = {"email": TEST_EMAIL, "password": TEST_PASSWORD}
        serializer = self.UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        self.assertEqual(user.first_name, "")

        # confirm that the user save has created a default profile
        user_profile = Profile.objects.get(user=user)
        self.assertEqual(user_profile, user.profile)
