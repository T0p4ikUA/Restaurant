"# Restaurant" 
'Bezdohannyyi' is a comprehensive Django-based restaurant management system designed to streamline internal operations, staff coordination, and customer order processing.

Technologies:
-  Python 3.x
-  Django
-  Bootstrap 5
-  SQLite
-  JavaScript (for dynamic frontend UI updates)
Features:
-  sPosition & Employee Management: Organize restaurant staff roles and monitor employee accounts.
-  Dish Catalog: Manage the menu items, prices, descriptions, and filtering options. 
-  Order Processing: Create and track orders with a dynamic JavaScript-based real-time price calculation using CheckboxSelectMultiple fields.
-  Admin & Authentication: Secure system access protected by authentication and CSRF validation.
Installation & Setup:
-  Clone the repository and navigate to the project folder.
-  Create and activate your virtual environment:

- python -m venv venv
- source venv/bin/activate  # On Windows use: venv\Scripts\activate
- Install the dependencies:

pip install -r requirements.txt
Run database migrations:

python manage.py migrate
Create an administrator account (enter your desired username and password when prompted):

python manage.py createsuperuser
Start the local development server:

python manage.py runserver
Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser, log in with your superuser credentials, and access the application.