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

import FournisseursApp




from ClientApp import views
from VenteApp import views
from ProduitApp import views
from .views import index, venue_pdf, loginPage, registerPage, logOutUser, achat, alertesStock, client, fournisseur
from .views import produit, statistique, vente
from FournisseursApp import views

urlpatterns = [
    path('login/', loginPage, name="login"),
    path('logout/', logOutUser, name="logout"),
    
    path('alertes/', alertesStock, name="alertes"),
    path('client/', client, name="client"),
    path('compte/', registerPage, name="compte"),
    path('fournisseur/', fournisseur, name="fournisseur"),
    path('statistique/', statistique, name="statistique"),
    path('vente/', vente, name="vente"),

    path("", index, name="index"),

    path('venue_pdf/', venue_pdf, name="venue_pdf"),
    path('compteApp/', ClientApp.views.index, name='compteApp'),

    #VENTE URL
    path('venteApp/', include('VenteApp.urls',namespace='venteApp')),
    path('proformat/', VenteApp.views.proformat, name="proformat"),
    path('create_order/', VenteApp.views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', VenteApp.views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', VenteApp.views.deleteOrder, name="delete_order"),
    path('recherche/', VenteApp.views.searchBar, name="search"),

    #PRODUIT URL
    path('', include('ProduitApp.urls')),

    path('admin/', admin.site.urls),
    #FournisseurApp
    
    path('',include(('FournisseursApp.urls','FournisseursApp'),namespace='FournisseursApp')),
    
    path('fournisseurs/',FournisseursApp.views.index,name='FournisseursApp'),
    path('ajout_fournisseurs/',FournisseursApp.views.ajout_fournisseurs,name='ajout_fournisseurs'),
    path('fournisseurs/supprimer/<int:pk>/', FournisseursApp.views.FournisseurDeleteView.as_view(), name='supprimer_fournisseur'),
    #AchatApp
    path('',include(('AchatApp.urls','AchatApp'),namespace='AchatApp')),

]
