import time
from typing import Sequence

from fastapi import HTTPException, BackgroundTasks
from sqlalchemy.exc import NoResultFound

from app.core.config import settings
from app.integrations.digiseller import DigisellerAPI, DigisellerAPIError
from app.integrations.welcomegamers import WelcomeGamersAPI, WelcomeGamersAPIError
from app.repositories.orders import OrderRepository
from app.repositories.goods import GoodsRepository
from app.schemas.orders import OrderCreate, OrderRead, Status
from app.db.models.orders import Orders
from app.utils.convert_time import moscow_to_timestamp


def map_response(unique_code: str, digi_data: dict) -> Orders:
    return Orders(
        **OrderCreate(
            inv=digi_data.get("inv"),
            unique_code=unique_code,
            lot_id=digi_data.get("id_goods"),
            buyer_email=digi_data.get("email"),
            received=digi_data.get("amount"),
            received_currency=digi_data.get("type_curr"),
            pay_time=moscow_to_timestamp(digi_data.get("date_pay")),
            check_time=int(time.time()),
            status=Status.pending,
        ).model_dump()
    )


class OrderService:
    def __init__(self, order_repo: OrderRepository, goods_repo: GoodsRepository):
        self.order_repo = order_repo
        self.goods_repo = goods_repo

    async def get_all_orders(self) -> Sequence[OrderRead]:
        return await self.order_repo.get_all()

    async def get_by_unique_code(self, unique_code: str) -> OrderRead:
        order = await self.order_repo.get_by_unique_code(unique_code)
        if not order:
            raise HTTPException(status_code=404, detail="Offer not found")
        return order

    async def create_order(
        self,
        unique_code: str,
        digi_api: DigisellerAPI,
        wgamers_api: WelcomeGamersAPI,
        background_task: BackgroundTasks,
    ) -> OrderCreate:
        if existing_order := await self.order_repo.get_by_unique_code(unique_code):
            return existing_order

        try:
            token = await digi_api.get_auth_token()
            order_data = await digi_api.search_order(
                unique_code=unique_code, token=token
            )

            order = map_response(unique_code, order_data)

            if order.pay_time < settings.digi.min_pay_time:
                raise HTTPException(
                    status_code=422,
                    detail=f"Покупки старше {settings.digi.min_pay_time} не обрабатываются"
                )

            result = await self.order_repo.create(order)

        except DigisellerAPIError as e:
            raise HTTPException(
                status_code=502, detail=f"Digiseller service unavailable: {str(e)}"
            )

        background_task.add_task(self.get_goods, unique_code, wgamers_api)
        return result

    async def get_goods(self, unique_code: str, wgamers_api: WelcomeGamersAPI):
        existing_order = await self.order_repo.get_by_unique_code(unique_code)
        if not existing_order:
            return None

        try:
            await self.order_repo.change_status(
                unique_code=unique_code,
                current_status=Status.pending,
                need_status=Status.processing,
            )
        except NoResultFound:
            return None

        try:
            response = await wgamers_api.test_request()
            get_time = response["get_time"]
            values = response["values"]

        except WelcomeGamersAPIError as e:
            await self.order_repo.change_status(
                unique_code=unique_code,
                current_status=Status.pending,
                need_status=Status.error,
                notation="Ошибка получения товара",
            )
            return None

        await self.goods_repo.add_goods(
            order_code=unique_code, get_time=get_time, values=values
        )

        await self.order_repo.change_status(
            unique_code=unique_code,
            current_status=Status.processing,
            need_status=Status.success,
        )
