"""
all the urls used by  ProduitApp

"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import VenteApp
from . import views
from .views import total_qty

app_name = 'VenteApp'

urlpatterns = [
    path('vente/', VenteApp.views.index, name='venteApp'),

    path('update_order/<str:pk>/', VenteApp.views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', VenteApp.views.deleteOrder, name="delete_order"),
    path('recherche/', VenteApp.views.searchBar, name="search"),

    path('pdf_view/', VenteApp.views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', VenteApp.views.DownloadPDF.as_view(), name="pdf_download"),

    path("order/create/cadre", VenteApp.views.createCadre,name="cadre"),


    path('orders/<int:pk>', views.OrderDetail.as_view(), name='order_details'),
    path('orders/client/commandes', views.commandes_client, name="commandes"),
    path('order/create/', views.OrderCreate.as_view(), name='order_create'),
    path('orders/', views.OrderList.as_view(), name='orders'),

    path('<int:commande_id>/total_qty/', total_qty, name='total_qty'),

    path('customer/<int:client_id>/orders/', views.commandes_client, name='commandes'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)