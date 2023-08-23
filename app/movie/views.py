import logging

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, mixins

from app.movie.models import Movie
from app.movie.serializers import MovieSerializer

logger = logging.getLogger("main")

# Create your views here.
class MovieListCreateAPIView(mixins.DestroyModelMixin, ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        logger.debug("receiving movie creation request")
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        logger.debug("creating movie")
        return super().create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
