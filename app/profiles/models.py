from django.db import models
from django.conf import settings


class Profile(models.Model):
    """Base model for a users profile."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
