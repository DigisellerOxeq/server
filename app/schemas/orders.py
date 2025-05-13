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

    id: Optional[int] = None
    inv: int
    unique_code: str
    buyer_email: str
    received: float
    received_currency: str
    pay_time: int
    check_time: Optional[int] = None
    status: Status
    notation: Optional[str] = None

    offer: OfferRead
