import traceback

# from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import login as _login

from rest_framework import generics, mixins, status, exceptions, response
from rest_framework.decorators import api_view

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


@api_view(["POST"])
def create_account(request, *args, **kwargs):
    try:
        # print("creating account")
        # print(request.POST)
        serializer = UserSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        return response.Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            content_type="application/json",
        )

    except exceptions.APIException as api_error:
        return generate_error_response(
            str(api_error),
            status=api_error.status_code,
            long_message=traceback.format_exc(),
        )
    except Exception as e:
        return generate_error_response(
            traceback.format_exc(),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            long_message=traceback.format_exc(),
        )


@api_view(["POST"])
def login(request):
    try:
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        # request.session["username"] = email
        # print(user)
        if user is not None:
            res = _login(request, user)
            print(res)

        else:
            raise exceptions.APIException("Invalid login.")

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
