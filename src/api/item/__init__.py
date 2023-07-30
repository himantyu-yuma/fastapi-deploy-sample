from fastapi import APIRouter

from . import get_item

router = APIRouter()
router.include_router(get_item.router)
