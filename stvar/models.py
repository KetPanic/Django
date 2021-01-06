from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Stvar(models.Model):
    ime = models.CharField(max_length=250)
    cena = models.PositiveIntegerField()
    opis = models.CharField(max_length=5000)
    kategorija = models.CharField(max_length=50)
    slika = models.FileField(blank=True)
    grad = models.CharField(max_length=30)
    telefon = models.PositiveIntegerField()

    korisnik = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ime

class Ocene(models.Model):
    ocena = models.IntegerField(default=None, validators=[MaxValueValidator(5), MinValueValidator(1)], null=True)
    korisnik = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    proizvod = models.ForeignKey(Stvar, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ocena)