🌐 FLASK WEB APP

A Simple, Clean, and Professional Web Application Built Using Flask

📌 Overview

This project is a Flask-based web application that demonstrates core web development concepts such as routing, templates, authentication, and modular application structure.
It is designed to be easy to understand, cleanly structured, and beginner-friendly, yet written professionally to showcase my backend and full-stack development skills.

The goal of this project is to show:

My ability to build a complete Flask application

How I structure production-quality code

How I work with templates, static files, and routes

How I write clean, readable, and extendable code

✨ Key Features

User Login System

Simple authentication flow (login page, user verification)

Flask Routing Architecture

Organized route handling using views.py and auth.py

Templating with Jinja2

Reusable templates using base.html

Static File Management

Properly organized CSS files under /static

Clean Project Structure

Easy-to-understand folder layout suitable for beginners and recruiters

Extendable Design

New routes, pages, and modules can be added easily

🏗️ Project Structure
project/
│
├── main.py                 # Application entry point
│
├── website/                # Main Flask package
│   ├── __init__.py         # App factory and setup
│   ├── views.py            # Routes for normal website pages
│   ├── auth.py             # Routes for authentication pages
│   ├── models.py           # Database models (if added)
│   │
│   ├── templates/          # HTML templates
│   │   ├── base.html       # Main layout file
│   │   ├── home.html       # Home page
│   │   └── login.html      # Login page 
│   │
│   └── static/             # Static assets
│       └── style.css       # Project stylesheet
│
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation


This structure is simple, clean, and follows Flask best practices.

🛠️ Tech Stack

Backend: Python, Flask
Frontend: HTML, CSS (Jinja2 templating)
Database: SQLite (or can be extended easily)
Environment: Virtual Environment (venv)

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/Arunrdy/FLASK_WEB_APP.git
cd FLASK_WEB_APP

2️⃣ Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python main.py


Your app will run on:
👉 http://127.0.0.1:5000/

📄 How It Works (Simple Explanation)

When the app starts, main.py loads the Flask application from website/__init__.py

views.py handles all normal pages (like home page)

auth.py manages login logic and authentication routes

templates/ contains clean, reusable HTML pages

base.html acts as the main layout (header, body, footer)

style.css adds styles to the UI

This structure makes the project:
✔ Easy to understand
✔ Easy to extend
✔ Easy for recruiters to quickly evaluate

📘 Learning Purpose

This project is perfect for learning:

How Flask handles routing

How to use Jinja2 templates

How to structure real-world Flask applications

How backend and frontend connect in a web app

How authentication works at a basic level

🧩 Future Improvements

These are planned (or possible) future upgrades:

Add registration page

Add database models for users

Add dashboard pages

Add password hashing and secure login

Add more HTML pages (About, Profile, Contact, etc.)

Add API endpoints with Flask REST

Add form validation

Deploy the app to Render / Railway / AWS / Heroku

🤝 Contributing

Pull requests and improvements are welcome.
If you want to improve UI, add pages, or extend backend logic, feel free to contribute.

📬 Contact

Author: Arun Reddy
GitHub: https://github.com/Arunrdy

If you want to discuss improvements or ask questions, feel free to contact me.

⭐ Final Note

This project focuses on:

Clean code

Professional structure

Simple user experience

Easy learning path

Recruiter-friendly design

Thank you for checking out this project!
