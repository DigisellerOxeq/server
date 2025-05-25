from typing import Sequence
import time

from fastapi import HTTPException
from app.db.models.offers import Offers
from app.repositories.options import OptionsRepository
from app.schemas.options import Options


class OptionsService:
    def __init__(self, offer_repo: OptionsRepository):
        self.repo = offer_repo

    async def get_all_options(self) -> Sequence[Options]:
        return await self.repo.get_all()

    async def get_by_offer_id(self, offer_id: int) -> Sequence[Options]:
        offer = await self.repo.get_by_offer_id(offer_id)
        if not offer:
            raise HTTPException(status_code=404, detail="Offer not found")
        return offer

    async def add_option(self, data: Options) -> Options:
        offer = await self.repo.get_by_option_id(data.lot_id)
        if offer:
            raise HTTPException(status_code=409, detail="Offer already exist")

        db_offer_data = data.model_dump()
        return await self.repo.create(Offers(**db_offer_data))

    async def delete_option(self, option_id: int) -> bool:
        return await self.repo.delete(option_id)
