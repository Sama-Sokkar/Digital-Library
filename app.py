import flask

app = flask.Flask("library")

def get_html(name):
    html_file = open(name + ".html")
    content = html_file.read()
    html_file.close()
    return content

@app.route("/")
def index_page():
    return get_html("templates/index")

@app.route("/login")
def login_page():
    return get_html("templates/login")

@app.route("/register")
def register_page():
    return get_html("templates/register")

@app.route("/addForm")
def add_page():
    return get_html("templates/addForm")