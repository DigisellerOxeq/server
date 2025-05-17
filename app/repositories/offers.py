from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, SQLAlchemyError

from app.db.models import Offers


class OfferRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> Sequence[Offers]:
        result = await self.session.scalars(select(Offers))
        return result.all()
