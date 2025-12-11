# Task Manager App

🌐 Live Demo

🔗 https://demo-task-dashboard.onrender.com/

🗂 GitHub:

A simple Task Management Web Application built as part of a Full-Stack Developer assignment for Social Booster Media.

This project demonstrates CRUD APIs, API integration, data visualization, and deployment.

1. CRUD Operations (REST API)

Implemented using Django REST Framework:

Method	Endpoint	Description
GET	/api/tasks/	List all tasks
POST	/api/tasks/	Create a task
GET	/api/tasks/<id>/	Get task
PATCH	/api/tasks/<id>/	Update task partial
DELETE	/api/tasks/<id>/	Delete task partial

2. External API Integration

Fetching user data from JSONPlaceholder:

GET /api/user/
This displays a demo user on the dashboard.

3. Data Visualization

Using Chart.js to display:

Completed tasks count

Pending tasks count

4. Frontend Dashboard (HTML + JS)

The UI includes:

Add task

Complete task

Delete task

View user info

Live chart updates

5. Tech Stack

Backend: Django, Django REST Framework

Database: PostgreSQL

Frontend: HTML, CSS, JS

Charts: Chart.js

Hosting: Render.com

6. How to run locally 

1. Clone the repository
git clone <your-repo-link>
cd project

2. Install requirements
pip install -r requirements.txt

3. Apply migrations
python manage.py migrate

4. Run server
python manage.py runserver

7. API Examples

Create Task
POST /api/tasks/
{
  "title": "Interview",
  "description": "Complete Django assignment",
  "completed": false
}

Update Task
PATCH /api/tasks/3/
{
  "completed": true
}

8.Dashboard Features

Task list divided into:
✔ Pending Tasks
✔ Completed Tasks

Buttons:

Add Task

Complete Task

Delete Task

Chart showing task status visually

User API fetched and displayed