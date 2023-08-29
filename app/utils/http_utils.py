import logging

from rest_framework.response import Response


logger = logging.getLogger("main")


def generate_error_response(message: str, status: int, **kwargs) -> Response:
    meta = kwargs.get("meta", None)
    short_message = kwargs.get("short_message", None)

    if type(message) != str:
        raise TypeError("message argument must be of type string")

    if type(status) != int:
        raise TypeError("status argument must be of type integer")

    if meta:
        if type(meta) != str:
            raise TypeError("meta argument must be of type string")

    if short_message:
        if type(short_message) != str:
            raise TypeError("short_message argument must be of type string")

    error = {"message": message}
    if meta:
        error["meta"] = meta
    if short_message:
        error["short_message"] = short_message

    data = {"error": error}

    logger.error(message)

    return Response(data=data, status=status)
