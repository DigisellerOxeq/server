from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import db_helper
from app.repositories.options import OptionsRepository
from app.services.options import OptionsService


def get_options_service(
    session: AsyncSession = Depends(db_helper.session_getter),
) -> OptionsService:
    repo = OptionsRepository(session)
    return OptionsService(repo)
