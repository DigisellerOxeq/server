import httpx
from typing import Any, Optional


class HTTPClient:
    def __init__(self, base_url: str, timeout: int = 15, headers: Optional[dict[str, str]] = None,
                 retries: int = 3):
        self.base_url = base_url
        self.timeout = timeout
        self.default_headers = headers or {}
        self.retries = retries

    async def get(self, endpoint: str, params: dict[str, Any] = None, headers: dict[str, str] = None) -> Any:
        attempt = 0
        while attempt < self.retries:
            try:
                combined_headers = self.default_headers.copy()
                if headers:
                    combined_headers.update(headers)

                async with httpx.AsyncClient(timeout=self.timeout) as client:
                    response = await client.get(
                        f"{self.base_url}{endpoint}",
                        params=params,
                        headers=combined_headers
                    )
                    response.raise_for_status()
                    return response.json()

            except (httpx.HTTPStatusError, httpx.TimeoutException, httpx.RequestError) as e:
                attempt += 1
                if attempt == self.retries:
                    raise RuntimeError(f"Request failed after {self.retries} attempts: {str(e)}")
        return None
