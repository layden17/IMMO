from io import BytesIO
from typing import io


import data as data
from django.db import transaction
from django.db.models import Q
from django.forms import inlineformset_factory
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from xhtml2pdf import pisa

from ClientApp.models import Client
from ProduitApp.models import Categorie, ProduitBrut, Produit
from VenteApp.forms import VenteForms, OrderItemFormset, ArticleForms, OrderCadreFormset, ArticleCadreForms
from VenteApp.models import Commande, Article, ArticleCadre


def index(request):

    form = VenteForms()

    total_produit = Produit.objects.count()
    total_client = Client.objects.count()
    total_oder = Commande.objects.count()


    context = {
        'form': form,
        'dataCommande': Commande.objects.all(),
        'product': total_produit,
        'customer': total_client,
        'order': total_oder,

    }



    return render(request, "VenteApp/index.html",context )

def proformat(request):

    return render(request,"VenteApp/proformat.html")

def createOrder(request):

    form = VenteForms()

    if request.method == 'POST':
        form = VenteForms(request.POST, request.FILES)
        products = request.POST.getlist('unProduit')
        quantities = request.POST.getlist('quantite')
        for i, product_id in enumerate(products):
            product = Produit.objects.get(id=product_id)
            quantity = int(quantities[i])
            Article.objects.create(order=Commande, product=product, quantity=quantity)

        if form.is_valid():
            form.save()
            return redirect('VenteApp:venteApp')

    context = {'form' : form , 'dataCommande' : Commande.objects.all()}
    return render(request, 'VenteApp/order_form.html', context)

def updateOrder(request, pk):

    order = Commande.objects.get(id=pk)
    form = VenteForms(request.POST, instance=order)
    ItemFormset = inlineformset_factory(Commande, Article, form=ArticleForms, extra=1)
    ItemCadre = inlineformset_factory(Commande, ArticleCadre, form=ArticleCadreForms, extra=1)

    if request.method == 'POST':

        formset = ItemFormset(request.POST, instance=order)
        cadre = ItemCadre(request.POST, instance=order)

        if formset.is_valid() and cadre.is_valid():
            form.save()
            formset.save()
            cadre.save()
            return redirect('VenteApp:venteApp')
        elif formset.is_valid() :
            form.save()
            formset.save()
            return redirect('VenteApp:venteApp')
        elif cadre.is_valid() :
            form.save()
            cadre.save()
            return redirect('VenteApp:venteApp')
    else:

        form = VenteForms(instance=order)
        formset = ItemFormset(instance=order)
        cadre = ItemCadre(instance=order)

    return render(request, 'VenteApp/update_form.html', {'form':form, 'formset' : formset, 'cadre' : cadre})



def deleteOrder(request,pk):
    order = Commande.objects.get(id=pk)
    if request.method == "POST" :
        order.delete()
        return redirect('VenteApp:venteApp')
    context = {'item':order}
    return render(request,'VenteApp/delete.html', context)

def searchBar(request):
    if request.method=='GET':
        query = request.GET.get('requete')
        if query:
            commandes = Commande.objects.filter(Q(client__prenom__icontains=query) | Q(client__nom__icontains=query))
            return render(request, 'VenteApp/searchbar.html', {'commandes':commandes})
        else:
            print("Aucun résultat")
            return request(request, 'VenteApp/searchbar.html', {})

def render_to_pdf(template,context_dict={}):
    dataCommande = Commande.objects.all()
    context = {'dataCommande': dataCommande}
    template = get_template(template)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO_8859-1")),result, STATIC_ROOT="Users/lathan/Documents/Projet_L3L1/2022-l3l1/branches/siteWeb/src/static")
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

# Opens up page as PDF
class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('VenteApp/pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

# Automaticly downloads to PDF file
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('VenteApp/pdf_template.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        content = 'attachment; filename="listeCommandes.pdf"'
        response['Content-Disposition'] = content
        return response

def requeteManuel(request):
    donnee = Produit.objects.create(
    designation = "machine",
    description = "metaux de base",
    TVA= 3,
    categorie= Categorie.objects.get(id=1),
    stock_alerte="100"),

    return redirect('VenteApp:venteApp')

def requeteManuel2(request):
    donnee = ProduitBrut.objects.create(
    designation = "FER 10/",
    description = "metaux de base",
    TVA= 3,
    categorie= Categorie.objects.get(id=1),
    stock_alerte="100",
    stock_barre = 100,
    stock_metre = 40,
    stock_quintal = 50,
    prix_barre = 2030,
    prix_quintal = 319,
    prix_metre = 8093,
    prix_achat_quintal = 9897,
    prix_achat_barre = 8777,
    prix_achat_metre =7987,
    )

    return redirect('VenteApp:venteApp')

def deleteData(request):

        produit = Produit.objects.get(id=1)
        produit.delete()
        return redirect('VenteApp:venteApp')


#VIEWS 2.0


class OrderList(ListView):
    template_name = 'VenteApp/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Commande.objects.order_by('-date_creation')


class OrderDetail(DetailView):
    model = Commande
    template_name = 'VenteApp/order_details.html'

class OrderCreate(CreateView):
    model = Commande
    fields = ['id', 'client','date_reception', 'statut']
    template_name = 'VenteApp/order_create.html'
    success_url = reverse_lazy('VenteApp:venteApp')

    def get_context_data(self, **kwargs):
        data = super(OrderCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = OrderItemFormset(self.request.POST)
            data['cadre'] = OrderCadreFormset(self.request.POST)
        else:
            data['items'] = OrderItemFormset()
            data['cadre'] = OrderCadreFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        with transaction.atomic():
            self.object = form.save()

            if items.is_valid():
                items.instance = self.object
                items.save()

        cadre = context['cadre']
        with transaction.atomic():
            self.object = form.save()

            if cadre.is_valid():
                cadre.instance = self.object
                cadre.save()

        return super(OrderCreate, self).form_valid(form)


def order_update(request, order_id):

    order = Commande.objects.get(id=order_id)
    form = VenteForms(request.POST, instance=order)
    ItemFormset = inlineformset_factory(Commande, Article, form=VenteForms, extra=1)

    if request.method == 'POST':

        formset = ItemFormset(request.POST, instance=order)

        if formset.is_valid():
            form.save()
            formset.save()
            from django.contrib import messages
            messages.success(request, 'Order successfully updated')
    else:

        form = VenteForms(instance=order)
        formset = ItemFormset(instance=order)

    return render(request, 'customers/order_update.html', {'form':form, 'formset' : formset})


def get_item_price(request):

        item_id = request.GET['item_id']
        qty = request.GET['qty']
        shipping_fee = request.GET['shipping_fee']

        item = Produit.objects.get(pk=item_id)

        total_price = ( (item.price * float(qty) ) + float(shipping_fee) )
        return JsonResponse(total_price, safe=False)

def ma_vue(request):
    tri = request.GET.get('sort', 'num')
    if tri == 'client':
        objets = Commande.objects.all().order_by('client')
    elif tri == 'quantite':
        objets = Commande.objects.all().order_by('quantite')
    elif tri == 'total':
        objets = Commande.objects.all().order_by('total')
    elif tri == 'date_creation':
        objets = Commande.objects.all().order_by('date_creation')
    elif tri == 'date_reception':
        objets = Commande.objects.all().order_by('date_reception')
    else:
        objets = Commande.objects.all().order_by('num')

    return render(request, 'VenteApp/index.html', {'objets': objets})