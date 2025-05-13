from fastapi import APIRouter, Query
from fastapi.params import Depends

from app.schemas.offers import OfferRead
from app.services.orders import OrderService
from app.dependencies.orders import get_order_service
from app.dependencies.auth import get_auth

router = APIRouter(prefix="/offers", tags=["Offers"])


# Получение всех лотов
@router.get("/get", response_model=list[OfferRead], dependencies=[Depends(get_auth)])
async def get_orders(service: OrderService = Depends(get_order_service)):
    return await service.get_all_orders()
