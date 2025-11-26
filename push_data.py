import os 
import sys 
import json
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging
load_dotenv()
MANGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MANGO_DB_URL)
import certifi
ca = certifi.where()


# creating our class

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)
    def cv_to_json_convertor(self, filepath):
        try:
            data = pd.read_csv(filepath)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e, sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = pymongo.MongoClient(MANGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "MOSAMIR"
    collection = 'NetworkData'
    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json_convertor(filepath=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records=records, database=DATABASE, collection=collection)
    print(no_of_records)