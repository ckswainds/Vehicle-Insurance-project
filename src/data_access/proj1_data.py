import sys
from typing import Optional

import numpy as np
import pandas as pd

from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import *
from src.exception import MyException


class Proj1data:

    def __init__(self) -> None:
        try:
            self.mongo_client = MongoDBClient(database_name=DB_NAME)
        except Exception as e:
            raise MyException(e, sys)

    def export_collection_as_dataframe(
        self,
        collection_name: str,
        database_name: Optional[str] = None,
    ) -> pd.DataFrame:

        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collecion = self.mongo_client[database_name][collection_name]

            print("Fetching data from MongoDB")
            df = pd.DataFrame(list(collection.find()))
            if "id" in df.columns.to_list():
                df = df.drop(columns=["id"], axis=1)
            df.replace({"na": np.nan}, inplace=True)
            return df

        except Exception as e:
            raise MyException(e, sys)
