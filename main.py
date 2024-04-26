from flask import  Blueprint, render_template

main = Blueprint("main", __name__)

@main.route('/')
def Home():
    return "Hello, World!"

@main.route('/profile')
def profile():
    return "profile here"