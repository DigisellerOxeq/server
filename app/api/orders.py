from fastapi import APIRouter, BackgroundTasks
from fastapi.params import Depends

from app.integrations.digiseller import DigisellerAPI
from app.schemas.orders import OrderRead
from app.services.orders import OrderService
from app.dependencies.orders import get_order_service
from app.dependencies.auth import get_auth
from app.dependencies.clients import get_digiseller_api

router = APIRouter(prefix="/orders", tags=["Orders"])


# Получение всех заказов
@router.get("/", response_model=list[OrderRead], dependencies=[Depends(get_auth)])
async def get_all_orders(service: OrderService = Depends(get_order_service)):
    return await service.get_all_orders()


# Получение заказа по unique code
@router.get(
    "/{unique_code}", response_model=list[OrderRead], dependencies=[Depends(get_auth)]
)
async def get_by_unique_code(
    unique_code: str, service: OrderService = Depends(get_order_service)
):
    return await service.get_by_unique_code(unique_code)


# Создание заказа по уникальному коду Digiseller
@router.post("/{unique_code}", response_model=OrderRead)
async def create_order(
    background_tasks: BackgroundTasks,
    unique_code: str,
    service: OrderService = Depends(get_order_service),
    digi_api: DigisellerAPI = Depends(get_digiseller_api),
):
    return await service.create_order(unique_code, digi_api, BackgroundTasks)
