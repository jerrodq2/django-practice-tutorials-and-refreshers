from django import forms
from django.core import validators

# Example of a custom validation method. Django knows it is used for validation when we pass in 'value', we can then simply pass it into an input like we do for the name field below
def check_for_j(value):
    if value[0].lower() != 'j':
        print('problem with check_for_j')
        raise forms.ValidationError('Name needs to start with Z')

class ThirdForm(forms.Form):
    name = forms.CharField(validators=[check_for_j])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
