from fastapi import Request

from app.integrations.digiseller import DigisellerAPI
from app.core.config import settings

async def get_digiseller_api(request: Request) -> DigisellerAPI:
    return DigisellerAPI(
        http_client=request.app.state.http_client,
        token=settings.digi.token,
        seller_id=settings.digi.seller_id
    )