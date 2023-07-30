class Database:
    """databaseを隠蔽したい"""

    def __init__(self, db_name, table_name):
        pass

    def close():
        pass

    def insert_one(self, data):
        return data

    def insert_many(self, data):
        pass

    def find(self, query):
        return {"query": query}

    def __del__(self):
        self.close()
