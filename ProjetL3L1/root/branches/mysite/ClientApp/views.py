from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ClientApp.form import CustomForms
from ClientApp.models import Client


def index2(request):

    form = CustomForms()

    if request.POST == 'POST':
        form = CustomForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('student/')
        else:
            form = CustomForms()
        context = {'form': form}
        return render(request, 'ClientApp/index.html', context)


def index(request):

    form = CustomForms()

    if request.method == 'POST':
        form = CustomForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student')

    return render(request, 'clientApp/index.html', {'form' : form , 'dataClient' : Client.objects.all()})