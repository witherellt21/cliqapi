from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .utils import search_utelly_movies_by_keyword


# Create your views here.
@api_view(["GET"])
def search_movies_by_keyword(request, *args, **kwargs):
    results = search_utelly_movies_by_keyword(request, *args, **kwargs).json()
    return Response(data=results, status=status.HTTP_200_OK)
