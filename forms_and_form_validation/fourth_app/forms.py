from django import forms
from django.core import validators

class FourthForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)


    # when you have a method title 'clean' it can be used to validate the entire form, it is automatically activated.  Here we just check that email matches, we could do much more.
    def clean(self):
        # using super() below grabs all the clean data for the form
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            print('emails dont match!')
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
