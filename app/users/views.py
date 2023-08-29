import traceback

from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics, mixins, status, exceptions

from .serializers import UserSerializer

from app.utils.http_utils import generate_error_response


class UserCreateAPIView(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView
):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)

        except exceptions.APIException as api_error:
            return generate_error_response(
                str(api_error),
                status=api_error.status_code,
                long_message=traceback.format_exc(),
            )
        except Exception as e:
            return generate_error_response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                long_message=traceback.format_exc(),
            )
