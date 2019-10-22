#!/usr/bin/env python
from flask import Flask, send_from_directory

#import other module blueprints
from Twitter import twitter
	     
app = Flask(__name__)

#register other module blueprints
app.register_blueprint(twitter)

@app.route('/')
def default_route():
    
    return send_from_directory('www', 'index.html')
    
@app.route('/admin')
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