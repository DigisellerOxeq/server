from pydantic import BaseModel


class Options(BaseModel):
    offer_id: int
    option_id: int
    option_type: str
    value: str

