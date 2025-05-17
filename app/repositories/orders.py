from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, SQLAlchemyError
from sqlalchemy.orm import joinedload

from app.core.decorators import handle_db_errors
from app.db.models import Orders


class OrderRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    @handle_db_errors
    async def get_all(self) -> Sequence[Orders]:
        result = await self.session.scalars(
            select(Orders).options(joinedload(Orders.offer))
        )
        return result.all()

    @handle_db_errors
    async def get_by_unique_code(self, unique_code: str) -> Orders:
        result = await self.session.execute(
            select(Orders)
            .options(joinedload(Orders.offer))
            .where(Orders.unique_code == unique_code)
        )
        return result.scalar()

    @handle_db_errors
    async def create(self, order: Orders) -> Orders:
        self.session.add(order)
        await self.session.commit()
        await self.session.refresh(order, ["offer"])
        return order

