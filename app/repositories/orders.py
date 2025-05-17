from typing import Sequence

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, SQLAlchemyError
from sqlalchemy.orm import joinedload

from app.db.models import Orders


class OrderRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> Sequence[Orders]:
        result = await self.session.scalars(
            select(Orders).options(joinedload(Orders.offer))
        )
        return result.all()

    async def get_by_unique_code(self, unique_code: Orders.unique_code) -> Orders:
        result = await self.session.execute(
            select(Orders)
            .options(joinedload(Orders.offer))
            .where(Orders.unique_code == unique_code)
        )
        return result.scalar_one_or_none()

    async def create(self, order: Orders) -> Orders:
        try:
            self.session.add(order)
            await self.session.commit()
            await self.session.refresh(order, ["offer"])
            return order
        except SQLAlchemyError as e:
            await self.session.rollback()
            raise HTTPException(
                status_code=400, detail=f"Failed to create order: {str(e)}"
            )
