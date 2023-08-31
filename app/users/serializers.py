from rest_framework import serializers

from .models import User


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
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'update'.")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ("password", "id")

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
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'create'.")
