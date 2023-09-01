from django.db import models


class Movie(models.Model):
    """Base Movie model."""

    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
