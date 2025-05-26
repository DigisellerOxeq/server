from app.lib.http_client import HTTPClient
from app.core.config import settings


class APIClients:
    def __init__(self):
        self.digi = None
        self.wgamers = None

    async def init_digi_client(self):
        self.digi = HTTPClient(
            headers=settings.digi.headers,
            timeout=settings.digi.timeout,
            delay=settings.digi.delay,
            retries=settings.digi.retries,
        )

    async def init_wgamers_client(self):
        self.wgamers = HTTPClient(
            headers=settings.wgamers.headers,
            timeout=settings.wgamers.timeout,
            delay=settings.wgamers.delay,
            retries=settings.wgamers.retries,
        )

    async def close_all(self):
        if self.digi:
            await self.digi.close()
        if self.wgamers:
            await self.wgamers.close()
