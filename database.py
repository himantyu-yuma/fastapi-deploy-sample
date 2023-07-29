import os

from deta import Deta
from dotenv import load_dotenv

load_dotenv()

DETA_PRODUCT_KEY = os.environ.get("DETA_PRODUCT_KEY")
deta = Deta(DETA_PRODUCT_KEY)


class Database:
    """databaseを隠蔽したい"""

    def __init__(self, db_name, table_name):
        self.base = deta.Base(db_name)

    def close():
        pass

    def insert_one(self, data):
        self.base.put(data)
        return "success"

    def insert_many(self, data):
        pass

    def find(self, query):
        """
        ref: https://deta.space/docs/en/build/reference/deta-base/queries
        """
        res = self.base.fetch(query)
        return res.items


if __name__ == "__main__":
    db = Database("Items", "")
    db.base.put({"name": "test"})
    # print(db.base.get())
