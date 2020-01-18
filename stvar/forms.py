from django.contrib.auth.models import User
from django import forms
from .models import Stvar


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]


class StvarForm(forms.ModelForm):
    class Meta:
        model = Stvar
        fields = ["ime", "cena", "opis", "kategorija", "slika", "grad", "telefon"]
