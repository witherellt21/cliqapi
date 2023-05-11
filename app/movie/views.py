from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

# Create your views here.
class MovieListCreateAPIView(ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
