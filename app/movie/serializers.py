from rest_framework import serializers
from app.movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """Serializer class for the movie model movies.models.Movie"""

    class Meta:
        model = Movie
        fields = "__all__"
