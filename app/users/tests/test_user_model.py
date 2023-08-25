from django.test import TestCase

from django.contrib.auth import get_user_model


class UserModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.User = get_user_model()

    def test_create_superuser(self):
        self.User.create_superuser()
