from pydantic import BaseModel


class OptionsCreate(BaseModel):
    offer_id: int
    option_id: int
    option_type: str
    value: str

class OptionsRead(BaseModel):
    id: int
    offer_id: int
    option_id: int
    option_type: str
    value: str

