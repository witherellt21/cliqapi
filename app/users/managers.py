from typing import Any
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.apps import apps

from django.utils.translation import ugettext as _


class UserManager(BaseUserManager):
    """Manager for our custom user model users.models.User"""

    use_in_migrations = True

    def _create_user(self, username, email, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        password = extra_fields.get(_("password"), None)

        if not username:
            raise ValueError(_("The given username must be set"))
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        if password:
            user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)
        return self._create_user(username, email, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("password", password)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))

        return self._create_user(username, email, **extra_fields)

    def create(self, **kwargs: Any) -> Any:
        return super().create(**kwargs)
