import os
import sys

import certifi
import pymongo

from src.constants import *
from src.exception import MyException
from src.logger import logging

ca = certifi.where()


class MongoDBClient:

    client = None

    def __init__(self, database_name: str = DB_NAME) -> None:

        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Mongo db url is not assigned")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successful..")

        except Exception as e:
            raise MyException(e, sys)
