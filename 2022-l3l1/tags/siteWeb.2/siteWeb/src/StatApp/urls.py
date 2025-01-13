"""
all the urls used by  StatApp

"""

from django.urls import path
from . import views


app_name = 'StatApp'

urlpatterns = [
    path('statistique/', views.all_stat, name="statistique"),

]