from fastapi import APIRouter

from . import get_item, post_item

router = APIRouter()
router.include_router(get_item.router)
router.include_router(post_item.router)
