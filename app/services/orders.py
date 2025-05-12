from typing import Sequence

from app.core.config import settings
from app.repositories.orders import OrderRepository
from app.schemas import OrderRead
from app.integrations.digiseller import DigisellerAPI


class OrderService:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    async def get_all_orders(self) -> Sequence[OrderRead]:
        return await self.order_repo.get_all()

    async def create_order(self, unique_code):
        if self.order_repo.get_by_unique_code(unique_code=unique_code):
            return False







        return None
