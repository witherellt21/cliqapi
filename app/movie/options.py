from django.db import models
from django.utils.translation import gettext_lazy as _


class Genre(models.TextChoices):
    COMEDY = _("Comedy")
    ROMANCE = _("Romance")
    THRILLER = _("Thriller")
    DRAMA = _("Drama")
    OTHER = _("Other")


class StreamingService(models.TextChoices):
    NETFLIX = _("Netflix")
    MAX = _("Max")
    HULU = _("Hulu")
    PEACOCK = _("Peacock")
    DISNEY_PLUS = _("Disney+")
    PRIME = _("Primer")
