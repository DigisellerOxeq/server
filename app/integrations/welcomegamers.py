from typing import Any, Optional

from app.core.config import settings
from app.lib.http_client import HTTPClient
from app.schemas.offers import LotType


class WelcomeGamersAPIError(Exception):
    def __init__(self, message: str, status_code: int | None = None):
        self.status_code = status_code
        super().__init__(message)


class WelcomeGamersAPI:
    def __init__(self, http_client: HTTPClient, api_key: str):
        self.base_url = settings.wgamers.base_url
        self.http_client = http_client
        self.api_key = api_key

    async def test_request(
            self,
            lot_type: LotType,
            currency: Optional[str] = None,
            nominal: Optional[str] = None,
            platform: Optional[str] = None,
    ) -> dict[str:Any]:

        test_list = ["code1", "code2", "code3"]
        try:
            return {"get_time": 1, "values": test_list}
        except Exception as e:
            raise WelcomeGamersAPIError(f"Auth failed: {str(e)}")
