from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def index(request):
    form = forms.ThirdForm()
    context = { 'form': form }
    return render(request, 'third_app/index.html', context)


def result(request):
    if request.method == 'POST':
        form = forms.ThirdForm(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])
    return redirect('third:index')
