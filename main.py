# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_limiter import Limiter
from flask_cors import CORS, cross_origin
from flask_limiter.util import get_remote_address



app = Flask('app')

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#really bad Data Base
db = {}

#Limit to 100 requests per second
limiter = Limiter(
		app,
		key_func=get_remote_address,
		default_limits=["100 per second"]
)

@app.route('/', methods = ['GET', 'POST']) 
@limiter.limit("100 per second")
@cross_origin()

def main():
    
	if request.method == 'POST':
		username = request.json.get('usr')
		password = request.json.get('pwd')

		if username in list(db): return 'username already exists'
		else: 
			db[username] = password


	return 'success', 200

app.run(host='0.0.0.0', port=8080)