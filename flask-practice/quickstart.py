from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/login")
def login():
    return "Login Page"

# Varibale rules
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

# Unique URLs / Redirection Behavior
# If you access the URL without a trailing slash (/projects), 
# Flask redirects you to the canonical URL with the trailing slash (/projects/).
@app.route("/projects/")
def projects():
    return "The Project Page"

@app.route("/about")
def about():
    return "The About Page"