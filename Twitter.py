from flask import Blueprint, Response
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

    #dump to console for debugging purposes
    print(json.dumps(requestJson, indent=4, sort_keys=True))
    
    tweetURL = requestJson['tweetURL']
    
    #Get tweet details then commit to DB if valid
    #HERE
    
    return ('', HTTPStatus.OK)    
