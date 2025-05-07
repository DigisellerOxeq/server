from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import db_helper
from app.repositories.orders import OrderRepository
from app.services.orders import OrderService

def get_order_service(
    session: AsyncSession = Depends(db_helper.session_getter),
) -> OrderService:
    repo = OrderRepository(session)
    return OrderService(repo)