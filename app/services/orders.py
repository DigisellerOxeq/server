from app.repositories.orders import OrderRepository
from app.schemas import OrderRead

class OrderService:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    async def get_all_orders(self) -> list[OrderRead]:
        orders = await self.order_repo.get_all()
        return [OrderRead.from_orm(order) for order in orders]