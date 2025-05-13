from fastapi import APIRouter, Query
from fastapi.params import Depends

from app.integrations.digiseller import DigisellerAPI
from app.schemas.orders import OrderRead
from app.services.orders import OrderService
from app.dependencies.orders import get_order_service
from app.dependencies.auth import get_auth
from app.dependencies.digiseller import get_digiseller_api

router = APIRouter(prefix="/orders", tags=["Orders"])


# Получение всех заказов
@router.get("/get", response_model=list[OrderRead], dependencies=[Depends(get_auth)])
async def get_orders(service: OrderService = Depends(get_order_service)):
    return await service.get_all_orders()


# Создание заказа по уникальному коду Digiseller
@router.post("/create", response_model=OrderRead)
async def create_order(
    service: OrderService = Depends(get_order_service),
    digi_api: DigisellerAPI = Depends(get_digiseller_api),
    unique_code: str = Query(default=..., max_length=30),
):
    return await service.create_order(unique_code, digi_api)
