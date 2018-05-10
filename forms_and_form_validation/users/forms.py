from django import forms


class UserForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # You can change the labels to the inputs like so
    verify_email = forms.EmailField(label='Enter your email again:')
    # You can change the type of input from text to textarea like so
    text = forms.CharField(widget=forms.Textarea)
