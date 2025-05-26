from __future__ import annotations

import enum

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum

from app.db.base import Base


class LotType(enum.Enum):
    telegram_stars = "telegram"
    steam_cards = "steam"
    itunes_cards = "itunes"


class Offers(Base):

    __tablename__ = "offers"

    id: Mapped[int] = mapped_column(primary_key=True)
    lot_id: Mapped[int] = mapped_column(nullable=False, unique=True, index=True)
    lot_type: Mapped[str] = mapped_column(Enum(LotType), nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False)
    add_time: Mapped[int] = mapped_column(nullable=False)

    orders: Mapped[list["Orders"]] = relationship(back_populates="offer")
    options: Mapped[list["Options"]] = relationship(back_populates="offer")