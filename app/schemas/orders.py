from typing import Optional
from pydantic import BaseModel
from enum import Enum

from offers import OfferRead


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