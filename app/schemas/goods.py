from pydantic import BaseModel


class Goods(BaseModel):
    value: str
    get_time: int