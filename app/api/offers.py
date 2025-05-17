from fastapi import APIRouter
from fastapi.params import Depends

from app.schemas.offers import OfferRead, OfferCreate, OfferUpdate
from app.services.orders import OrderService
from app.dependencies.offers import get_offer_service
from app.dependencies.auth import get_auth

router = APIRouter(prefix="/offers", tags=["Offers"])


# Получение всех лотов
@router.get("/get", response_model=list[OfferRead], dependencies=[Depends(get_auth)])
async def get_orders(service: OrderService = Depends(get_offer_service)):
    return await service.get_all_orders()


# Добавление лота
@router.post("/add", dependencies=[Depends(get_auth)])
async def get_orders(
    data: OfferCreate, service: OrderService = Depends(get_offer_service)
):
    return await service.edit_offer(update_data)


# Изменение лота
@router.patch("/edit", dependencies=[Depends(get_auth)])
async def edit_order(
    data: OfferUpdate, service: OrderService = Depends(get_offer_service)
):
    return await service.edit_offer(update_data)
