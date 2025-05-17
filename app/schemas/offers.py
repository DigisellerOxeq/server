from pydantic import BaseModel
from enum import Enum
from typing import Optional


class LotType(str, Enum):
    telegram_stars = "telegram_stars"
    steam_cards = "steam_cards"
    itunes_cards = "itunes_cards"


class Status(str, Enum):
    active = "active"
    inactive = "inactive"


class OfferRead(BaseModel):
    lot_id: int
    lot_type: LotType
    add_time: int
    status: Status


class OfferCreate(BaseModel):
    lot_id: int
    lot_type: LotType


class OfferUpdate(BaseModel):
    lot_id: int
    lot_type: Optional[LotType] = None
    add_time: Optional[int] = None
    status: Optional[Status] = None
