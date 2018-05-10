from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    form = forms.UserForm()
    context = { 'form': form }
    return render(request, 'users/index.html', context)
