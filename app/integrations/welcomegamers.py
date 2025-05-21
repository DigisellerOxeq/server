from app.lib.http_client import HTTPClient


class WelcomeGamersAPIError(Exception):
    def __init__(self, message: str, status_code: int | None = None):
        self.status_code = status_code
        super().__init__(message)


class WelcomeGamersAPI:
    def __init__(self, http_client: HTTPClient, api_key: str):
        self.http_client = http_client
        self.api_key = api_key


