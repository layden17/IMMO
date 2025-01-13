from django.contrib import admin
from django.urls import path, include
from AchatApp import views
from AchatApp.views import AchatDeleteView,AchatUpdateView
from django.views.i18n import JavaScriptCatalog
urlpatterns=[
    path('achat/',views.index,name='achat'),
    path('<int:pk>/delete/', AchatDeleteView.as_view(), name='supprimer_achat'),
    path('<int:pk>/update/', AchatUpdateView.as_view(), name='modifier_achat'),
    path('ajouter_produits/',views.ajouter_produits,name='ajouter_produits'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
]