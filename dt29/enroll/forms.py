from django import forms

# create form classes

class StudentRegistration(forms.Form):
    name = forms.CharField(initial="Ashish", help_text="Enter your name")
    email = forms.EmailField()