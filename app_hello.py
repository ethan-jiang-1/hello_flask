#!flask/bin/python
from flask import Flask
import pdb

#pdb.set_trace() 

app = Flask(__name__)

@app.route('/')
def index():
	pdb.set_trace()
	return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
