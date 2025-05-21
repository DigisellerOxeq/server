from typing import Optional, List
from pydantic import BaseModel
from enum import Enum

from app.schemas.offers import OfferRead
from app.schemas.goods import Goods


# Статусы заказов
class Status(str, Enum):
    pending = "pending"
    processing = "processing"
    success = "success"
    error = "error"


# Получение информации о заказе
class OrderRead(BaseModel):
    id: int
    inv: int
    lot_id: int
    unique_code: str
    buyer_email: str
    received: float
    received_currency: str
    pay_time: int
    check_time: int
    status: Status
    notation: Optional[str] = None

    offer: Optional[OfferRead] = None
    goods_list: List[Goods] = []


# Создание заказа
class OrderCreate(BaseModel):
    inv: int
    unique_code: str
    lot_id: int
    buyer_email: str
    received: float
    received_currency: str
    pay_time: int
    check_time: int
    status: Status
    notation: Optional[str] = None
