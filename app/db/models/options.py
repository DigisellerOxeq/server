from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from app.db.base import Base


class Options(Base):

    __tablename__ = "options"

    id: Mapped[int] = mapped_column(primary_key=True)
    offer_id: Mapped[int] = mapped_column(ForeignKey("offers.id"), nullable=False)
    option_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    option_type: Mapped[str] = mapped_column(nullable=False)
    value: Mapped[str] = mapped_column(nullable=False)

    offer: Mapped["Offers"] = relationship(back_populates="options")
