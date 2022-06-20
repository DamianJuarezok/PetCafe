from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name','last_name']
        help_texts = {k:'' for k in fields}