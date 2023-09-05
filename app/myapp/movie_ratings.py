from django.db import models
from django.utils.translation import gettext_lazy as _

# from app.settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from app import settings

from app.movie.models import Movie
from .user import User


class MovieRating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    rating = models.DecimalField(_("rating"), max_digits=3, decimal_places=1)
    rated_on = models.DateTimeField(_("rated on"), auto_now_add=True, editable=False)

    # likes = LikesField
    # comments = CommentsField

    def calculate_rating(self) -> None:
        raise NotImplementedError

    def like(self, user: User) -> None:
        raise NotImplementedError
        # likes.add(user)

    def comment(self, user: User, message: str) -> None:
        raise NotImplementedError
        # comments.add(Comment(user=user, message=message))
