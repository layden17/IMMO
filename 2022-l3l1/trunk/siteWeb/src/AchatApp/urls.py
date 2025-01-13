from django.contrib import admin
from django.urls import path, include
from AchatApp import views
from AchatApp.views import AchatDeleteView,AchatUpdateView
urlpatterns=[
    path('achat/',views.index,name='achat'),
    path('ajout_achat/', views.ajout_achat, name='ajout_achat'),
    path('ajouter_facture/<int:fournisseur_id>/', views.ajouter_facture, name='ajouter_facture'),
    path('ajouter_facture/fournisseur/<int:fournisseur_id>/achat/<int:achat_id>/', views.ajouter_facture, name='ajouter_facture'),
    path('<int:pk>/delete/', AchatDeleteView.as_view(), name='supprimer_achat'),
    path('<int:pk>/update/', AchatUpdateView.as_view(), name='modifier_achat'),
    path('ajouter_produits/',views.ajouter_produits,name='ajouter_produits')
]