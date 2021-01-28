# CRUD
A simple Web application which keeps track of Users different account. Using HTML5 and bootstrap coupled with Django framework to architect a fast, secure and responsive website.

## Features
- Built multiple security measures for attacks like csrf, xss etc along with an authentication and validation system for user input data.
- Two seperate sides
  - client facing side
  - admin facing side
-  Persistence achieved through an SQLite database
- Input validation is done using builtin django method

### Requirements
- Django==3.1.3
- django-crispy-forms==1.10.0

### How to run **CRUD** on Local Machine
- Make sure to remove  these lines 'from decouple import config' and 'import os' from settings.py
- Drop a mail on kumarnauj1303@gmail.com for the SECRET_KEY.
- After getting SECRET_KEY replace it with the current SECRET_KEY in settings.py
