import logging, random
from time import time
from typing import Any

logger = logging.getLogger("main")


class RequestLoggingMiddleware:
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
        response = self.get_response(request)
        elapsed = round(time() - start, 3)

        # TODO: use resolve/reverse for this
        if not request.get_full_path() == "/api/v1/metrics/get-status":
            logger.info(
                f"End Request - {request_identifier} - {remote} - {request.method} - {request.get_full_path()} - {response.status_code} ({str(elapsed)}s)"
            )

        return response
