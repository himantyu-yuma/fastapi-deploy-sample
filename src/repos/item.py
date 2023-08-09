from pydantic import BaseModel

from src.db.schemes.item import db_item


class Item(BaseModel):
    key: str = ""
    name: str
    price: int

    def Find(id: str):
        item = db_item.find(id=id)
        result = Item(**item)
        return result

    def Save(req: dict):
        result = db_item.insert_one(data=req)
        return result
