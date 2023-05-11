from django.contrib import admin
from django.urls import path
from app.movie import views

urlpatterns = [
    path("", views.MovieListCreateAPIView.as_view(), name="movie-list-create"),
]
