from django import forms
from .models import *
class customform(forms.Form):
    username=forms.CharField(max_length=30, label="username",widget=forms.TextInput(attrs={
        'placeholder':'your full name',
        'class':'form-control'
    }))
    first_name=forms.CharField(max_length=30, label="first_name",widget=forms.TextInput(attrs={
        'placeholder':'your first_name',
        'class':'form-control'
    }))
    last_name=forms.CharField(max_length=30, label="last_name",widget=forms.TextInput(attrs={
        'placeholder':'your  last_name',
        'class':'form-control'
    }))
    email=forms.EmailField(max_length=30, label="email",widget=forms.TextInput(attrs={
        'placeholder':'your email',
        'class':'form-control'
    }))
    password=forms.CharField(max_length=30, label="password",widget=forms.TextInput(attrs={
        'placeholder':'your password',
        'class':'form-control'
    }))
    confirm_password=forms.CharField(max_length=30, label="confirm_password",widget=forms.TextInput(attrs={
        'placeholder':'confirm_password',
        'class':'form-control'
    }))

class loginform(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)

