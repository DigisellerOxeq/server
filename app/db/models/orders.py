import enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum, ForeignKey

from app.db.base import Base


class Status(enum.Enum):
    pending = "pending"
    processing = "processing"
    success = "success"
    error = "error"


class Orders(Base):

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    inv: Mapped[int] = mapped_column(nullable=False, unique=True)
    unique_code: Mapped[str] = mapped_column(nullable=False, unique=True)
    lot_id: Mapped[int] = mapped_column(ForeignKey("offers.lot_id"), nullable=False)
    buyer_email: Mapped[str] = mapped_column(nullable=False)
    received: Mapped[float] = mapped_column(nullable=False)
    received_currency: Mapped[str] = mapped_column(nullable=False)
    pay_time: Mapped[int] = mapped_column(nullable=False)
    check_time: Mapped[int] = mapped_column(nullable=True)
    status: Mapped[Status] = mapped_column(Enum(Status), nullable=False)
    notation: Mapped[str] = mapped_column(nullable=True)

    offer: Mapped["Offers"] = relationship(back_populates="orders")
    goods_list: Mapped[list["Goods"]] = relationship(back_populates="order")

