from fastapi import APIRouter

from app.api.orders import router as orders_router

router = APIRouter(
    prefix='/api'
)

router.include_router(orders_router)