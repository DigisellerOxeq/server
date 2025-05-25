from fastapi import APIRouter
from fastapi.params import Depends

from app.schemas.options import OptionsCreate, OptionsRead
from app.services.options import OptionsService
from app.dependencies.options import get_options_service
from app.dependencies.auth import get_auth

router = APIRouter(prefix="/options", tags=["Options"])


# Получение всех опций
@router.get("/", response_model=list[OptionsRead], dependencies=[Depends(get_auth)])
async def get_options(service: OptionsService = Depends(get_options_service)):
    return await service.get_all_options()


# Получение всех опций по offer_id
@router.get("/{offer_id}", response_model=list[OptionsRead], dependencies=[Depends(get_auth)])
async def get_option_by_id(
    offer_id: int, service: OptionsService = Depends(get_options_service)
):
    return await service.get_by_offer_id(offer_id)


# Добавление опции
@router.post("/", response_model=OptionsRead, dependencies=[Depends(get_auth)])
async def create_option(
    data: OptionsCreate, service: OptionsService = Depends(get_options_service)
):
    return await service.add_option(data)


# Удаление опции
@router.delete("/{offer_id}", dependencies=[Depends(get_auth)])
async def delete_option(
    option_id: int, service: OptionsService = Depends(get_options_service)
):
    return await service.delete_option(option_id)
