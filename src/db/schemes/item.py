from dataclasses import dataclass

from src.db.database import Database


@dataclass
class Item:
    key: str = ""
    name: str = ""
    price: int = 0


db_item = Database(Item())
