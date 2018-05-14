from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def form_one(request):
    context = { 'form': MainUserForm() }
    return render(request, 'users/form_one.html', context)

def form_one_result(request):
    if request.method == "POST":
        form = MainUserForm(request.POST)

        # The is_valid method below is determined based on the model field validations. For example, we put email as unique, if you submit the form with an email that is already in the db, the is_valid will return false.
        if form.is_valid():
            print('valid')
            # If the form is valid, it is automatically saved into the db. The difference between commit being True or False is that True saves it to the db automatically. If it was "commit = False", it would create the User object, but wouldn't save it, which could be useful if you need to mess with a few of the fields before saving it. You would then just write 'form.save()' to save it to the db.
            form.save(commit=True)
        else:
            print('ERROR FORM INVALID')

    return redirect('users:form_one')


def form_two(request):
    context = { 'form': ExludedUserForm() }
    return render(request, 'users/form_two.html', context)
def form_two_result(request):
    if request.method == "POST":
        form = ExludedUserForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save(commit=True)
        else:
            print('ERROR FORM INVALID')
    return redirect('users:form_two')

def form_three(request):
    context = { 'form': IncludedUserForm() }
    return render(request, 'users/form_three.html', context)
def form_three_result(request):
    if request.method == "POST":
        form = IncludedUserForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save(commit=True)
        else:
            print('ERROR FORM INVALID')
    return redirect('users:form_three')
