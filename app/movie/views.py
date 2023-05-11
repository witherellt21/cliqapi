import logging

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from app.movie.models import Movie
from app.movie.serializers import MovieSerializer

logger = logging.getLogger("main")

# Create your views here.
class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        logger.debug("receiving movie creation request")
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        logger.debug("creating movie")
        return super().create(request, *args, **kwargs)
