# Django Contacts App

This is a simple Django contacts app that allows you to manage a list of contacts. Follow the instructions below to set up and run the application.

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.12
- Django version 4

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kodala02/lab4.git
   cd django-contacts-app
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin):**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account.

   The following credentials are already being used by the datababse cloned with the project:

   - Username: kodala
   - Password: kodala

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at http://localhost:8000/.

8. **Access the admin interface:**

   Visit http://localhost:8000/admin/ and log in with the superuser credentials created in step 6.

## Usage

- **Home Page:** http://localhost:8000/
- **Contacts:** http://localhost:8000/contacts/
- **Help:** http://localhost:8000/help/

Explore the pages and manage your contacts through the provided interface.

```

```
