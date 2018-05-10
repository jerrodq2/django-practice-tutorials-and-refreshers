from django import forms
from django.core import validators

# Example of a custom validation method. Django knows it is used for validation when we pass in 'value', we can then simply pass it into an input like we do for the name field below
def check_for_j(value):
    if value[0].lower() != 'j':
        print('problem with check_for_j')
        raise forms.ValidationError('Name needs to start with Z')

class SecondForm(forms.Form):
    name = forms.CharField(validators=[check_for_j])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    # The below example is a hidden input that should be blank, bots would fill it in with data, so it's a security measure. We can change various properties of the input like so
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
    # validators=[validators.MaxLengthValidator(0)]
    )
    # Adding the above validators attribute to the charfield has the same effect as the below clean_botcatcher method, it just enforces that the botcatcher can't have a length of more than 0.


    # This is an example of basic validations with the 'clean' method. By creating a function named "clean_inputNameHere", Django knows it is a validation/clean method for a specific input from this form. The name is important, if I named it "clean_eh", it wouldn't do anything since this form doesn't have an 'eh' field/input. But since It's named after my botcatcher field, this method is called automatically upon form submission
    def clean_botcatcher(self):
        print('inside clean_botcatcher')
        botcatcher = self.cleaned_data['botcatcher']

        if len(botcatcher):
            print('inside if')
            raise forms.ValidationError("Gotcha Bot")
        return botcatcher
