from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def register(request):
    return render(request, 'users/register.html')

def login(request):
    return render(request, 'users/login.html')


def create(request):
    return redirect('users:register')
