from typing import Sequence

from app.db.models.offers import Offers
from app.repositories.offers import OfferRepository
from app.schemas.offers import OfferRead, OfferCreate


class OfferService:
    def __init__(self, offer_repo: OfferRepository):
        self.offer_repo = offer_repo

    async def get_all_offers(self) -> Sequence[OfferRead]:
        return await self.offer_repo.get_all()

    async def get_by_offer_id(self, offer_id: int) -> OfferRead:
        return await self.offer_repo.get_by_id(offer_id)

    async def create_offer(self, data: OfferCreate) -> OfferRead:
        data = Offers(**data.model_dump())
        return await self.offer_repo.create(data)
