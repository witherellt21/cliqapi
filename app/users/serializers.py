# from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import User


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
            # "id": {"write_only": True, "min_length": 4},
        }
