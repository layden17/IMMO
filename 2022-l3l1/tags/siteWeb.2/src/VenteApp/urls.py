"""
all the urls used by  ProduitApp

"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import VenteApp
from . import views

app_name = 'VenteApp'

urlpatterns = [
    path('venteApp/', VenteApp.views.index, name='venteApp'),
    path('proformat/', VenteApp.views.proformat, name="proformat"),
    #path('create_order/', VenteApp.views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', VenteApp.views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', VenteApp.views.deleteOrder, name="delete_order"),
    path('recherche/', VenteApp.views.searchBar, name="search"),

    path('pdf_view/', VenteApp.views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', VenteApp.views.DownloadPDF.as_view(), name="pdf_download"),

    path('sql/',VenteApp.views.requeteManuel,name="requete"),
    path('sql2/', VenteApp.views.requeteManuel2, name="requete2"),
    path('data/', VenteApp.views.deleteData, name="data"),


    path('orders/<int:pk>', views.OrderDetail.as_view(), name='order_details'),
    path('order/create/', views.OrderCreate.as_view(), name='order_create'),
    path('orders/', views.OrderList.as_view(), name='orders'),
    path('orders/<int:pk>', views.OrderDetail.as_view(), name='order_details'),

    #path('order/create/', views.OrderCreate.as_view(), name='order_create'),
    #path('order/update/<int:order_id>', views.order_update, name='order_update'),
    #path('order/delete/<int:pk>', views.OrderDelete.as_view(), name='order_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)