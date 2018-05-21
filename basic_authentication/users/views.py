from django.shortcuts import render, redirect
from .forms import *
from .models import *

# You can use this decorator to require users to be logged in when they go to a specific page/view method
from django.contrib.auth.decorators import login_required
# you use these functions for authentication. Make sure not to name any of your below methods after these or you will overwrite them.
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'users/index.html')

# A view used to test the built in login_required method. To use decorators, we simply write them one line above the method we want them to affect
@login_required #have to be logged in to see this page
def test_page(request):
    return render(request, 'users/test_page.html')


def register(request):
    context = {
        'user_form': UserForm(),
        'profile_form': UserProfileForm()
    }
    return render(request, 'users/register.html', context)


def create(request):
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False) # creates the user object, doesn't save yet
            # The below set_password hashes the password, as long as the 'PASSWORD_HASHERS' is set in settings.py, nothing else is necessary
            user.set_password(user.password) # hashes the password
            user.save() # saves the new hashed password

            profile = profile_form.save(commit = False)
            profile.user = user

            # request.FILES is all of the files uploaded in the request. If there is one titled 'profile_pic', it makes profile.profile_pic equal to that file
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            return redirect('users:index')
        else:
            print(user_form.errors, profile_form.errors)


    return redirect('users:register')


def login_page(request):
    return render(request, 'users/login.html')


# make sure not to name your methods after something you import, we import the 'login' function at the top
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # By using Django's built in authenticate method that we import at the top, it can take care of all of the authentication for us, we simply pass it the username and password from the form
        user = authenticate(username=username, password=password) # returns the user record if successful

        if user:
            # check if the user record is still active
            if user.is_active:
                # Once again, we use a built in method to take care of actually logging in the user, we just need to pass it the user from the authenticate method above
                login(request, user)
                return redirect('users:index')
        else:
            print('login failed')
            print("Username: {} and password {}".format(username, password))
            return redirect('users:login')


# don't name 'logout', we already imported a method called 'logout'
@login_required
def user_logout(request):
    logout(request) #automatically logs out the user
    return redirect('users:index')
