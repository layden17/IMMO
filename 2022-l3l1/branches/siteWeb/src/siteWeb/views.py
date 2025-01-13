
from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponseRedirect
from .forms import CreationUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from ProduitApp.models import ProduitBrut,AutreProduit

import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

@login_required(login_url="login")
def index(request):
    return render(request, "siteWeb/index.html")

def achat(request):
    return render(request, "AchatApp/achat.html")

def alertesStock(request):
    return render(request, "siteWeb/alertesStock.html")

def client(request):
    return render(request, "siteWeb/client.html")

def fournisseur(request):
    return render(request, "FournisseurApp/fournisseur.html")

def produit(request):
    return render(request, "siteWeb/produit.html")


def vente(request):
    return render(request, "siteWeb/vente.html")


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Username or password is incorrect' )
    context = {}
    return render(request, "siteWeb/login.html",context)

def registerPage(request):

    form = CreationUserForm()

    if request.method == 'POST':
        form = CreationUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user )
            return redirect('index')
    context = {'form' : form}
    return render(request, "siteWeb/register.html", context)

def logOutUser(request):
    logout(request)
    return redirect('login')

def venue_pdf(request):

    buf = io.BytesIO()

    c = canvas.Canvas(buf, pagesize=letter,bottomup=0)

    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)

    lines = ["This is line 1",
             "This is line 2",
             "This is line 3",
             ]
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='pythonPDF.pdf')






def produit_en_rupture(request):
    """
    Vue qui retourne les produits en rupture de stock .


    Le contexte contient les variables suivantes :
    - produits bruts en rupture de stock 
    - autres produits en rupture de stock
    
    """


    produits_bruts=ProduitBrut.objects.all()
    produit_brut_en_rupture=[]
    
    for produit in produits_bruts:
        if produit.stock_quintal<=produit.stock_alerte:
            produit_brut_en_rupture.append(produit)
    

    autres_produits=AutreProduit.objects.all()
    autre_produit_en_rupture=[]
    for produit in autres_produits:
        if produit.quantite<=produit.stock_alerte:
            autre_produit_en_rupture.append(produit)
    context={
        'produit_brut_en_rupture': produit_brut_en_rupture,
        'autre_produit_en_rupture':autre_produit_en_rupture
    }

    return render(request, 'siteWeb/alertesStock.html', context)


