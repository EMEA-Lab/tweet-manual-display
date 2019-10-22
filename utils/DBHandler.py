from pymongo import MongoClient

import os

DB_URL = os.environ.get('DB_URL', None)
DB_PORT = os.environ.get('DB_PORT', None)
DB_USERNAME = os.environ.get('DB_USERNAME', None)
DB_KEY = os.environ.get('DB_KEY', None) 
DB_NAME = os.environ.get('DB_NAME', None) 

client = MongoClient(DB_URL, DB_PORT)
db = client[DB_NAME]
db.authenticate(DB_USERNAME, DB_KEY)

def findOne(lookup):
	
	return db.entries.find_one(lookup)	