from flask import Blueprint, render_template

auth = Blueprint("auth", "__name__")

@auth.route("/signup")
def signup():
    return "This page is for sign up"

@auth.route("/login")
def login():
    return "this page is for login"

@auth.route("/logout")
def logout():
    return "this page is for logout"