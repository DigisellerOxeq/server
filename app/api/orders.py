from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import db_helper
from app.schemas.orders import OrderRead
from app.repositories.orders import OrderRepository

router = APIRouter(
    prefix='/orders',
    tags=['Orders']
)

@router.get('/get', response_model=list[OrderRead])
async def get_orders(
        session: AsyncSession = Depends(db_helper.session_getter),
):
    repo = OrderRepository(session)
    result = await repo.get_all()

    return result