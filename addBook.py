from flask import session
import json


books_file = "data/books.json"

# reads data from the JSON file and converts it into a Python object 
def load_books():
    with open(books_file,"r") as file:
        return json.load(file)

# writes a Python object into a file in JSON format.
def  save_books(books):
    with open(books_file,"w") as file:
        return json.dump(books,file,indent=2)

def register_book(title, author, year, review, description, percentage):
    books = load_books()

    max_id = max([book['id'] for book in books], default=0)

    new_book = {
        "id": max_id + 1,
        "title": title,
        "author": author,
        "year": year,
        "review": review,
        "description": description,
        "percentage": percentage,
        "owner_email": session["user"]["email"]
    }
    books.append(new_book)
    save_books(books)
