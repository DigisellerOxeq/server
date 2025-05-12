from typing import Any, Optional
import httpx
import asyncio


class HTTPClient:
    def __init__(self, base_url: str, timeout: int = 10, headers: Optional[dict[str, str]] = None,
                 retries: int = 3, delay: int = 1):
        self.base_url = base_url
        self.timeout = timeout
        self.default_headers = headers or {}
        self.retries = retries
        self.delay = delay
        self.client = httpx.AsyncClient(
            timeout=self.timeout,
            headers=self.default_headers,
            limits=httpx.Limits(max_connections=100)
        )

    async def _request(self, method: str, endpoint: str, **kwargs) -> Any:
        attempt = 0
        while attempt < self.retries:
            try:
                response = await self.client.request(method, f"{self.base_url}{endpoint}", **kwargs)
                response.raise_for_status()
                return response.json()
            except (httpx.HTTPStatusError, httpx.TimeoutException, httpx.RequestError) as e:
                attempt += 1
                if attempt == self.retries:
                    raise RuntimeError(f"Request failed after {self.retries} attempts: {str(e)}")
                await asyncio.sleep(self.delay * (2 ** attempt))

    async def get(self, endpoint: str, **kwargs):
        return await self._request("GET", endpoint, **kwargs)

    async def post(self, endpoint: str, **kwargs):
        return await self._request("POST", endpoint, **kwargs)

    async def close(self):
        await self.client.aclose()
