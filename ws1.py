#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
	"""List all tasks."""
	return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
	"""List specific task."""
	task = filter(lambda t: t['id'] == task_id, tasks)
	if len(task) == 0:
		abort(404)
	return jsonify({'task': task[0]})


@app.route('/todo/api/v1.0/help', methods=['GET'])
def help():
	"""Print available functions."""
	func_list = {}
	for rule in app.url_map.iter_rules():
		if rule.endpoint != 'static' : 
			func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
	return jsonify(func_list)

@app.errorhandler(404)
def not_find(error):
	return make_response(jsonify({'error': 'Not found'}),404)

if __name__ == '__main__':
    app.run(debug=True)