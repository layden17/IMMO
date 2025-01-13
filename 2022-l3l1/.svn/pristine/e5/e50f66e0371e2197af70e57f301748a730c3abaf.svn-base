from django.contrib import admin
from django.urls import path, include
from FournisseursApp import views
from .views import FournisseurUpdateView

from FournisseursApp.views import FournisseurDeleteView
urlpatterns=[
    path('fournisseurs/',views.index,name='fournisseurs'),
    path('ajout_fournisseurs/', views.ajout_fournisseurs, name='ajout_fournisseurs'),
   path('fournisseurs/supprimer/<int:pk>/', FournisseurDeleteView.as_view(), name='supprimer_fournisseur'),
   path('<int:pk>/modifier/', FournisseurUpdateView.as_view(), name='modifier_fournisseur'),
   path('fournisseurs/search/', views.search_fournisseurs, name='search_fournisseurs'),
path('tri_fournisseurs/<str:tri>/', views.tri_fournisseurs, name='tri_fournisseurs'),
]

