import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'hello_flask.db'
USERNAME = 'admin'
PASSWORD = 'admin'
CSRF_ENABLED = True
SECRET_KEY = 'my-secret-key-here'

DATABASE_PATH = os.path.jon(basedir,DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH