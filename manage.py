# manage.py

from flask.ext.script import Manager
from flask import url_for
from app_blueprint import app
from managers.list_routes import x_list_routes_ex

manager = Manager(app)

@manager.command
def hello():
    print "hello"


@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print line	

@manager.command
def list_routes_ex():
    x_list_routes_ex(app) 


if __name__ == "__main__":
    manager.run()