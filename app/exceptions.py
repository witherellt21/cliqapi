from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions as rest_exc
from rest_framework import status


class OperationPreventedError(rest_exc.APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = _(
        "The object cannot be deleted in its current state (there are likely related objects that cannot be cascaded)."
    )


class InvalidRequestParameters(rest_exc.APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = _("The request body is invalid.")


class InternalServerError(rest_exc.APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _("Could not reach the intended API.")
