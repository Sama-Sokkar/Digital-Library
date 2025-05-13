import flask
from flask import request,redirect,session
from authorization import load_users, save_users, is_registered, register_user
from addBook import register_book,load_books


app = flask.Flask("library")
app.secret_key = "9z6t9V0zRJ"

def get_html(name):
    with open(name+".html","r") as html_file:
        content = html_file.read()
    if "user" in session:
        auth_buttons = '<a href="/logout" onclick="logout()" class="navLinks">LogOut</a>'
    else:
        auth_buttons = '<a href="/login" class="navLinks">Login</a><a href="/register" class="navLinks">Register</a>'
    return content.replace("{{auth_buttons}}", auth_buttons)

@app.route("/") 
def index_page():
    return get_html("templates/index")


@app.route("/home", methods=['GET'])
def home_page():
    page = get_html("templates/home")

    # Inject username into localStorage
    if "user" in session:
        username = session["user"]["username"]
        page += f"""
        <script>
          localStorage.setItem("name", "{username}");
        </script>
        """

    # load books from json file
    books = load_books()
    books_html = ""
    for book in books:
        books_html += f"""
        <div class="book-card">
            <h3>{book['title']}</h3>
            <p><strong>Author:</strong> {book['author']}</p>
            <p><strong>Year:</strong> {book['year']}</p>
            <p><strong>Review:</strong> {book['review']}</p>
            <hr>
        </div>
        """
            #  <a href="/book/{book['id']}" class="details-button">View Details</a>

    # Replace placeholder in HTML file (e.g. {{books}})
    page = page.replace("{{books}}", books_html)

    # Inject alert if there's a success message in query params
    success_msg = request.args.get("success")
    if success_msg:
        page += f"""
        <script>
          document.addEventListener("DOMContentLoaded", function() {{
              showAlert("{success_msg}");
          }});
        </script>
        """

    return page



# @app.route("/book/<int:book_id>")
# def book_details(book_id):
#     books = load_books()
#     selected_book = next((book for book in books if book["id"] == book_id), None)

#     # if not selected_book:
#     #     return abort(404)

#     page = get_html("templates/bookDetails")

#     # Fill in the book details into the HTML
#     for key, value in selected_book.items():
#         page = page.replace(f"{{{{{key}}}}}", str(value))

#     return page


@app.route("/login",methods=['POST','GET'])
def login_page():
    login_page = get_html("templates/login")

    if request.method == "POST":
        loginEmail = request.form["loginEmail"]
        loginPassword = request.form["loginPassword"]

        users = load_users()

        for user in users:
            if user["email"] == loginEmail and user["password"] == loginPassword:
                session["user"] = user
                return redirect("/home?success=Login+Successful!")

            
            elif user["email"] == loginEmail and user["password"] != loginPassword:
                errorMessage="Incorrect Password!"
                return login_page.replace("<p></p>",errorMessage)
            
        errorMessage="Incorrect Email!"
        return login_page.replace("<p></p>",errorMessage)            
    return login_page


@app.route("/register",methods=['POST','GET'])
def register_page():
    register_page = get_html("templates/register")

    if request.method == 'POST':
        username = request.form['userName']
        email = request.form['email']
        password = request.form['password']

        if is_registered(email):
            errorMessage="Email already registered!"
            return register_page.replace("<p></p>",errorMessage)
        else:
            register_user(username, email, password)
            return redirect("/login")
    return register_page
    

@app.route("/addForm",methods=['GET', 'POST'])
def add_page():
    if "user" not in session:
        return redirect("/login")
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        review = request.form['review']
        description = request.form['description']
        percentage = request.form['percentage']

        register_book(title, author, year,review,description,percentage)
        return redirect("/home?success=Book+Added+Successfully!")
    
    return get_html("templates/addForm")

@app.route("/logout")
def logout():
    session.pop("user",None)
    return get_html("templates/login")