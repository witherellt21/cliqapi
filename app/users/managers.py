from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password

from django.apps import apps


class UserManager(BaseUserManager):
    """Manager for our custom user model users.models.User"""

    use_in_migrations = True

    def _create_user(self, username, email_address, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        password = extra_fields.get("password", None)

        if not username:
            raise ValueError("The given username must be set")
        email_address = self.normalize_email(email_address)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(
            username=username, email_address=email_address, **extra_fields
        )
        if password:
            user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email_address, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)
        return self._create_user(username, email_address, **extra_fields)

    def create_superuser(self, username, email_address, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("password", password)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        return self._create_user(username, email_address, **extra_fields)
