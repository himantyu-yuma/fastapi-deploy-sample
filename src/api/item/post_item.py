from fastapi import APIRouter

from src.repos.item import Item

router = APIRouter()


@router.post("/api/items")
def update_items(item: Item):
    result = Item.Save({"name": item.name, "price": item.price})
    return result
