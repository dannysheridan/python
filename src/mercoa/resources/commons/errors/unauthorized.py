# This file was auto-generated by Fern from our API Definition.

from ....core.api_error import ApiError


class Unauthorized(ApiError):
    def __init__(self, body: str):
        super().__init__(status_code=401, body=body)
