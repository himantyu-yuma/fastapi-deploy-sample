import os

from deta import Deta
from dotenv import load_dotenv

load_dotenv()

DETA_KEY = os.getenv("DETA_PRODUCT_KEY")


class Database:
    """databaseを隠蔽したい"""

    def __init__(self, Scheme):
        deta = Deta(DETA_KEY)
        class_name = Scheme.__class__.__name__
        self.deta = deta
        self.base = deta.Base(class_name)

    def insert_one(self, data: dict):
        return self.base.put(data)

    def insert_many(self, data: list[dict]):
        return self.base.put(data)

    def find(self, id):
        return self.base.get(id)
