from django.urls import path
from .views import *

urlpatterns = [path("", search_movies_by_keyword, name="search-movies")]
