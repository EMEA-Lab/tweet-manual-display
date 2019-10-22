from pymongo import MongoClient

import os

DB_URL = os.environ.get('DB_URL', None)
DB_PORT = os.environ.get('DB_PORT', None)
DB_USERNAME = os.environ.get('DB_USERNAME', None)
DB_KEY = os.environ.get('DB_KEY', None) 
DB_NAME = os.environ.get('DB_NAME', None) 

client = MongoClient(DB_URL, int(DB_PORT), retryWrites = False)
db = client[DB_NAME]
db.authenticate(DB_USERNAME, DB_KEY)
	
def addTweetIfNew(tweetID, tweetData):
        
    #check if tweet exists in collection
    currentTweet = db.entries.find_one({'tweet_id' : tweetID})	    
    	    	    
    if currentTweet is None:
    
        newData = {
            'tweet_id': tweetID,
            'tweetData': tweetData,
        }
        
        db.entries.insert(newData)
        
        return True
    else:
        return False