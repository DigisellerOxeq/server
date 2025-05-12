from typing import Optional
from pydantic import BaseModel

from enum import Enum


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
    unique_code: str
    lot_type: str
    buyer_email: str
    received: float
    received_currency: str
    pay_time: int
    check_time: Optional[int] = None
    status: Status
    notation: Optional[str] = None
