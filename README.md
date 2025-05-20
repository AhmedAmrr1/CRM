# Elite Store CRM

## Overview
Elite Store CRM is a Django-based system to manage customer data for a clothing retail store. It includes user authentication, supports multiple branches, and uses a MySQL database. The UI is responsive with Bootstrap 5.

## Features
- User registration, login, and logout
- Add, view, update, and delete customer records
- Manage branches (Smouha, Boukla, Miami)
- Responsive design using Bootstrap 5
- Client and server-side form validation
- Admin panel for managing users and records



````

## Prerequisites
- Python 3.8+
- Django 5.2
- MySQL 8.0+
- pip
- Bootstrap 5 (included via CDN)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CRM_App
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install django mysqlclient
   ```
4. Setup MySQL database:

   * Ensure MySQL is running.
   * Create database:

     ```sql
     CREATE DATABASE crm_db;
     ```
5. Configure database settings in `CRM_App/settings.py`.
6. Apply migrations:

   ```bash
   python manage.py migrate
   ```
7. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```
8. Run the development server:

   ```bash
   python manage.py runserver
   ```
9. Open [http://localhost:8000](http://localhost:8000) in your browser.

## Usage

| URL                   | Description                                |
| --------------------- | ------------------------------------------ |
| `/`                   | Login or view all customer records         |
| `/register`           | User registration form                     |
| `/logout`             | Logout user                                |
| `/record/<id>`        | View customer details                      |
| `/add_record`         | Add new customer record                    |
| `/update_record/<id>` | Update existing customer record            |
| `/delete_record/<id>` | Delete customer record (with confirmation) |
| `/admin`              | Django admin panel (superuser only)        |





