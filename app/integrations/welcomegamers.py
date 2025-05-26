from typing import Any, Optional

from app.core.config import settings
from app.lib.http_client import HTTPClient
from app.schemas.offers import LotType


class WelcomeGamersAPIError(Exception):
    def __init__(self, message: str, status_code: int | None = None):
        self.status_code = status_code
        super().__init__(message)


class WelcomeGamersAPI:
    def __init__(self, http_client: HTTPClient, base_url: str, api_key: str):
        self.base_url = base_url
        self.http_client = http_client
        self.api_key = api_key

    async def create_goods_task(
            self,
            lot_type: LotType,
            currency: Optional[str] = None,
            nominal: Optional[str] = None,
            platform: Optional[str] = None,
            quantity: Optional[int] = 1
    ) -> dict[str:Any]:

        try:
            data = {
                'account_name': 'digiseller',
                'currency': currency,
                'nominal': nominal,
                'quantity': quantity,
                'platform': platform
            }

            response = await self.http_client.post(
                endpoint=self.base_url + f"/api/funpay/redeem/{lot_type}/delivery",
                json=data
            )

            return response.get('codes')

        except Exception as e:
            raise WelcomeGamersAPIError(f"Get goods failed: {str(e)}")