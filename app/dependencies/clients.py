from fastapi import Request

from app.integrations.digiseller import DigisellerAPI
from app.integrations.welcomegamers import WelcomeGamersAPI
from app.core.config import settings


async def get_digiseller_api(request: Request) -> DigisellerAPI:
    return DigisellerAPI(
        http_client=request.app.state.clients.digi,
        api_key=settings.digi.api_key,
        seller_id=settings.digi.seller_id,
    )


async def get_wgamers_api(request: Request) -> WelcomeGamersAPI:
    return WelcomeGamersAPI(
        http_client=request.app.state.clients.wgamers,
        api_key=settings.wgamers.api_key,
    )