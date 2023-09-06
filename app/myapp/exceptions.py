from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions as rest_exc
from rest_framework import status


class InvalidRequestParameters(rest_exc.APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = _("The request body is invalid.")
