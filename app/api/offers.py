from fastapi import APIRouter
from fastapi.params import Depends

from app.schemas.offers import OfferRead, OfferCreate, OfferUpdate
from app.services.offers import OfferService
from app.dependencies.offers import get_offer_service
from app.dependencies.auth import get_auth

router = APIRouter(prefix="/offers", tags=["Offers"])


# Получение всех лотов
@router.get("/", response_model=list[OfferRead], dependencies=[Depends(get_auth)])
async def get_offers(service: OfferService = Depends(get_offer_service)):
    return await service.get_all_offers()


# Получение всех лота по ID
@router.get("/{offer_id}", response_model=OfferRead, dependencies=[Depends(get_auth)])
async def get_offer_by_id(
    offer_id: int, service: OfferService = Depends(get_offer_service)
):
    return await service.get_by_offer_id(offer_id)


# Создание лота
@router.post("/", response_model=OfferRead, dependencies=[Depends(get_auth)])
async def create_offer(
    data: OfferCreate, service: OfferService = Depends(get_offer_service)
):
    return await service.create_offer(data)


# Изменение лота
@router.patch("/{offer_id}", response_model=OfferRead, dependencies=[Depends(get_auth)])
async def update_offer(
    offer_id: int, data: OfferUpdate, service: OfferService = Depends(get_offer_service)
):
    return await service.update_offer(offer_id, data)
