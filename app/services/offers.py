from typing import Sequence

from fastapi import HTTPException
from app.db.models.offers import Offers
from app.repositories.offers import OfferRepository
from app.schemas.offers import OfferRead, OfferCreate, OfferUpdate


class OfferService:
    def __init__(self, offer_repo: OfferRepository):
        self.repo = offer_repo

    async def get_all_offers(self) -> Sequence[OfferRead]:
        return await self.repo.get_all()

    async def get_by_offer_id(self, offer_id: int) -> OfferRead:
        offer = await self.repo.get_by_id(offer_id)
        if not offer:
            raise HTTPException(status_code=404, detail="Offer not found")
        return offer

    async def create_offer(self, data: OfferCreate) -> OfferRead:
        offer = await self.repo.get_by_id(data.lot_id)
        if offer:
            raise HTTPException(status_code=409, detail="Offer already exist")
        return await self.repo.create(Offers(**data.model_dump(exclude_unset=True)))

    async def update_offer(self, offer_id: int, update_data: OfferUpdate) -> OfferRead:
        offer = await self.repo.get_by_id(offer_id)
        if not offer:
            raise HTTPException(status_code=404, detail="Offer not found")
        return await self.repo.update(offer_id, update_data.model_dump(exclude_unset=True))