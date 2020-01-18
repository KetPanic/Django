from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Stvar
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, StvarForm
from django.contrib.auth import logout
from django.db.models import Q

# Create your views here.

strana=True

def firstOpen(request):
    strana = True
    return redirect("stvar:index")

def index(request):
    strana = True
    sveStvari = Stvar.objects.all()
    query = request.GET.get("q")
    if query:
        sveStvari = Stvar.objects.filter()
        sveStvari = sveStvari.filter(
            Q(ime__icontains=query) |
              Q(kategorija__icontains=query) |
            Q(grad__icontains=query)
        ).distinct()
    #jednaStvar = get_object_or_404(Stvar, pk=1)
    #template = loader.get_template('stvar/index.html')
    context = {
        'stvari' : sveStvari,
        "strana": strana
    }
    return render(request, 'stvar/index.html', context)
    #return HttpResponse(template.render(context, request))
    #return HttpResponse("<h1>Ovo je stvar homepage</h1>")

def prodaj(request):
    strana = False
    user = request.user
    stvari = Stvar.objects.filter(korisnik=user.pk)
    return render(request, 'stvar/prodaj.html', {"stvari":stvari, "strana":strana})

def izmeniStvar(request, id):
    strana=False
    if request.method == "GET":
        stvar = Stvar.objects.get(pk=id)
        form = StvarForm(initial={"ime":stvar.ime, "kategorija":stvar.kategorija,
                                  "cena":stvar.cena, "slika":stvar.slika, "opis":stvar.opis,
                                  "grad":stvar.grad, "telefon":stvar.telefon})
        '''
        form["ime"] = stvar.ime
        form["kategorija"] = stvar.kategorija
        form["cena"] = stvar.cena
        form["slika"] = stvar.slika
        form["opis"] = stvar.opis
        form["grad"] = stvar.grad
        form["telefon"] = stvar.telefon'''
        return render(request, 'stvar/create_stvar.html', {"form":form, "strana":strana})
    form = StvarForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        stvar = Stvar.objects.get(pk=id)
        stvar.korisnik = request.user
        telefon = form["telefon"].value()
        if len(str(telefon)) < 9 or len(str(telefon)) > 10:
            context = {
                'form': form,
                'error_message': 'Broj telefona mora imati 9 ili 10 cifa',
                "strana":strana
            }
            return render(request, 'stvar/create_stvar.html', context)
        try:
            stvar.slika = request.FILES['slika']
            file_type = stvar.slika.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type != 'jpg' and file_type != 'png' and file_type != 'jpeg':
                context = {
                    'form': form,
                    'error_message': 'Slika mora biti png, jpg ili jpeg',
                    "strana":strana
                }
                return render(request, 'stvar/create_stvar.html', context)
        except:
            print("NemaSlike")
        stvar.telefon = form["telefon"].value()
        stvar.cena = form["cena"].value()
        stvar.opis = form["opis"].value()
        stvar.ime = form["ime"].value()
        stvar.grad = form["grad"].value()
        stvar.kategorija = form["kategorija"].value()
        stvar.save()
        print("Valjda je sacuvano")
        return redirect('/stvar/prodaj')

def create_stvar(request):
    strana=False
    form = StvarForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        stvar = form.save(commit=False)
        stvar.korisnik = request.user
        stvar.slika = request.FILES['slika']
        file_type = stvar.slika.url.split('.')[-1]
        file_type = file_type.lower()
        telefon = form["telefon"].value()
        if len(str(telefon)) < 9 or len(str(telefon)) > 10:
            context = {
                'form': form,
                'error_message': 'Broj telefona mora imati 9 ili 10 cifa',
                "strana":strana
            }
            return render(request, 'stvar/create_stvar.html', context)
        if file_type != 'jpg' and file_type != 'png' and file_type != 'jpeg':
            context = {
                'form' : form,
                'error_message' : 'Slika mora biti png, jpg ili jpeg',
                "strana": strana
            }
            return render(request, 'stvar/create_stvar.html', context)
        stvar.save()
        return redirect('/stvar/index')
    context = {
        "form": form,
    }
    return render(request, 'stvar/create_stvar.html', context)

def detalji(request, id):
    stvar = Stvar.objects.get(pk=id)
    korisnik = stvar.korisnik
    user = request.user
    #korisnik = User.objects.get(pk=ajdi)
    return render(request, 'stvar/detalji.html', {"stvar":stvar, "korisnik":korisnik, "strana":strana})

def detaljiProdaj(request, id):
    strana=False
    stvar = Stvar.objects.get(pk=id)
    korisnik = stvar.korisnik
    user = request.user
    #korisnik = User.objects.get(pk=ajdi)
    return render(request, 'stvar/detalji_prodaj.html', {"stvar":stvar, "korisnik":korisnik,"strana":strana})



def detaljiKupi(request, id):
    stvar = Stvar.objects.get(pk=id)
    korisnik = stvar.korisnik
    user = request.user
    #korisnik = User.objects.get(pk=ajdi)
    return render(request, 'stvar/detalji_kupi.html', {"stvar":stvar, "korisnik":korisnik, "strana":strana})

def obrisiStvar(request, id):
    strana=False
    Stvar.objects.filter(pk=id).delete()
    if(strana):
        return redirect('stvar:index')
    else:
        return redirect('stvar:prodaj')

def kupiArtikal(request, id):
    stvar = Stvar.objects.get(pk=id)
    return render(request, 'stvar/kupi_artikal.html', {"stvar": stvar, "strana":strana})

def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('stvar:index')
        return render(request, 'stvar/login.html', {"strana":strana})
    else:
        return render(request, "stvar/login.html", {"strana":strana})

def logoutUser(request):
    logout(request)
    #return render(request, 'stvari/index.html')
    strana = True
    return redirect('stvar:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'stvar/regustration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form":form, "strana":strana})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('stvar:index')

        return render(request, self.template_name, {'form':form, "strana":strana})