import time
import hashlib

from app.lib.http_client import HTTPClient


class DigisellerAPIError(Exception):
    def __init__(self, message: str, status_code: int | None = None):
        self.status_code = status_code
        super().__init__(message)


class DigisellerAPI:
    def __init__(self, http_client: HTTPClient, token: str, seller_id: int):
        self.http_client = http_client
        self.token = token
        self.seller_id = seller_id

    async def get_auth_token(self) -> str:
        timestamp = int(time.time())
        signature = self._generate_signature(timestamp)

        try:
            response = await self.http_client.post(
                endpoint="/api/apilogin",
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
        data = f"{self.token}{timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()
