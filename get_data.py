import os
import sys
import json


from dotenv import load_dotenv


import certifi
import pandas as pd
import numpy as np
from pymongo 
import MongoClient
from networksecurity.exception import NetworkSecurityException  
from networksecurity.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            load_dotenv()
            self.mongo_uri = os.getenv("MONGO_URI")
            self.mongo_db = os.getenv("MONGO_DB")
            self.mongo_collection = os.getenv("MONGO_COLLECTION")
            self.client = MongoClient(self.mongo_uri, tlsCAFile=certifi.where())
            self.db = self.client[self.mongo_db]
            self.collection = self.db[self.mongo_collection]
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    def csv_to_json(self, csv_file_path: str) -> list:
        try:
            df = pd.read_csv(csv_file_path)
            json_data = df.to_dict(orient='records')
            return json_data
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
    
    def pushing_data_to_mongodb(self, data: list):
        try:
            if isinstance(data, list):
                self.collection.insert_many(data)
            else:
                raise NetworkSecurityException("Data should be a list of dictionaries", sys)
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e


    