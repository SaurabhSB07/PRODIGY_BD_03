# PRODIGY_BD_03 – JWT Authentication (Task 3) & Redis Caching (Task 4) 
*(Django REST Framework)*

---

## 📌 Project Overview

This repository contains **Task 3 and Task 4** of the **Prodigy InfoTech Backend Development Internship (Track: BD)**.

The project demonstrates:
- Secure authentication & authorization using **JWT**
- **Role-based access control**
- **Performance optimization using Redis caching**

---

## 🧩 Tasks Implemented

### 🔐 Task 3 – JWT Authentication & Authorization
- User registration
- User login using JWT
- Protected API endpoints
- Role-based access control (Admin, User, Owner)

### ⚡ Task 4 – Caching with Redis
- Redis integration with Django
- Caching frequently accessed endpoints (users list)
- Cache expiration (TTL)
- Cache invalidation on update/delete
- Improved API performance

---

## 🛠️ Tech Stack
- Python  
- Django  
- Django REST Framework  
- SimpleJWT (JWT Authentication)  
- Redis  
- django-redis  
- SQLite (default database)

---

## ✨ Features

### 🔒 Authentication & Authorization
- User Registration → `/api/register/`
- User Login (JWT) → `/api/login/`
- Protected Profile API → `/api/profile/`
- Admin-only API → `/api/admin-only/`
- Role-based access control using custom permissions

### ⚡ Redis Caching
- Cached users list endpoint
- Faster responses for repeated requests
- Cache expiration to ensure fresh data
- Automatic cache invalidation on data changes

---

## 🔑 API Endpoints

| Method | Endpoint | Description |
|------|--------|-------------|
| POST | `/api/register/` | Register a new user |
| POST | `/api/login/` | Login & receive JWT token |
| GET | `/api/profile/` | View user profile (JWT required) |
| GET | `/api/admin-only/` | Admin-only access |
| GET | `/api/users/` | Fetch all users (Redis cached) |

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/SaurabhSB07/PRODIGY_BD_03.git


## ▶️ How to Run

#1. Clone the repository:
git clone https://github.com/SaurabhSB)&/PRODIGY_BD_03.git

#2.Activate virtual environment:
cd PRODIGY_BD_03
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac

#3.Install requirements:
pip install -r requirements.txt

#4.Run Redis Server
Make sure Redis is running: redis-server

#5.Run migrations:
python manage.py makemigrations
python manage.py migrate

#6.Start the server
python manage.py runserver

#7.Access the APIs at:
http://127.0.0.1:8000/api/

🔒 Authentication

Use the JWT token from login in headers for protected endpoints:
Authorization: Bearer <your_token>

🚀 Performance Improvement (Task 4)

First request fetches data from database

Subsequent requests are served from Redis cache

Reduced database queries

Faster API response times

📚 Internship Information

Internship: Prodigy InfoTech

Track: Backend Development (BD)

Tasks Completed:

Task 3 – JWT Authentication & Authorization

Task 4 – Redis Caching for API Optimization
