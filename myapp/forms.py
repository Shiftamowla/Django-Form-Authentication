from django import forms
from .models import *
class customform(forms.Form):
    username=forms.CharField(max_length=100)
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField(max_length=100)
    confirm_password=forms.CharField(max_length=100)
class loginform(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)

