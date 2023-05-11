from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
import logging

logger = logging.getLogger("main")

# Create your views here.
class MovieListCreateAPIView(ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        logger.debug("receiving movie creation request")
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        logger.debug("creating movie")
        return super().create(request, *args, **kwargs)
