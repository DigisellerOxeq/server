from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, SQLAlchemyError

from app.core.decorators import handle_db_errors
from app.db.models import Offers


class OfferRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    @handle_db_errors
    async def get_all(self) -> Sequence[Offers]:
        result = await self.session.scalars(select(Offers))
        return result.all()

    @handle_db_errors
    async def get_by_id(self, offer_id: int) -> Offers:
        result = await self.session.scalar(
            select(Offers).where(Offers.lot_id == offer_id)
        )
        return result

    @handle_db_errors
    async def create(self, data: Offers) -> Offers:
        self.session.add(data)
        await self.session.commit()
        return data

    @handle_db_errors
    async def update(self, offer_id: int, update_data: dict) -> Offers:
        stmt = (
            update(Offers)
            .where(Offers.id == offer_id)
            .values(**update_data)
            .returning(Offers)
        )

        result = await self.session.execute(stmt)
        offer = result.scalar_one()
        await self.session.commit()

        return offer
