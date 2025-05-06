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

