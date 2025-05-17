from typing import Sequence

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, SQLAlchemyError

from app.db.models import Offers


class OfferRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> Sequence[Offers]:
        result = await self.session.scalars(select(Offers))
        return result.all()

    async def get_by_id(self, offer_id: int) -> Offers:
        result = await self.session.execute(
            select(Offers).where(Offers.lot_id == offer_id)
        )
        return result.scalar_one_or_none()

    async def create(self, data: Offers) -> Offers:
        try:
            self.session.add(data)
            await self.session.commit()
            return data
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise HTTPException(
                status_code=400, detail=f"Failed to create order: {str(e)}"
            )
