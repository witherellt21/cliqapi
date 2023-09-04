import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.postgres.fields import ArrayField
from app.options import Genre, StreamingService


def default_genres():
    return [_("Other")]


class Movie(models.Model):
    title = models.CharField(_("title"), max_length=50)
    duration = models.IntegerField(_("duration"))
    release_year = models.IntegerField(_("release year"))
    genres = ArrayField(
        models.CharField(max_length=20, choices=Genre.choices),
        len(Genre.choices),
        verbose_name=_("genre"),
        default=default_genres,
    )
    streaming_options = ArrayField(
        models.CharField(max_length=20, choices=StreamingService.choices),
        len(StreamingService.choices),
        verbose_name=_("streaming options"),
        default=list,
        blank=True,
    )
