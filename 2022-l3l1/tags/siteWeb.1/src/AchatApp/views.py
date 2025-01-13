from django.shortcuts import render
from .models import Achat
# Create your views here.
def index(request):

    return render(request,"achat.html",{"achats":Achat.objects.all()})