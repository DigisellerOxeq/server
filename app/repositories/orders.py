from typing import Sequence

from app.core.exceptions import NotFoundError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.core.decorators import handle_db_errors
from app.db.models import Orders
from app.db.models.orders import Status


class OrderRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    @handle_db_errors
    async def get_all(self) -> Sequence[Orders]:
        result = await self.session.scalars(
            select(Orders)
            .options(
                joinedload(Orders.offer),
                joinedload(Orders.goods_list)
            )
        )
        return result.all()

    @handle_db_errors
    async def get_by_unique_code(self, unique_code: str) -> Orders:
        result = await self.session.execute(
            select(Orders)
            .options(
                joinedload(Orders.offer),
                joinedload(Orders.goods_list)
            )
            .where(Orders.unique_code == unique_code)
        )
        return result.scalar()

    @handle_db_errors
    async def create(self, order: Orders) -> Orders:
        self.session.add(order)
        await self.session.commit()
        await self.session.refresh(order, ["offer", "goods_list"])
        return order


    @handle_db_errors
    async def change_status(self, unique_code: str, current_status: str, need_status: Status, notation: str = None) -> Orders:
            result = await self.session.execute(
                select(Orders)
                .where(
                    (Orders.unique_code == unique_code) &
                    (Orders.status == current_status)
                )
                .options(
                    joinedload(Orders.offer),
                    joinedload(Orders.goods_list)
                )
                .where(Orders.unique_code == unique_code)
            )

            order = result.scalar()
            if not order:
                raise NotFoundError()

            order.status = need_status
            if notation:
                order.notation = notation

            await self.session.commit()
            return order