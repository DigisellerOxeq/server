from pydantic import BaseModel
from enum import Enum
from typing import Optional


class LotType(str, Enum):
    telegram_stars = "telegram_stars"
    steam_cards = "steam_cards"
    itunes_cards = "itunes_cards"


class OfferRead(BaseModel):
    lot_id: int
    lot_type: LotType
    add_time: int