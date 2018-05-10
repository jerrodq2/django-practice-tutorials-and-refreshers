from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def index(request):
    form = forms.SecondForm()
    context = { 'form': form }
    return render(request, 'second_app/index.html', context)


def result(request):
    if request.method == 'POST':
        form = forms.SecondForm(request.POST)
        # The below 'form.is_valid()' line is used automatically with the validation methods in the form files. If they all pass, the below passes as true, if even one validation method doesn't pass, then the .is_valid() method returns false
        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])
    return redirect('second:index')
