from pymongo import MongoClient

import os

USER = str(os.environ.get('MLAB_NAME', None))
PASS = str(os.environ.get('MLAB_PASS', None))

client = MongoClient('mongodb+srv://' + USER + ':' + PASS + '@tweet-display.t3de1.mongodb.net/tweet-display?retryWrites=true&w=majority')
db = client['tweet-display']

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
        
def getLatestTweet():
    
    tweet = list(db.entries.find().limit(1).sort([( '$natural', -1 )]))[0]
    
    if tweet is None:
    
        return False
    else:
        return tweet
