from flask import Blueprint

main = Blueprint("main", __name__)

@main.route('/')
def Home():
    return "Hello, World!"

@main.route('/profile')
def profile():
    return "profile here"
