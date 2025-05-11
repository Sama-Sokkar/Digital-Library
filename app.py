import flask
from flask import request,redirect
from authorization import load_users, save_users, is_registered, register_user


app = flask.Flask("library")

def get_html(name):
    with open(name+".html","r") as html_file:
        return html_file.read()

@app.route("/")
def index_page():
    return get_html("templates/index")

@app.route("/home",methods=['GET'])
def home_page():
    return get_html("templates/home")

@app.route("/login")
def login_page():
    return get_html("templates/login")

@app.route("/register",methods=['POST','GET'])
def register_page():
    register_page = get_html("templates/register")

    if request.method == 'POST':
        username = request.form['userName']
        email = request.form['email']
        password = request.form['password']

        if is_registered(email):
            errorMessage="<p>Email already registered!<p/>"
            return register_page.replace("<p></p>",errorMessage)
        else:
            register_user(username, email, password)
            return redirect("/home")
    return get_html("templates/register")
    

@app.route("/addForm")
def add_page():
    return get_html("templates/addForm")