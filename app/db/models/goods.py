from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from app.db.base import Base


class Goods(Base):

    __tablename__ = "goods"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_code: Mapped[str] = mapped_column(ForeignKey("orders.unique_code"), nullable=False)
    value: Mapped[str] = mapped_column(nullable=False)
    get_time: Mapped[int] = mapped_column(nullable=False)

    order: Mapped["Orders"] = relationship(back_populates="goods_list")

