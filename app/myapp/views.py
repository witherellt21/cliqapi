import traceback

from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from django.http import Http404

from rest_framework import generics, mixins, status, exceptions
from rest_framework.response import Response
from rest_framework.decorators import api_view

from app.utils.http_utils import generate_error_response

from .models import MovieRating
from .serializers import UserCreationSerializer, MovieRatingSerializer

import logging

logger = logging.getLogger("main")


class UserCreateAPIView(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView
):
    queryset = get_user_model().objects.all()
    serializer_class = UserCreationSerializer
    lookup_field = "pk"

    def post(self, request, *args, **kwargs):
        try:
            user = getattr(request, "user", None)
            auth = getattr(request, "_auth", None)

            # if authenticated by third party, create link to database
            if user != "AnonymousUser" and auth != None:
                username = auth.get("username", None)
                email = auth.get("email", None)

                password = request.data.get(
                    "password",
                    get_random_string(12),
                    # password is arbitrary as user is using third-party authentication
                )

                if all([username, email]):
                    request.data.update(
                        {
                            "username": username,
                            "email": email,
                            "password": password,
                        }
                    )

            return self.create(request, *args, **kwargs)

        except Http404 as e404:
            raise exceptions.NotFound(str(e404))

        # TODO: probably don't need this
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


class MovieRatingAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = MovieRating.objects.all()
    serializer_class = MovieRatingSerializer
    lookup_field = "pk"

    def get_object(self):
        return super().get_object()

    def get(self, request, user_id, *args, **kwargs):
        try:
            self.queryset = self.queryset.filter(user__id=user_id)

            if kwargs.get("pk", None):
                return self.retrieve(request, *args, **kwargs)

            payload = {
                "results": self.get_serializer(self.queryset, many=True).data,
                "count": self.queryset.count(),
            }

            return Response(data=payload, status=status.HTTP_200_OK)

        except Http404 as e404:
            raise exceptions.NotFound(str(e404))

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

    def post(self, request, user_id, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, user_id, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)

        except Http404 as e404:
            raise exceptions.NotFound(str(e404))

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
