from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import db_helper
from app.repositories.offers import OfferRepository
from app.services.offers import OfferService


def get_offer_service(
    session: AsyncSession = Depends(db_helper.session_getter),
) -> OfferService:
    repo = OfferRepository(session)
    return OfferService(repo)
