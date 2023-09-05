import traceback

from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import login as _login
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _

from rest_framework import generics, mixins, status, exceptions, response
from rest_framework.decorators import api_view

from app.utils.http_utils import generate_error_response

from .models import MovieRating
from .serializers import UserCreationSerializer


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
                            "id": user,
                            "username": username,
                            "email": email,
                            "password": password,
                        }
                    )

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


class MovieRatingAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = MovieRating.objects.all()
    serializer_class = UserCreationSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        if kwargs.get("id", False):
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        # except exceptions.APIException as api_error:
        #     return generate_error_response(
        #         str(api_error),
        #         status=api_error.status_code,
        #         long_message=traceback.format_exc(),
        #     )
        # except Exception as e:
        #     return generate_error_response(
        #         str(e),
        #         status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         long_message=traceback.format_exc(),
        #     )
