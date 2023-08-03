# from dataclasses import dataclass

from src.db.database import db

# @dataclass
# class ItemType:
#     name: str
#     price: float


class Item:
    def __init__(self, name: str, price: int, key: str):
        self.key = key
        self.name = name
        self.price = int(price)

    def Find(id: str):
        db_item = db.find(table_name="item", id=id)
        item = Item(**db_item)
        return item

    def Save():
        result = db.insert_one(
            table_name="item", data={"name": "トリケラトプス", "price": "9980"}
        )
        return result
