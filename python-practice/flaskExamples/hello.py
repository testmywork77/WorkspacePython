from flask import Flask
from markupsafe import escape

"""
    To run flask app:
        set FLASK_APP=hello.py
        (env) C:\WorkspacePython\python-pocs\flaskapi>python -m flask run
            * Serving Flask app "hello.py"
            * Environment: production
            WARNING: This is a development server. Do not use it in a production deployment.
            Use a production WSGI server instead.
            * Debug mode: off
            * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

    set FLASK_ENV=development
    This does the following things:
        1. it activates the debugger
        2. it activates the automatic reloader
        3. it enables the debug mode on the Flask application.
"""

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
