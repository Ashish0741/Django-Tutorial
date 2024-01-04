from django import forms

# create form classes

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    key = forms.CharField(widget=forms.HiddenInput())