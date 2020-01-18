from django.urls import path
from . import views

app_name= 'stvar'

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.firstOpen, name='firstOpen'),
    path('logout', views.logoutUser, name='logout'),
    path('login', views.loginUser, name='login'),
    path('registracija', views.UserFormView.as_view(), name='registracija'),
    path('dodaj_stvar', views.create_stvar, name='dodajStvar'),
    path('detalji/<int:id>', views.detalji, name='detalji'),
    path('detalji_kupi/<int:id>', views.detaljiKupi, name='detalji_kupi'),
    path('detalji_prodaj/<int:id>', views.detaljiProdaj, name='detalji_prodaj'),
    path('prodaj', views.prodaj, name='prodaj'),
    path('kupi_artikal/<int:id>', views.kupiArtikal, name='kupi_artikal'),
    path('obrisi_stvar/<int:id>', views.obrisiStvar, name='obrisi_stvar'),
    path('izmeni_stvar/<int:id>', views.izmeniStvar, name='izmeni_stvar'),
]