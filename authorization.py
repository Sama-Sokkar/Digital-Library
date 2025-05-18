import string
import json

users_file = "data/users.json"

# reads data from the JSON file and converts it into a Python object 
def load_users():
    with open(users_file,"r") as file:
        return json.load(file)

# writes a Python object into a file in JSON format.
def  save_users(users):
    with open(users_file,"w") as file:
        return json.dump(users,file,indent=2)

# return true if the user already registered with the same email
def is_registered(email):
    users = load_users()
    return any(user["email"] == email for user in users)

# hash the password
def custom_hash(password):
    chars = string.ascii_letters + string.digits + "!@#$"
    hashed = ""

    for i, char in enumerate(password):
        # get ASCII value
        val = ord(char) + i

        hashed_char = chars[val % len(chars)]
        hashed += hashed_char

    return hashed

# register the user
def register_user(username, email, password):
    users = load_users()
    hashed_password = custom_hash(password)
    users.append({"username": username, "email": email, "password": hashed_password})
    save_users(users)
