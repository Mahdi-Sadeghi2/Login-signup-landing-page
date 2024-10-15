README.md

# Django User Authentication

This Django application provides user registration and login functionalities. Users can create an account and log in to access the main index page.

## Features

- User registration with form validation
- User login with authentication
- Success and error messages for user feedback

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the project directory:**
   ```bash
   cd <project-directory>
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

### User Registration

- Navigate to the registration page.
- Fill out the registration form with your details.
- Upon successful registration, you will receive a confirmation message and be redirected to the login page.

### User Login

- Navigate to the login page.
- Enter your username and password.
- If the credentials are correct, you will be logged in and redirected to the index page.

## Templates

- `index.html`: The main landing page after login.
- `register.html`: The registration form template.
- `login.html`: The login form template.

## Contributing

Feel free to submit issues or pull requests if you want to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




