# Django Blog Application

## Setup

1. Clone the repository:
   ```bash
   git clone <https://github.com/munishmangla98/django-ass.git>

python -m venv myvenv
myvenv\Scripts\activate
python manage.py migrate
python manage.py runserver


APIs to test in Postman
Signup = http://127.0.0.1:8000/api/signup/
dome credentials = {
  "username": "Django",
  "password": "123"
}
Login = http://127.0.0.1:8000/api/token/
dome credentials = {
  "username": "Django",
  "password": "123"
}
For CRUD
Add Blog = "POST"  http://127.0.0.1:8000/api/posts/
Retrive_all blog = "GET" http://127.0.0.1:8000/api/posts/
Retrive bt Id = "GET"  http://127.0.0.1:8000/api/posts/{blog_Id}
Update bolg = "PUT"   http://127.0.0.1:8000/api/posts/{blog_Id}/
Delete blog = "DELETE"  http://127.0.0.1:8000/api/posts/{blog_Id}/

For Adding Comments
Add comments = "POST" http://127.0.0.1:8000/api/posts/{blog_Id}/comments/

