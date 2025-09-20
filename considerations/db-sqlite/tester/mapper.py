import logging
import sqlite3
import os


logger = logging.getLogger(__package__)


class SQLMapper:
    def __init__(self, db_path: str, queries_folder: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.queries = {}
        self._load_queries(queries_folder)

    def _load_queries(self, folder: str):
        for file in os.listdir(folder):
            if file.endswith('.sql'):
                name = os.path.splitext(file)[0]
                path = os.path.join(folder, file)
                with open(path, 'r') as f:
                    self.queries[name] = f.read().removesuffix('\n')

    def execute(self, query_name: str, params: tuple = ()):
        sql = self.queries.get(query_name)
        if sql is None:
            raise ValueError(f"No query found for '{query_name}'")

        logger.info(sql)
        return self.cursor.execute(sql, params)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
