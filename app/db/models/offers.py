from __future__ import annotations

import enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum

from app.db.base import Base


class LotType(enum.Enum):
    telegram_stars = "telegram_stars"
    steam_cards = "steam_cards"
    itunes_cards = "itunes_cards"


class Status(enum.Enum):
    active = "active"
    inactive = "inactive"


class Offers(Base):

    __tablename__ = "offers"

    id: Mapped[int] = mapped_column(primary_key=True)
    lot_id: Mapped[int] = mapped_column(nullable=False, unique=True, index=True)
    lot_type: Mapped[str] = mapped_column(Enum(LotType), nullable=False)
    status: Mapped[str] = mapped_column(Enum(Status), nullable=False)
    add_time: Mapped[int] = mapped_column(nullable=False)

    orders: Mapped[list["Orders"]] = relationship(back_populates="offer")
