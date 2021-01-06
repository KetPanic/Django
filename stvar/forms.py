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

INTEGER_CHOICES = [tuple([x,x]) for x in range (1,5)]
class OceneFrom(forms.Form):
    ocena = forms.IntegerField(label='--', widget=forms.Select(choices=INTEGER_CHOICES))
