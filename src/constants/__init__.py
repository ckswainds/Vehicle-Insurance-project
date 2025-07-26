import os
from datetime import date

# MongoDB constants
DB_NAME = "Vehicle_DataBase"
MONGODB_URL_KEY = "MONGODB_URL"
COLLECTION_NAME = "vehicledata"

# $env:MONGODB_URL = "mongodb+srv://chandankumarswain3467:L7YPbvbCD1tfNTtV@cluster0.ukd05il.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# echo $env:MONGODB_URL

PIPELINE_NAME: str = ""
ARTIFACT_DIR: str = "artifact"

MODEL_FILE_NAME: str = "model.pkl"

TARGET_COLUMN = "Response"
CURRENT_YEAR = date.today().year
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"


FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

# Data ingestion constants
DATA_INGESTION_COLLECTION_NAME: str = "vehicledata"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25
