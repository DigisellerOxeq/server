from typing import Optional

from pydantic import BaseModel


class OptionsCreate(BaseModel):
    offer_id: int
    option_id: int
    platform: Optional[str]
    nominal: Optional[float]
    currency: Optional[str]

class OptionsRead(BaseModel):
    id: int
    offer_id: int
    option_id: int
    platform: Optional[str]
    nominal: Optional[float]
    currency: Optional[str]

