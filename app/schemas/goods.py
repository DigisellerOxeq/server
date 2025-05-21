from pydantic import BaseModel


class Goods(BaseModel):
    id: int
    order_code: str
    value: str
    get_time: int