from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from AvisApp.forms import AvisForm
from AvisApp.models import Avis


def index(request):
    avis = Avis.objects.all()
    if request.method =='POST' :
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
        "PRODELIMMO: "+name,
        message,
        'settings.EMAIL_HOST_USER',
        [email],
        fail_silently=False)
    return render(request, "IMMO/index.html",{'avis': avis})


def ajouter_avis(request):
    if request.method == 'POST':
        form = AvisForm(request.POST)
        if form.is_valid():
            nouvel_avis = form.save(commit=False)
            nouvel_avis.save()
            return redirect('index')
    else:
        form = AvisForm()
    return render(request, 'IMMO/ajouter_avis.html', {'form': form})

def test(request):
    return render(request, 'IMMO/test.html')
