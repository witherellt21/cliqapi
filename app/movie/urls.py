from django.urls import path
from . import views

urlpatterns = [
    path("", views.MovieListCreateAPIView.as_view(), name="movie-list-create"),
]
