import flask
from flask import request, redirect, session, flash
from authorization import (
    load_users,
    is_registered,
    register_user,
    custom_hash
)
from addBook import load_books, save_books, register_book
from contactClass import ContactHandler
from utils import flash_alerts

app = flask.Flask("library")
app.secret_key = "9z6t9V0zRJ"

def get_html(name):
    with open(name+".html","r",encoding="utf-8") as html_file:
        content = html_file.read()
    if "user" in session:
        auth_buttons = '<a href="/logout" onclick="logout()" class="nav-links log-buttons">LogOut</a>'
    else:
        auth_buttons = '<a href="/login" class="nav-links log-buttons">Login</a><a href="/register" class="nav-links log-buttons">Register</a>'
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
            <a href="/book/{book['id']}" class="details-link">View Details</a>
           
        </div>
        """
    page = page.replace("{{books}}", books_html)

    page += flash_alerts("rgb(54, 168, 54)")

    return page


@app.route("/book/<book_id>")
def book_details(book_id):
    if "user" not in session:
        flash("You need to Login First")
        return redirect("/login")
        # show login alert
    else:
        books = load_books()
        
        # Find the book using a loop
        book = None
        for b in books:
            if str(b.get("id")) == str(book_id):
                book = b
                break

        if not book:
            return "<h1>Book not found</h1>"

        content = get_html("templates/bookDetails") 
        content = content.replace("{{title}}", book.get("title", "N/A"))
        content = content.replace("{{author}}", book.get("author", "N/A"))
        content = content.replace("{{year}}", str(book.get("year", "N/A")))
        content = content.replace("{{review}}", book.get("review", "N/A"))

        # Only show description and percentage if they exist
        description_html = f"<p class='details-p'><strong>Description:</strong> {book['description']}</p>" if book.get("description") else ""
        percentage_html = f"<p class='details-p'><strong>Percentage Read:</strong> {book['percentage']}%</p>" if book.get("percentage") else ""

        owner_html = f"<p class='details-p'><strong>Added By:</strong> {book['owner_email']}</p>" if book.get("owner_email") else ""
        


        content = content.replace("{{description}}", description_html)
        content = content.replace("{{percentage}}", percentage_html)
        content = content.replace("{{owner_html}}", owner_html)

    return content



@app.route("/login",methods=['POST','GET'])
def login_page():
    login_page = get_html("templates/login")

    if request.method == "POST":
        loginEmail = request.form["loginEmail"]
        loginPassword = request.form["loginPassword"]
        hashedPassword = custom_hash(loginPassword)

        users = load_users()

        for user in users:
            if user["email"] == loginEmail and user["password"] == hashedPassword:
                session["user"] = user
                flash("Login Successful!")
                return redirect("/home")

            if not loginEmail or not loginPassword:
                errorMessage = "All fields are required!"
                return register_page.replace("<p></p>", errorMessage)
            
            elif user["email"] == loginEmail and user["password"] != hashedPassword:
                errorMessage="Incorrect Password!"
                return login_page.replace("<p></p>",errorMessage)
            
        errorMessage="Incorrect Email!"
        return login_page.replace("<p></p>",errorMessage)    
       
    login_page += flash_alerts("rgb(195, 52, 52)")
         
    return login_page


@app.route("/register",methods=['POST','GET'])
def register_page():
    register_page = get_html("templates/register")

    if request.method == 'POST':
        username = request.form['userName']
        email = request.form['email']
        password = request.form['loginPassword']

        if not username or not email or not password:
            errorMessage = "All fields are required!"
            return register_page.replace("<p></p>", errorMessage)

        if is_registered(email):
            errorMessage="Email already registered!"
            return register_page.replace("<p></p>",errorMessage)
        
        if len(password) < 6:
            errorMessage = "Password must be at least 6 characters long!"
            return register_page.replace("<p></p>", errorMessage)

        else:
            register_user(username, email, password)
            return redirect("/login")
    return register_page
    

@app.route("/addForm",methods=['GET', 'POST'])
def add_page():
    if "user" not in session:
        flash("You need to Login First")
        return redirect("/login")
    
        # show login alert
    
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        review = request.form['review']
        description = request.form['description']
        percentage = request.form['percentage']

        register_book(title, author, year,review,description,percentage)
        flash("Book Added Successfully!")
        return redirect("/home")
    
    return get_html("templates/addForm")

@app.route("/profile")
def profile_page():
    if "user" not in session:
        flash("You need to Login First")
        return redirect("/login")
    
    user_email = session["user"]["email"]
    books = load_books()

    user_books = [book for book in books if book.get("owner_email") == user_email]

    content = get_html("templates/profile")

    books_html = ""
    for book in user_books:
        description_html = f"<p><strong>Description:</strong> {book['description']}</p>" if book.get("description") else ""

        percentage_html = f"<p><strong>Percentage Read:</strong> {book['percentage']}%</p>" if book.get("percentage") else ""

        books_html += f"""
        <div class='book-card'>
            <h3>{book['title']}</h3>
            <p><strong>Author:</strong> {book['author']}</p>
            <p><strong>Year:</strong> {book['year']}</p>
            <p><strong>Review:</strong> {book['review']}</p>
            {description_html}
            {percentage_html}
            <a href="/book/{book['id']}" class="details-link">View Details</a>
            <a href="#" class="details-link edit-button"
            data-id="{book['id']}"
            data-title="{book['title']}"
            data-author="{book['author']}"
            data-year="{book['year']}"
            data-review="{book['review']}"
            data-description="{book.get('description', '')}"
            data-percentage="{book.get('percentage', '')}">Edit</a>
            <a href="#" class="details-link delete-button" data-id="{book['id']}">Delete</a>


        </div>
        """

    content = content.replace("{{user_books}}", books_html)
    content = content.replace("{{user_email}}", user_email)

    content += flash_alerts("rgb(195, 52, 52)")


    return content



@app.route("/edit_book", methods=["POST"])
def edit_book():
    books = load_books()
    book_id = request.form["id"]

    for book in books:
        if str(book["id"]) == book_id:
            book["title"] = request.form["title"]
            book["author"] = request.form["author"]
            book["year"] = request.form["year"]
            book["review"] = request.form["review"]
            book["description"] = request.form["description"]
            book["percentage"] = request.form["percentage"]
            break

    save_books(books)

    return redirect("/profile")


@app.route("/delete_book/<book_id>", methods=["POST"])
def delete_book(book_id):

    books = load_books()
    updated_books = [book for book in books if str(book.get("id")) != str(book_id)]

    save_books(updated_books)
    flash("Book Deleted Successfully!")

    return redirect("/profile")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    contact_handler = ContactHandler()

    if request.method == "POST":
        name = request.form.get("name")
        mobile = request.form.get("mobile")
        feedback = request.form.get("feedback")

        contact_handler.set_data(name, mobile, feedback)
        contact_handler.save_to_file()

        flash("Thank you for your feedback :)")
        return redirect("/home")

    return get_html("templates/contactUs")

@app.route("/logout")
def logout():
    session.clear()
    return get_html("templates/login")

@app.errorhandler(404)
def page_not_found(e):
    return get_html("templates/error"), 404

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return response