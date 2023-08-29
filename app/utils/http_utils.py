import logging

from rest_framework.response import Response


logger = logging.getLogger("main")


def generate_error_response(message: str, status: int, **kwargs) -> Response:
    meta = kwargs.get("meta", None)
    long_message = kwargs.get("long_message", None)

    if type(message) != str:
        raise TypeError("message argument must be of type string")

    if type(status) != int:
        raise TypeError("status argument must be of type integer")

    if meta:
        if type(meta) != str:
            raise TypeError("meta argument must be of type string")

    if long_message:
        if type(long_message) != str:
            raise TypeError("long_message argument must be of type string")

    error = {"message": message}
    if meta:
        error["meta"] = meta
    if long_message:
        error["long_message"] = long_message

    data = {"error": error}

    logger.error(message)

    return Response(data=data, status=status)
