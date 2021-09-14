#!/usr/bin/env python
from functools import wraps
from flask import request, Response, Flask, send_from_directory

import os

#import other module blueprints
from Twitter import twitter
	     
app = Flask(__name__)

AUTH_USER = os.environ.get('SIMPLE_AUTH_USER', None)
AUTH_PASS = os.environ.get('SIMPLE_AUTH_PASS', None)

##############################################
#########    BASIC AUTH WRAPPER   ############
##############################################

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == AUTH_USER and password == AUTH_PASS

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

##############################################
#########   END BASIC AUTH WRAPPER   #########
##############################################

#register other module blueprints
app.register_blueprint(twitter)

@app.route('/')
def default_route():
    
    return send_from_directory('www', 'index.html')
    
@app.route('/admin')
@requires_auth
def admin_route():    
    return send_from_directory('www', 'admin.html')    
    
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('www/js', path)
    
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('www/css', path)        

@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('www/fonts', path)
        
@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('www/images', path)    
	    
if __name__ == '__main__':
    app.run(debug=True, port=65010)    