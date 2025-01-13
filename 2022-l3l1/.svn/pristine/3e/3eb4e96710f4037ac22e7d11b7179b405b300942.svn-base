from django.contrib import admin
from django.urls import path, include
from FournisseursApp import views  # Importe les vues de l'application FournisseursApp
from .views import FournisseurUpdateView  # Importe la vue FournisseurUpdateView pour la mise à jour des fournisseurs
from FournisseursApp.views import FournisseurDeleteView  # Importe la vue FournisseurDeleteView pour la suppression des fournisseurs

urlpatterns=[
    path('fournisseurs/',views.index,name='fournisseurs'),  # URL pour afficher la liste des fournisseurs
    path('ajout_fournisseurs/', views.ajout_fournisseurs, name='ajout_fournisseurs'),  # URL pour ajouter un nouveau fournisseur
    path('fournisseurs/supprimer/<int:pk>/', FournisseurDeleteView.as_view(), name='supprimer_fournisseur'),  # URL pour supprimer un fournisseur spécifique
    path('<int:pk>/modifier/', FournisseurUpdateView.as_view(), name='modifier_fournisseur'),  # URL pour mettre à jour les informations d'un fournisseur spécifique
    path('fournisseurs/search/', views.search_fournisseurs, name='search_fournisseurs'),  # URL pour effectuer une recherche de fournisseurs
    path('tri_fournisseurs/<str:tri>/', views.tri_fournisseurs, name='tri_fournisseurs'),  # URL pour trier les fournisseurs par ordre alphabétique
    path('fournisseurs/factures_detail/<int:pk>/', views.factures_detail, name='factures_detail'),  # URL pour afficher les détails des factures pour un fournisseur spécifique
]
