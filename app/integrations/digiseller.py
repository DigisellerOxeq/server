import httpx
from typing import Any


class DigisellerAPI:
    BASE_URL = "https://partner-api.example.com"
    TIMEOUT = 15.0

    def __init__(self, token: str):
        self.token = token

    async def get_data_by_code(self, code: str) -> dict[str, Any]:
        url = f"{self.BASE_URL}/api/data"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json"
        }
        params = {"code": code}

        try:
            async with httpx.AsyncClient(timeout=self.TIMEOUT) as client:
                response = await client.get(url, headers=headers, params=params)
                response.raise_for_status()
                return response.json()

        except httpx.HTTPStatusError as e:
            raise RuntimeError(f"HTTP error {e.response.status_code}: {e.response.text}")
        except httpx.TimeoutException:
            raise RuntimeError("Request timed out")
        except httpx.RequestError as e:
            raise RuntimeError(f"Request failed: {str(e)}")