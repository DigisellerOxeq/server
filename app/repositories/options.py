from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.decorators import handle_db_errors
from app.core.exceptions import NotFoundError
from app.db.models import Options


class OptionsRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    @handle_db_errors
    async def get_all(self) -> Sequence[Options]:
        result = await self.session.scalars(select(Options))
        return result.all()

    @handle_db_errors
    async def get_by_offer_id(self, offer_id: int) -> Sequence[Options]:
        result = await self.session.scalars(
            select(Options).where(Options.offer_id == offer_id)
        )
        return result.all()

    @handle_db_errors
    async def get_by_id(self, id: int) -> Options:
        result = await self.session.scalar(
            select(Options).where(Options.id == id)
        )
        return result

    @handle_db_errors
    async def create(self, data: Options) -> Options:
        self.session.add(data)
        await self.session.commit()
        return data

    @handle_db_errors
    async def delete(self, id: int) -> bool:
        result = await self.session.scalar(
            select(Options).where(Options.id == id)
        )

        if not result:
            raise NotFoundError

        await self.session.delete(result)
        await self.session.commit()
        return True

