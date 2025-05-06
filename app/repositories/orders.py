from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models import Orders

class OrderRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list[Orders]:
        result = await self.session.execute(select(Orders))
        return list(result.scalars())

