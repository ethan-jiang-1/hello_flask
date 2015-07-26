#!flask/bin/python
from flask import Flask, url_for
from flask import Blueprint, render_template
import pdb

#pdb.set_trace() 

bp_f1 = Blueprint('bpf1', __name__, template_folder="template", url_prefix='/bpf1')
bp_f2 = Blueprint('bpf2', __name__, template_folder="template", url_prefix='/bpf2')

app = Flask(__name__)

@app.route('/')
def index():
	#pdb.set_trace()
	return "Hello, World!"



@bp_f1.route("/")
def bpf1_index():
	return "Hello, from bpf1"

app.register_blueprint(bp_f1)


@bp_f2.route("/")
def bpf2_index():
	return "hello, from bpf2"

app.register_blueprint(bp_f2)



if __name__ == '__main__':
	#pdb.set_trace()
	app.run(debug=True)