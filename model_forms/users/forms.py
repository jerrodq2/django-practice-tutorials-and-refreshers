from django import forms
from .models import User

# form 1
class MainUserForm(forms.ModelForm):
    class Meta():
        model = User
        # This is how you include all fields from the model
        fields = '__all__'


# form 2
class ExludedUserForm(forms.ModelForm):
    class Meta():
        model = User
        # This is how you exlude specific fields, all others will be included by default
        exclude = ['last', 'summary'] # specify which fields get excluded


# form 3
class IncludedUserForm(forms.ModelForm):
    class Meta():
        model = User
        # This is how you include specific fields, all others will be excluded by default
        fields = ['first', 'email'] # specify which fields get included
