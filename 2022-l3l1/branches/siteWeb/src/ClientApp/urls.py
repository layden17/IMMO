"""
all the urls used by  ProduitApp

"""

from django.urls import path

import ClientApp
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ClientApp'

urlpatterns = [
    path('clientApp/', ClientApp.views.index, name='clientApp'),
    path('create_customer/', ClientApp.views.createCustomer, name="create_customer"),
    path('update_customer/<str:pk>/', ClientApp.views.updateCustomer, name="update_customer"),
    path('delete_customer/<str:pk>/', ClientApp.views.deleteCustomer, name="delete_customer"),
    path('search/', ClientApp.views.searchBar, name="searchClient"),
    #path('pdf_view/', ClientApp.views.ViewPDF.as_view(), name="pdf_view"),
    #path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


