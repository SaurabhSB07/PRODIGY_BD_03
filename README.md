# PRODIGY_BD_03 – JWT Authentication with Django REST Framework

## 📌 Task Description
This project is Task 3 of the Prodigy InfoTech Backend Development Internship (Track: BD).  
It implements **authentication and authorization** using **JSON Web Tokens (JWT)** with Django REST Framework.

The project includes:
- User registration
- User login
- JWT token generation on successful login
- Protected API routes
- Role-based access control (admin, user, owner)

---

## 🛠️ Tech Stack
- Python
- Django
- Django REST Framework
- SimpleJWT (JWT Authentication)
- SQLite (default database)

---

## ✨ Features
- **User Registration** API (`/api/register/`)
- **User Login** API (`/api/login/`) with JWT token
- **Protected Routes** using JWT authentication (`/api/profile/`)
- **Role-Based Access Control** (admin, user, owner) (`/api/admin-only/`)
- **Secure Password Hashing** (Django handles it automatically)

---

## 🔑 API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| POST   | `/api/register/`  | Register a new user |
| POST   | `/api/login/`     | Login and receive JWT token |
| GET    | `/api/profile/`   | View your profile (authenticated users only) |
| GET    | `/api/admin-only/` | Admin-only access |

---

## ▶️ How to Run

#1. Clone the repository:
git clone https://github.com/SaurabhSB)&/PRODIGY_BD_03.git

#2.Activate virtual environment:
cd PRODIGY_BD_03
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac

#3.Install requirements:
pip install -r requirements.txt

#4.Run migrations:
python manage.py makemigrations
python manage.py migrate

#5.Start the server
python manage.py runserver

#6.Access the APIs at:
http://127.0.0.1:8000/api/

🔒 Authentication

Use the JWT token from login in headers for protected endpoints:
Authorization: Bearer <your_token>

📚 Internship Info

Internship: Prodigy InfoTech

Track: Backend Development (BD)

Task: 3 – JWT Authentication & Authorization
