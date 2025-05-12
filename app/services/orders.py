from typing import Sequence

from fastapi import HTTPException

from app.integrations.digiseller import DigisellerAPI, DigisellerAPIError
from app.repositories.orders import OrderRepository
from app.schemas import OrderRead


class OrderService:
    def __init__(self, order_repo: OrderRepository):
        self.order_repo = order_repo

    async def get_all_orders(self) -> Sequence[OrderRead]:
        return await self.order_repo.get_all()

    async def create_order(
        self, unique_code: str, digi_api: DigisellerAPI
    ) -> OrderRead:
        if existing_order := await self.order_repo.get_by_unique_code(unique_code):
            return existing_order

        try:
            token = await digi_api.get_auth_token()
            order_data = await digi_api.search_order(
                unique_code=unique_code, token=token
            )
            print(order_data)
            order = self._map_digi_response_to_order(unique_code, order_data)
            return await self.order_repo.create(order)

        except DigisellerAPIError as e:
            raise HTTPException(
                status_code=502, detail=f"Digiseller service unavailable: {str(e)}"
            )

    def _map_digi_response_to_order(
        self, unique_code: str, digi_data: dict
    ) -> OrderRead:
        return OrderRead(
            id=digi_data.get("order_id"),
            unique_code=unique_code,
        )
