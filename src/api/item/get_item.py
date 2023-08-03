from fastapi import APIRouter

from src.repos.item import Item

router = APIRouter()


@router.get("/items/{item_id}")
def read_item(item_id: str):
    item = Item.Find(id=item_id)
    return item
