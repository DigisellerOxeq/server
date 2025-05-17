from fastapi import APIRouter

from app.api.orders import router as orders_router
from app.api.offers import router as offers_router

router = APIRouter(prefix="/api")

router.include_router(orders_router)
router.include_router(offers_router)
