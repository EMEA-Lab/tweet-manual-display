from flask import Blueprint, Response, request
from TwitterAPI import TwitterAPI
from http import HTTPStatus

from utils import DBHandler

import os, json, requests

CONSUMER_KEY = os.environ.get('CONSUMER_KEY', None)
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET', None)

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', None)
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET', None)

twitter = Blueprint('twitter', __name__)

def initApiObject():
    
    #user authentication
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)    
    
    return api	
    			
@twitter.route("/add-tweet", methods=["POST"])
def addTweetRecieved():    
	  		
    requestJson = request.get_json()

    #dump to console for debugging purposs
    print(json.dumps(requestJson, indent=4, sort_keys=True))
    
    tweetID = requestJson['tweetID']
    
    twitterAPI = initApiObject()
            
    r = twitterAPI.request('statuses/show/:%d' % int(tweetID))    

    print(r.json())
    
    if r.status_code == 200:
    
        #save tweet
        isNew = DBHandler.addTweetIfNew(tweetID, r.json())  
        
        if isNew == True:
            return Response(json.dumps({'message': 'Successfully added'}),  mimetype='application/json')  
        else:
            return Response(json.dumps({'message': 'Already added'}),  mimetype='application/json')                  

    else:
        return Response(json.dumps({'message': 'Twitter API error'}),  mimetype='application/json')      
        
        
    return ('', HTTPStatus.OK)
    
    
