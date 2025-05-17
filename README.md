# MY FINAL PROJECT (Digital-Library)

The Digital Library is a web app for organizing and tracking digital books with secure user authentication. Users can add content and monitor their reading progress.

- What does it do?  
   It allows users to register, log in, and manage a personal digital library by adding, editing, and deleting books.
- What is the "new feature" which you have implemented that
  we haven't seen before?  
   The user profile displays only the books added by the logged-in user, unlike the home page which shows all books.
  It also allows the user to edit or delete their books directly from the profile.

## Prerequisites

Did you add any additional modules that someone needs to
install (for instance anything in Python that you `pip 
install-ed`)?  
pip install flask

## Project Checklist

- [✅] It is available on GitHub.

- [✅] It uses the Flask web framework.

- [✅] It uses at least one module from the Python Standard
  Library other than the random module.
  Please provide the name of the module you are using in your
  app.

  - Modules name:
    flask
    flask.request
    flask.redirect
    flask.session
    json

- [✅] It contains at least one class written by you that has
  both properties and methods. It uses `__init__()` to let the
  class initialize the object's attributes (note that  
  `__init__()` doesn't count as a method). This includes
  instantiating the class and using the methods in your app.

  Please provide below the file name and the line number(s) of
  at least one example of a class definition in your code as
  well as the names of two properties and two methods.

  - File name for the class definition: contactClass.py
  - Line number(s) for the class definition: from line number 1 till line number 17
  - Name of two properties: name and mobile
  - Name of two methods: set_data() and save_to_file()
  - File name and line numbers where the methods are used: app.py line number 259 and 260

- [✅] It makes use of JavaScript in the front end and uses the
  localStorage of the web browser.

- [✅] It uses modern JavaScript (for example, let and const
  rather than var).

- [✅] It makes use of the reading and writing to the same file
  feature.

- [✅] It contains conditional statements. Please provide below
  the file name and the line number(s) of at least
  one example of a conditional statement in your code.

  - File name: app.py
  - Line number(s): from line 92 to line 95

- [✅] It contains loops. Please provide below the file name
  and the line number(s) of at least
  one example of a loop in your code.

  - File name: app.py
  - Line number(s): from line 40 to line 50

- [✅] It lets the user enter a value in a text box at some
  point.
  This value is received and processed by your back end
  Python code.

- [✅] It doesn't generate any error message even if the user
  enters a wrong input.

- [✅] It is styled using your own CSS.

- [] The code follows the code and style conventions as
  introduced in the course, is fully documented using comments
  and doesn't contain unused or experimental code.  
   In particular, the code should not use `print()` or
  `console.log()` for any information the app user should see.
  Instead, all user feedback needs to be visible in the
  browser.

- [✅] All exercises have been completed as per the
  requirements and pushed to the respective GitHub repository.
