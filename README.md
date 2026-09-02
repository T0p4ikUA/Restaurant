# Restaurant

**Bezdohannyyi** is a comprehensive Django-based restaurant management system designed to streamline internal operations, staff coordination, and customer order processing.

## Technologies

* **Python 3.x**
* **Django**
* **Bootstrap 5**
* **SQLite**
* **JavaScript** — for dynamic frontend UI updates

## Features

* **Position & Employee Management**
  Organize restaurant staff roles and manage employee accounts.

* **Dish Catalog**
  Manage menu items, prices, descriptions, and filtering options.

* **Order Processing**
  Create and track orders with dynamic JavaScript-based real-time price calculation using `CheckboxSelectMultiple` fields.

* **Admin & Authentication**
  Secure system access protected by authentication and CSRF validation.

## Installation & Setup

### 1. Clone the Repository

Clone the repository and navigate to the project folder:

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create and Activate a Virtual Environment

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

Run the database migrations:

```bash
python manage.py migrate
```

### 5. Create a Superuser

Create an administrator account:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter your desired username, email, and password.

### 6. Start the Development Server

Run the Django development server:

```bash
python manage.py runserver
```

### 7. Open the Application

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

Log in using your superuser credentials to access the application.

## Project Structure

A typical project structure may look like this:

```text
Restaurant/
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── app/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
└── project/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

## Authentication

The application uses Django's built-in authentication system to protect access to the restaurant management functionality.

CSRF protection is enabled for forms and requests to improve application security.

## Database

The project uses **SQLite** as its default database.

Database migrations can be applied with:

```bash
python manage.py migrate
```

## Development

To run the project locally:

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

## License

This project is intended for educational and development purposes.
