from email.policy import default
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env.local")

MONGO_URL = os.environ.get("MONGO_URL", "mongo")
MONGO_USERNAME = os.environ.get("MONGO_USERNAME", "root")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "")
MONGO_PORT = os.environ.get("MONGO_PORT", 27017)

mongo_client = MongoClient(
    host=MONGO_URL,
    username=MONGO_USERNAME,
    password=MONGO_PASSWORD,
    port=MONGO_PORT,  # add ',' at the end to keep it on multiple lines
)


# def insert_test_document():
#   """Inserts sample document to the test_collection"""
#     db = mongo_client.gallery
#     test_collection = db.images_collection
#     res = test_collection.insert_one({"name": "Jonathan", "instructor": False})
#     print(res)
