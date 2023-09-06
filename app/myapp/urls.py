from django.urls import path
from .views import *

urlpatterns = [
    path(r"", UserCreateAPIView.as_view(), name="user-create"),
    path(r"configurations/", get_options_configuration, name="options-configuration"),
    # path(
    #     r"<int:user_id>/ratings/",
    #     MovieRatingListAPIView.as_view(),
    #     name="movie-ratings",
    # ),
    path(
        r"ratings/",
        MovieRatingAPIView.as_view(),
        name="movie-ratings",
    ),
    path(
        r"ratings/<int:pk>/",
        MovieRatingAPIView.as_view(),
        name="movie-rating",
    ),
]
