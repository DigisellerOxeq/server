from fastapi import APIRouter, Query
from fastapi.params import Depends

from app.schemas.orders import OrderRead
from app.services.orders import OrderService
from app.dependencies.orders import get_order_service
from app.dependencies.auth import get_auth

router = APIRouter(prefix="/orders", tags=["Orders"])


# Получение всех заказов
@router.get("/get", response_model=list[OrderRead], dependencies=[Depends(get_auth)])
async def get_orders(service: OrderService = Depends(get_order_service)):
    return await service.get_all_orders()


# Создание заказа по уникальному коду Digiseller
@router.post("/create")
async def check_unique_code(
    service: OrderService = Depends(get_order_service),
    unique_code: str = Query(default=..., max_length=30),
):
    return await service.create_order()
