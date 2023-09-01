from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

from .managers import UserManager
from .utils import generate_user_identifier


class User(AbstractUser):
    """Base auth user model that overrides the django auth user model."""

    id = models.CharField(
        name=_("id"),
        verbose_name=_("ids"),
        primary_key=True,
        unique=True,
        default=generate_user_identifier,
        max_length=40,
    )
    avatar = models.ImageField(
        name=_("avatar"),
        verbose_name=_("avatars"),
        upload_to="avatars/",
        null=True,
        blank=True,
    )
    email = models.EmailField(_("email address"), unique=True)

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
