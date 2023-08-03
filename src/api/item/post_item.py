from fastapi import APIRouter

from src.repos.item import Item

router = APIRouter()


@router.post("/api/items")
def update_items(req: str):
    result = Item.Save()
    return result
