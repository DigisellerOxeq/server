from app.lib.http_client import HTTPClient
from typing import Any


class WelcomeGamersAPIError(Exception):
    def __init__(self, message: str, status_code: int | None = None):
        self.status_code = status_code
        super().__init__(message)


class WelcomeGamersAPI:
    def __init__(self, http_client: HTTPClient, api_key: str):
        self.http_client = http_client
        self.api_key = api_key

    async def test_request(self) -> dict[str:Any]:

        test_list = ["code1", "code2", "code3"]
        try:
            return {"get_time": 1, "values": test_list}
        except Exception as e:
            raise WelcomeGamersAPIError(f"Auth failed: {str(e)}")
