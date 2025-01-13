"""
all the urls used by  ProduitApp

"""

from django.urls import path
from . import views
from .views import modifier_produit,supprimer_autre_produit, autre_produit_detail,modifier_autre_produit,modifier_categorie,supprimer_categorie
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ProduitApp'
            
urlpatterns = [
    path('produit_brut/',views.produit_brut,name='produit_brut'),
    path('produit_brut/modifier/<int:pk>/', modifier_produit.as_view(), name='modifier_produit'),
    path('historique_prix_achat_quintal/', views.historique_prix_achat_quintal, name='historique_prix_achat_quintal'),
    path('historique_prix_vente_quintal/', views.historique_prix_vente_quintal, name='historique_prix_vente_quintal'),


    path('autre_produit/',views.autre_produit,name='autre_produit'),
    path('autre_produit/modifier/<int:pk>/', modifier_autre_produit.as_view(), name='modifier_autre_produit'),
    path('autre_produit/add/', views.add_autre_produit, name='add_autre_produit'),
    path('autre_produit/detail/<int:pk>/', autre_produit_detail.as_view(), name='autre_produit_detail'),
    path('autre_produit/supprimer/<int:pk>/', supprimer_autre_produit.as_view(), name='supprimer_autre_produit'),
    path('autre_produit/recherche/', views.recherche_autre_produit, name='recherche_autre_produit'),

   


    path('cadre/',views.cadre ,name='cadre'),
    path('cadre/create_cadre', views.createCadre, name='create_cadre'),
    path('cadre/supprimer/<int:id>/', views.supprimer_cadre, name='supprimer_cadre'),
    path('cadre/modifier/<int:pk>/', views.modifier_cadre.as_view(), name='modifier_cadre'),
    path('tri_cadre/<str:tri>/', views.tri_cadre, name='tri_cadre'),


    path('produitApp/', views.index, name='produitApp'),


    path('categorie/', views.categorie, name='categorie'),
    path('create_categorie/', views.create_category, name='create_categorie'),
    path('categorie/modifier/<int:pk>/', modifier_categorie.as_view(), name='modifier_categorie'),
    path('categorie/supprimer/<int:pk>/',supprimer_categorie.as_view(),name='supprimer_categorie'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)