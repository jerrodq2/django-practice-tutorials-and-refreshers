from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def register(request):
    if 'register' not in request.session:
        request.session['registered'] = False
    context = {
        'user_form': UserForm(),
        'profile_form': UserProfileForm()
    }
    return render(request, 'users/register.html', context)

def login(request):
    return render(request, 'users/login.html')


def create(request):
    registered = False

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
            request.session['registered'] = True
        else:
            print(user_form.errors, profile_form.errors)


    return redirect('users:register')
