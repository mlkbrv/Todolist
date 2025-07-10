# Django Todo List

This project is a simple Todo List web application built with Django. It allows each user to manage their own tasks, mark them as urgent or normal, edit, complete, and delete them. Completed tasks are displayed in a separate section or tab.

## Features
- User-specific task lists
- Mark tasks as normal (default) or urgent (highlighted in red)
- Edit, complete, or delete tasks
- Completed tasks are shown in a separate section/tab
- Responsive and clean interface (Bootstrap recommended)

## Project Structure
- `manage.py` — Django project management script
- `Todolist/` — Django project settings and configuration
- `main/` — (expected) Django app for task management (create this if not present)
- `templates/` — HTML templates for rendering pages
- `static/` — Static files (CSS, images, etc.)

## How to Run
1. Install dependencies:
   ```bash
   pip install django
   ```
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Start the development server:
   ```bash
   python manage.py runserver
   ```
4. Open your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Frontend
- The user interface is rendered using Django templates (HTML) and styled with [Bootstrap 5](https://getbootstrap.com/).
- You can use Bootstrap Icons for better UX.
- All logic is handled server-side; no JavaScript is required for basic functionality.

## License
MIT (or specify your own) 