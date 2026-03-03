# 🚀 Flask Notes Web Application

A full-stack web application built using **Flask**,**Python**,**MySQL**, and **SQLAlchemy** that allows users to securely register, log in, and manage personal notes with persistent storage.

---

## 🌐 Live Application

🔗 **Live Demo:**  
👉 https://flask-web-app-kzaa.onrender.com


---

## 📂 GitHub Repository

🔗 https://github.com/Arunrdy/FLASK_WEB_APP

---

## 📌 Project Overview

This project is a secure Notes Management System where:

- Users can create an account
- Log in using encrypted (hashed) passwords
- Add personal notes
- Delete notes
- Store data permanently in a MySQL database

The application demonstrates backend development, authentication handling, ORM usage, and real database integration.

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Flask-Login**
- **Flask-SQLAlchemy**
- **PyMySQL**
- **MySQL**
- **HTML & CSS**
- **Render (Deployment)**

---

## 🧠 System Architecture

User → Flask → Flask-SQLAlchemy → SQLAlchemy ORM → PyMySQL → MySQL Database

- Flask handles routing and form submissions
- SQLAlchemy converts Python objects into SQL queries
- PyMySQL acts as the database driver
- MySQL stores the data permanently

---

## 🔐 Core Features

✅ User Registration  
✅ Secure Password Hashing  
✅ Login Authentication  
✅ Add Notes  
✅ Delete Notes  
✅ MySQL Persistent Storage  
✅ Organized MVC Structure  

---

## 🗂️ Project Structure

```
FLASK_WEB_APP/
│
├── main.py
├── requirements.txt
├── README.md
│
└── Website/
    ├── __init__.py
    ├── models.py
    ├── views.py
    ├── auth.py
    ├── templates/
    │   ├── base.html
    │   ├── home.html
    │   ├── login.html
    │   └── sign_up.html
    └── static/
        └── index.js
```

---

## ⚙️ Database Configuration

The application connects to MySQL using:

```
mysql+pymysql://username:password@localhost/flask_notes_app
```

### Database Tables

**Users Table**
- id
- email
- password (hashed)
- first_name

**Notes Table**
- id
- content
- user_id (Foreign Key → users.id)

---

## 🚀 Deployment

This project is deployed using **Render** and configured with:

- `gunicorn` as the production server
- `requirements.txt` for dependency management

---

## 📈 Future Enhancements

- Password reset functionality
- Email verification
- User profile settings
- Pagination for notes
- REST API support
- Docker containerization

---

## 👨‍💻 Author

**Arun**

---

⭐ If you found this project helpful, feel free to star the repository!
