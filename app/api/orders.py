from fastapi import APIRouter
from fastapi.params import Depends

from app.schemas.orders import OrderRead
from app.services.orders import OrderService
from app.dependencies.orders import get_order_service
from app.dependencies.auth import get_auth

router = APIRouter(
    prefix='/orders',
    tags=['Orders']
)


@router.get("/get", response_model=list[OrderRead], dependencies=[Depends(get_auth)])
async def get_orders(service: OrderService = Depends(get_order_service)):
    return await service.get_all_orders()