from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ClientApp.forms import CustomForms
from ClientApp.models import Client


def index(request):

    form = CustomForms()

    if request.method == 'POST':
        form = CustomForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('compteApp')

    return render(request, "index.html", {'form' : form , 'dataClient' : Client.objects.all()})

