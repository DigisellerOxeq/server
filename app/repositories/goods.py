from sqlalchemy.ext.asyncio import AsyncSession

from app.core.decorators import handle_db_errors
from app.db.models import Goods


class GoodsRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    @handle_db_errors
    async def add_goods(self, order_code: str, get_time: int, values: list[str]) -> None:
        goods_objects = []
        for value in values:
            goods_objects.append(
                Goods(
                    order_code=order_code,
                    get_time=get_time,
                    value=value
                )
            )

        self.session.add_all(goods_objects)
        await self.session.commit()