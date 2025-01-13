"""siteWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import VenteApp
import ProduitApp
import ClientApp
import AchatApp
import FournisseursApp
import StatApp




from ClientApp import views
from ProduitApp import views
from AchatApp import views
from .views import index,  produit_en_rupture, venue_pdf, loginPage, registerPage, logOutUser, achat, alertesStock, client, fournisseur, produit
from .views import vente
from FournisseursApp import views
from StatApp import views

from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('login/', loginPage, name="login"),
    path('logout/', logOutUser, name="logout"),
    
    path('alertes/', produit_en_rupture, name="alertes"),
    path('client/', client, name="client"),
    path('compte/', registerPage, name="compte"),
    path('fournisseur/', fournisseur, name="fournisseur"),
    path('vente/', vente, name="vente"),
    

    path("", index, name="index"),

    path('venue_pdf/', venue_pdf, name="venue_pdf"),

    #CLIENT URL
    path('', include('ClientApp.urls')),

    #VENTE URL
    path('', include('VenteApp.urls')),

    #PRODUIT URL
    path('', include('ProduitApp.urls')),


    path('admin/', admin.site.urls),
    #FournisseurApp
    
    path('',include(('FournisseursApp.urls','FournisseursApp'),namespace='FournisseursApp')),

    path('fournisseurs/',FournisseursApp.views.index,name='FournisseursApp'),
    path('ajout_fournisseurs/',FournisseursApp.views.ajout_fournisseurs,name='ajout_fournisseurs'),
    path('fournisseurs/supprimer/<int:pk>/', FournisseursApp.views.FournisseurDeleteView.as_view(), name='supprimer_fournisseur'),
    #AchatApp
    path('achat/',AchatApp.views.index,name='achat'),
    path('',include(('AchatApp.urls','AchatApp'),namespace='AchatApp')),
    path('ajouter_produits', AchatApp.views.ajouter_produits, name='ajouter_produits'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('<int:pk>/delete/', AchatApp.views.AchatDeleteView.as_view(), name='supprimer_achat'),
    path('<int:pk>/update/', AchatApp.views.AchatUpdateView.as_view(), name='modifier_achat'),

    #Stat
    path('statistique/',StatApp.views.all_stat, name="statistique"),
]
