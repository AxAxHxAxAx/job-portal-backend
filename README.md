Job Portal Backend API

A backend Job Portal application built using FastAPI and PostgreSQL that supports authentication, role-based access control, job posting, applications, saved jobs, filtering, and pagination.

🚀 Features

🔐 Authentication & Authorization
User Registration & Login
JWT-based Authentication
Role-based Authorization
Protected Routes

👨‍💼 Recruiter Features
Create Job Posts
Update Own Jobs
Delete Own Jobs
View Applications on Posted Jobs

👨‍💻 User Features
View Available Jobs
Apply to Jobs
Save/Bookmark Jobs
View Saved Jobs
Prevent Duplicate Applications & Saves

🔎 Job Search Features
Filter jobs by:
Company
Location
Title

🗄️ Database Features
Relational Database Design
Foreign Key Relationships
SQLAlchemy ORM
JOIN Queries

🛠️ Tech Stack
Python
FastAPI
PostgreSQL
SQLAlchemy
JWT Authentication
Pydantic
Uvicorn

📂 Project Structure
job_portal/
│
├── app/
│   ├── auth/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── database.py
│
├── requirements.txt
├── .env
├── main.py

⚙️ Installation & Setup

1️⃣ Clone Repository
git clone <your-repo-url>
cd job-portal-fastapi

2️⃣ Create Virtual Environment
python -m venv venv

Activate virtual environment:

Windows
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure Environment Variables

Create .env file:

DATABASE_URL=postgresql://postgres:yourpassword@localhost/jobportal
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

5️⃣ Run Server
uvicorn main:app --reload

Server runs at:

http://127.0.0.1:8000

Swagger Docs:

http://127.0.0.1:8000/docs

📌 Main API Endpoints
Authentication
POST /register
POST /login

Jobs
GET /jobs
POST /jobs
PUT /jobs/{job_id}
DELETE /jobs/{job_id}

Applications
POST /apply/{job_id}
GET /job_applications

Saved Jobs
POST /save_jobs/{job_id}
GET /saved_jobs

🔥 Concepts Learned
REST API Development
JWT Authentication
Role-Based Access Control
SQLAlchemy ORM
Database Relationships
Query Filtering
Pagination
JOIN Queries
Error Handling
Environment Variables
Git & GitHub

👨‍💻 Author

Akash Rawat
