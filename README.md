# Report Project

**Report Project** is a web application based on the MTV (Model-Template-View) architecture, built with Django. The application allows for the entry of incoming invoices and provides reports on total costs by cost centers.

## Contents

- [Starting the Server](#starting-the-server)
- [Application Structure](#application-structure)
- [Features](#features)
- [Technologies](#technologies)

---

## Starting the Server

To run the project locally, follow these steps:

1. **Clone the repository**:

    If you are downloading the project from GitHub, clone the repository using `git clone`:

    ```bash
    git clone https://github.com/anasicic/report_project.git
    ```

2. **Navigate to the project directory**:

    After cloning the project, navigate to the project directory:

    ```bash
    cd report_project
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create migration files for the database**:

    ```bash
    python manage.py makemigrations
    ```

5. **Apply migrations to update the database**:

    ```bash
    python manage.py migrate
    ```

6. **Start the development server**:

    ```bash
    python manage.py runserver
    ```

7. **Open your browser and go to**:

    ```url
    http://127.0.0.1:8000/
    ```

---

## Application Structure

The application consists of two apps: `invoice` and `users`. Both apps inherit from `base.html`, which defines the overall layout for all pages.

- **Database**: The application uses SQLite for data storage.
- **Frontend**: The frontend is created with HTML, CSS, and Bootstrap.

### Invoice App

- Contains four models:
  - `TypeOfCost`
  - `CostCenter`
  - `Supplier`
  - `Invoice`

- The `Invoice` model serves as an intermediary table connecting the other models, including a link to the user (User).

---

## Features

### 1. User Login

- On application launch, users are presented with a login interface.
- Unregistered users can register via the form on the "Register" link.
- **Functionality**: User authentication (login, registration, logout).

### 2. Administrative Privileges

- Administrators can access the interface to add/remove users, suppliers, cost types, and cost centers.
- **Functionality**: Administrative functions (adding and removing users, generating reports).

### 3. Display of Incoming Invoices

- Displays the invoice number, date, supplier, and net amount.
- Administrators additionally see the user who entered the invoice.

### 4. Invoice Update and Deletion

- After updating or deleting an invoice, the user receives a confirmation message and is redirected to the homepage.

### 5. Adding a New Invoice

- Users can enter new invoices via the form on the homepage.

### 6. User Profile

- Users can update their information through the "Profile" page.

### 7. Logout

- Users can log out by clicking "Logout".

---

## Technologies

- **Django** - Web framework for the backend
- **SQLite** - Database
- **HTML, CSS, Bootstrap** - Frontend technologies for the interface
