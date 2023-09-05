import logging, random, traceback
from time import time
from typing import Any

from rest_framework import exceptions
from rest_framework import status

from app.utils.http_utils import generate_error_response

logger = logging.getLogger("main")


class RequestHandlerMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> Any:
        # Retrieve info about the IP and Port of the remote connection
        remote_port = request.META.get("REMOTE_PORT", None)
        remote_addr = request.META.get("REMOTE_ADDR", None)
        remote = f"{remote_addr}:{remote_port}"

        # Generate a random number to link the start and end of request transmission
        request_identifier = random.randint(0, 1000)

        # Log info regarding incoming request
        if not request.get_full_path() == "/api/v1/metrics/get-status":
            logger.info(
                f"Start Request - {request_identifier} - {remote} - {request.method} - {request.get_full_path()}"
            )

        # Process request - record elapsed time
        start = time()

        try:
            response = self.get_response(request)
        except exceptions.APIException as api_error:
            response = generate_error_response(
                str(api_error),
                status=api_error.status_code,
                long_message=traceback.format_exc(),
            )
        except Exception as e:
            response = generate_error_response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                long_message=traceback.format_exc(),
            )
        elapsed = round(time() - start, 3)

        if not request.get_full_path() == "/api/v1/metrics/get-status":
            logger.info(
                f"End Request - {request_identifier} - {remote} - {request.method} - {request.get_full_path()} - {response.status_code} ({str(elapsed)}s)"
            )

        return response
