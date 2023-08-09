from fastapi import APIRouter

from . import health, item

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(item.router, tags=["item"])
