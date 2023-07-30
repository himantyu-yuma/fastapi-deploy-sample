from fastapi import APIRouter

from src.db.database import db

router = APIRouter()


@router.get("/items/{item_id}")
def read_item(item_id: str, q: str = None):
    item = db.find({"item_id": item_id})
    return item
