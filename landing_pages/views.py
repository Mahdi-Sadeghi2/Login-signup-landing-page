from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth import authenticate, login

from django.contrib.auth.forms import AuthenticationForm

from .forms import UserRegisterForm


# View for the index page
def index(request):
    # Render the index.html template with a title context
    return render(request, 'index.html', {'title': 'index'})


# View for user registration
def register(request):
    if request.method == 'POST':  # Check if the request method is POST
        # Create a form instance with submitted data
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # Validate the form
            form.save()  # Save the new user to the database
            # Success message
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')  # Redirect to the login page
    else:
        form = UserRegisterForm()  # Create a blank form for GET requests
    # Render the registration template
    return render(request, 'register.html', {'form': form, 'title': 'register here'})


# View for user login
def Login(request):
    if request.method == 'POST':  # Check if the request method is POST
        username = request.POST['username']  # Get the username from the form
        password = request.POST['password']  # Get the password from the form
        user = authenticate(request, username=username,
                            password=password)  # Authenticate the user
        if user is not None:  # If authentication is successful
            login(request, user)  # Log the user in
            messages.success(request, f'Welcome {username}😉')
            return redirect('index')
        else:
            # Inform user of failed login
            messages.info(request, f'Account does not exist 🙄, please sign in')
    form = AuthenticationForm()  # Create an instance of the authentication form
    # Render the login template
    return render(request, 'login.html', {'form': form, 'title': 'log in'})
