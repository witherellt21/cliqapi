from rest_framework import serializers
from django.utils.translation import gettext as _

from app.movie.serializers import MovieSerializer

from .models import User, MovieRating


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        # These fields are displayed but not editable and have to be a part of 'fields' tuple
        read_only_fields = (
            "is_active",
            "is_staff",
            "is_superuser",
        )

        # These fields are only editable (not displayed) and have to be a part of 'fields' tuple
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 4},
        }

    def update(self, instance, validated_data):
        raise AttributeError(_(f"{self.__class__.__name__} has no attribute 'update'."))


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ("password",)

        # These fields are displayed but not editable and have to be a part of 'fields' tuple
        read_only_fields = (
            "is_active",
            "is_staff",
            "is_superuser",
        )

        # These fields are only editable (not displayed) and have to be a part of 'fields' tuple
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 4},
        }

    def create(self, validated_data):
        raise AttributeError(_(f"{self.__class__.__name__} has no attribute 'create'."))


class MovieRatingSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        self.fields["movie"] = MovieSerializer()
        self.fields["user"] = UserSerializer()
        return super().to_representation(obj)

    class Meta:
        model = MovieRating
        fields = "__all__"
