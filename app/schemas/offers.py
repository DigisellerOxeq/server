from pydantic import BaseModel
from enum import Enum
from typing import Optional, List

from app.schemas.options import OptionsRead


class LotType(str, Enum):
    telegram = "telegram"
    steam = "steam"
    itunes = "itunes"


class OfferRead(BaseModel):
    id: int
    lot_id: int
    lot_type: LotType
    add_time: int
    is_active: bool
    options: List[OptionsRead]


class OfferCreate(BaseModel):
    lot_id: int
    lot_type: LotType


class OfferUpdate(BaseModel):
    lot_type: Optional[LotType] = None
    add_time: Optional[int] = None
    is_active: Optional[bool] = None
