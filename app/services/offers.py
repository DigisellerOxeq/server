from typing import Sequence

from app.repositories.offers import OfferRepository
from app.schemas.orders import OfferRead


class OfferService:
    def __init__(self, offer_repo: OfferRepository):
        self.offer_repo = offer_repo

    async def get_all_offers(self) -> Sequence[OfferRead]:
        return await self.offer_repo.get_all()
