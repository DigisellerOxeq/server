from typing import Sequence

from fastapi import HTTPException
from app.schemas.options import OptionsCreate
from app.db.models.options import Options
from app.repositories.options import OptionsRepository


class OptionsService:
    def __init__(self, offer_repo: OptionsRepository):
        self.repo = offer_repo

    async def get_all_options(self) -> Sequence[Options]:
        return await self.repo.get_all()

    async def get_by_offer_id(self, offer_id: int) -> Sequence[Options]:
        offer = await self.repo.get_by_offer_id(offer_id)
        if not offer:
            raise HTTPException(status_code=404, detail="Options not found")
        return offer

    async def add_option(self, data: OptionsCreate) -> Options:
        options = await self.repo.get_by_option_id(data.option_id)
        if options:
            raise HTTPException(status_code=409, detail="Options already exist")

        db_options_data = data.model_dump()
        return await self.repo.create(Options(**db_options_data))

    async def delete_option(self, option_id: int) -> bool:
        return await self.repo.delete(option_id)
