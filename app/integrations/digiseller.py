import time
import hashlib
from typing import Any

from app.core.config import settings
from app.lib.http_client import HTTPClient


class DigisellerAPIError(Exception):
    def __init__(self, message: str, status_code: int | None = None):
        self.status_code = status_code
        super().__init__(message)


class DigisellerAPI:
    def __init__(self, http_client: HTTPClient, base_url: str, api_key: str, seller_id: int):
        self.base_url = base_url
        self.http_client = http_client
        self.api_key = api_key
        self.seller_id = seller_id

    async def get_auth_token(self) -> str:
        timestamp = int(time.time())
        signature = self._generate_signature(timestamp)

        try:
            response = await self.http_client.post(
                endpoint=self.base_url + "/api/apilogin",
                json={
                    "seller_id": self.seller_id,
                    "timestamp": timestamp,
                    "sign": signature,
                },
            )

            if not response.get("token"):
                raise DigisellerAPIError("Invalid response format")

            return response["token"]

        except Exception as e:
            raise DigisellerAPIError(f"Auth failed: {str(e)}")

    def _generate_signature(self, timestamp: int) -> str:
        data = f"{self.api_key}{timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()

    async def search_order(self, unique_code, token) -> dict[Any]:
        try:
            response = await self.http_client.get(
                endpoint=self.base_url + f"/api/purchases/unique-code/{unique_code}/?token={token}",
            )
            print(response)
            if response.get("retval") != 0:
                raise DigisellerAPIError("Invalid response format")

            return response

        except Exception as e:
            raise DigisellerAPIError(f"Search failed: {str(e)}")
