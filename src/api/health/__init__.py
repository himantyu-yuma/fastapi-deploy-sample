from fastapi import APIRouter

from . import get_ping

router = APIRouter()
router.include_router(get_ping.router)
