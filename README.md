# TrackCart

TrackCart is a web application for tracking daily expenses.

## Tech Stack

The main tech stack used in this project includes:

- Vue.js for the frontend
- Django for the backend
- Django Rest Framework for building APIs
- Bootstrap for styling
- PostgreSQL for the database

## Features
The main features for this application will be:

- Add/Remove/Update a Wallet
- Viewing Expenses Reports (Daily, Weekly, Montly, Quarterly, Annually)
- Add/Remove/Update Expenses
- Add/Remove/Update Categories
- Filter / Search for expenses based on multiple criterias, such as Wallet, Category, Location, Date, Range of Amount, etc.
- Signup / Signin using username/password and OAuth (Google, Facebook)

## Directory Structure
trackcart /
&nbsp;&nbsp;&nbsp;&nbsp;|— frontend (Vue application)
&nbsp;&nbsp;&nbsp;&nbsp;|— backend (Django application)


## Installation and Setup

1. Clone the repository:
git clone https://github.com/username/trackcart.git
2. Change into the project directory:
cd trackcart
3. Set up the backend:

- Create a virtual environment and activate it:

  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

- Install the requirements:

  ```
  cd backend
  pip install -r requirements.txt
  ```

- Migrate the database:

  ```
  python manage.py migrate
  ```

- Run the server:

  ```
  python manage.py runserver
  ```

4. Set up the frontend:

- Install the dependencies:

  ```
  cd frontend
  npm install
  ```

- Run the development server:

  ```
  npm run serve
  ```

5. Visit `http://localhost:8080` in your browser to view the application.

## License

This project is licensed under the [MIT License](LICENSE).



