import os

from deta import Deta
from dotenv import load_dotenv

load_dotenv()

DETA_KEY = os.getenv("DETA_PRODUCT_KEY")


class Database:
    """databaseを隠蔽したい"""

    def __init__(self, db_name):
        deta = Deta(DETA_KEY)
        self.deta = deta
        self.base = deta.Base(db_name)

    def close():
        pass

    def insert_one(self, table_name, data):
        if table_name == "item":
            return self.base.put({"name": "トリケラトプス", "price": "9980"})
        return data

    def insert_many(self, data):
        pass

    def find(self, query):
        return {"query": query}

    def __del__(self):
        self.close()


db = Database("test")
