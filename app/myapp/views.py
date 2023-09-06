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
from . import options

import logging

logger = logging.getLogger("main")


@api_view(["GET"])
def get_options_configuration(request, *args, **kwargs):
    try:
        return Response(data=options.CONFIGURATION, status=status.HTTP_200_OK)
    except Exception as unexpected_error:
        return generate_error_response(
            str(unexpected_error),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            long_message=traceback.format_exc(),
        )


class UserCreateAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
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


class MovieRatingListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = MovieRating.objects.all()
    serializer_class = MovieRatingSerializer
    lookup_field = "pk"

    def get(self, request, user_id, *args, **kwargs):
        try:
            self.queryset = self.queryset.filter(user__id=user_id)
            response = self.list(request, *args, **kwargs)

            response.data = {
                "results": self.get_serializer(self.queryset, many=True).data,
                "count": self.queryset.count(),
            }

            return response
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


class MovieRatingAPIView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = MovieRating.objects.all()
    serializer_class = MovieRatingSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        try:
            if kwargs.get("pk"):
                return self.retrieve(request, *args, **kwargs)
            return self.list(request, *args, **kwargs)

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

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
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

    def patch(self, request, pk, *args, **kwargs):
        try:
            # TODO: In the future we create roles
            # role = getattr(request, "_auth", {}).get("role")
            # if role == :

            if any(x in request.data for x in ["movie", "user"]):
                raise exceptions.PermissionDenied(
                    "Cannot update a movie rating's movie or user field."
                )

            # For now, we will just use is_admin attribute
            return self.update(request, pk=pk, partial=True, *args, **kwargs)

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

    def delete(self, request, pk, *args, **kwargs):
        try:
            return self.destroy(request, pk=pk, *args, **kwargs)

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
