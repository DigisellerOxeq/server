from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models import Orders

class OrderRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> Sequence[Orders]:
        result = await self.session.scalars(select(Orders))
        return result.all()

    async def get_by_unique_code(self, unique_code: Orders.unique_code) -> Orders:
        result = await self.session.execute(select(Orders).where(Orders.unique_code==unique_code))
        return result.scalar_one_or_none()


