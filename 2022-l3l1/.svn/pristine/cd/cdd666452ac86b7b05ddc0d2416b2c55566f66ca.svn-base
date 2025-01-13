import sys
from _decimal import Decimal
from datetime import datetime
from io import BytesIO



import data as data
from django.contrib import messages
from django.core.validators import MinValueValidator
from django.db import transaction, models
from django.db.models import Q
from django.forms import inlineformset_factory
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from flask import json
from xhtml2pdf import pisa

from ClientApp.models import Client
from ProduitApp.forms import CadreForms
from ProduitApp.models import Categorie, ProduitBrut, Produit, AutreProduit
from VenteApp.forms import VenteForms, OrderItemFormset, ArticleForms, OrderCadreFormset, ArticleCadreForms, \
    OrderAutreFormset
from VenteApp.models import Commande, Article, ArticleCadre

"""
Affiche la page d'accueil de l'application VenteApp.

@param request: objet HttpRequest contenant la demande HTTP envoyée par le client.

@return un objet HttpResponse contenant la réponse HTTP envoyée au client avec la page d'accueil de l'application.
"""

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



def updateOrder(request, pk):
    """
    Update an existing order and associated articles in the database.

    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the order to update.

    Returns:
        HttpResponseRedirect: A redirection to the 'VenteApp:venteApp' view.

    Raises:
        N/A
    """
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
            print("boucle1")
            return redirect('VenteApp:venteApp')
        elif formset.is_valid() :
            form.save()
            formset.save()
            print("boucle2")
            return redirect('VenteApp:venteApp')
        elif cadre.is_valid() :
            form.save()
            cadre.save()
            print("boucle3")
            return redirect('VenteApp:venteApp')
    else:

        form = VenteForms(instance=order)
        formset = ItemFormset(instance=order)
        cadre = ItemCadre(instance=order)
        print("boucle4")

    return render(request, 'VenteApp/update_form.html', {'form':form, 'formset' : formset, 'cadre' : cadre})



def deleteOrder(request,pk):
    """
    Supprime une commande de la base de données.

    Args:
        request (HttpRequest): Requête HTTP envoyée au serveur.
        pk (int): Identifiant unique de la commande à supprimer.

    Returns:
        HttpResponse: Redirige vers la page principale de l'application VenteApp.

    Raises:
        Commande.DoesNotExist: Si la commande avec l'ID fourni n'existe pas dans la base de données.
    """
    order = Commande.objects.get(id=pk)
    if request.method == "POST" :
        order.delete()
        return redirect('VenteApp:venteApp')
    context = {'item':order}
    return render(request,'VenteApp/delete.html', context)

def searchBar(request):
    """
    Affiche la liste des commandes correspondantes à la recherche de nom ou prénom d'un client.

    Args:
        request (HttpRequest): Requête HTTP envoyée au serveur.

    Returns:
        HttpResponse: Renvoie un objet HTTP contenant la liste des commandes correspondantes ou un message d'erreur si aucun résultat n'est trouvé.
    """
    if request.method=='GET':
        query = request.GET.get('requete')
        if query:
            commandes = Commande.objects.filter(Q(client__prenom__icontains=query) | Q(client__nom__icontains=query))
            return render(request, 'VenteApp/searchbar.html', {'commandes':commandes})
        else:
            print("Aucun résultat")
            return request(request, 'VenteApp/searchbar.html', {})

def render_to_pdf(template,context_dict={}):
    """
    Convertit un template HTML en un document PDF.

    Args:
        template (str): Le nom du template à convertir en PDF.
        context_dict (dict): Un dictionnaire contenant les données à utiliser pour remplir le template.

    Returns:
        HttpResponse: Renvoie un objet HTTP contenant le document PDF ou None si une erreur se produit pendant la conversion.

    Raises:
        TypeError: Si le nom du template n'est pas une chaîne de caractères.
    """
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
    """
    Vue permettant d'afficher un document PDF généré à partir d'un template HTML.

    Attributes:
        None

    Methods:
        get(HttpRequest, *args, **kwargs): Affiche le document PDF généré en réponse à une requête HTTP GET.

    Raises:
        None
    """
    def get(self, request, *args, **kwargs):
        """
        Affiche le document PDF généré en réponse à une requête HTTP GET.

        Args:
            request (HttpRequest): Requête HTTP envoyée au serveur.
            *args: Arguments positionnels supplémentaires.
            **kwargs: Arguments nommés supplémentaires.

        Returns:
            HttpResponse: Renvoie un objet HTTP contenant le document PDF généré.

        Raises:
            None
        """
        pdf = render_to_pdf('VenteApp/pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

# Automaticly downloads to PDF file
class DownloadPDF(View):
    """
    Vue permettant de télécharger un document PDF généré à partir d'un template HTML.

    Attributes:
        None

    Methods:
        get(HttpRequest, *args, **kwargs): Télécharge le document PDF généré en réponse à une requête HTTP GET.

    Raises:
        None
    """
    def get(self, request, *args, **kwargs):
        """
        Télécharge le document PDF généré en réponse à une requête HTTP GET.

        Args:
            request (HttpRequest): Requête HTTP envoyée au serveur.
            *args: Arguments positionnels supplémentaires.
            **kwargs: Arguments nommés supplémentaires.

        Returns:
            HttpResponse: Renvoie un objet HTTP contenant le document PDF généré en tant que fichier à télécharger.

        Raises:
            None
        """
        pdf = render_to_pdf('VenteApp/pdf_template.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        content = 'attachment; filename="listeCommandes.pdf"'
        response['Content-Disposition'] = content
        return response


def deleteData(request):
    """
    Supprime un produit avec l'ID 8 de la base de données et redirige l'utilisateur vers la page de la liste des produits.

    Args:
        request (HttpRequest): Requête HTTP envoyée au serveur.

    Returns:
        HttpResponseRedirect: Redirige l'utilisateur vers la page de la liste des produits.

    Raises:
        None
    """
    produit = Produit.objects.get(id=8)
    produit.delete()
    return redirect('VenteApp:venteApp')


#VIEWS 2.0


class OrderList(ListView):
    """
    Affiche une liste de commandes triées par date de création décroissante.

    Attributes:
        template_name (str): Le nom du template utilisé pour afficher la liste de commandes.
        context_object_name (str): Le nom de l'objet de contexte utilisé dans le template pour accéder à la liste de commandes.

    Methods:
        get_queryset: Renvoie la liste des commandes triées par date de création décroissante.
    """
    template_name = 'VenteApp/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        """
        Renvoie la liste des commandes triées par date de création décroissante.

        Returns:
            QuerySet: La liste des commandes triées par date de création décroissante.
        """
        return Commande.objects.order_by('-date_creation')


class OrderDetail(DetailView):
    """
    Une vue basée sur des classes pour afficher les détails d'un seul objet Commande.
    """
    model = Commande
    """
    L'attribut "model" spécifie la classe de modèle (Commande) à laquelle la vue est associée. 
    La vue utilisera le modèle pour récupérer les détails de l'objet Commande et les afficher à l'utilisateur.
    """
    template_name = 'VenteApp/order_details.html'
    """
    L'attribut "template_name" spécifie le nom du fichier de modèle HTML qui sera utilisé pour afficher les détails de la commande. 
    Dans ce cas, il s'agit de 'VenteApp/order_details.html'.
    """

class OrderCreate(CreateView):
    """
    A class-based view for creating a new Order.

    Attributes
    ----------
    model : Commande
        The model to use for creating the order.
    fields : list of str
        The fields to include in the form for creating the order.
    template_name : str
        The name of the template to use for rendering the form.
    success_url : str
        The URL to redirect to after the form has been successfully submitted.

    Methods
    -------
    get_context_data(**kwargs)
        Returns the context data to be used when rendering the form.
    form_valid(form)
        Saves the order and its related items, cadre, and other products.
    """
    model = Commande
    fields = ['id', 'client','date_reception', 'statut']
    template_name = 'VenteApp/order_create.html'
    success_url = reverse_lazy('VenteApp:venteApp')

    def get_context_data(self, **kwargs):
        """
        Returns the context data to be used when rendering the form.

        Parameters
        ----------
        **kwargs : dict
            Keyword arguments to pass to the super method.

        Returns
        -------
        dict
            The context data for the form.
        """
        data = super(OrderCreate, self).get_context_data(**kwargs)

        if self.request.POST:
            data['items'] = OrderItemFormset(self.request.POST)
            data['cadre'] = OrderCadreFormset(self.request.POST)
            data['produit'] = OrderAutreFormset(self.request.POST)
        else:
            data['items'] = OrderItemFormset()
            data['cadre'] = OrderCadreFormset()
            data['produit'] = OrderAutreFormset()

        return data

    def form_valid(self, form):
        """
        Saves the order and its related items, cadre, and other products.

        Parameters
        ----------
        form : Form
            The form containing the data for the order.

        Returns
        -------
        HttpResponse
            A response indicating that the form was successfully submitted.
        """
        context = self.get_context_data()

        items = context['items']
        cadre = context['cadre']
        produit = context['produit']
        with transaction.atomic():
            self.object = form.save()

            if items.is_valid():
                items.instance = self.object
                items.save()

            if cadre.is_valid():
                cadre.instance = self.object
                cadre.save()

            if produit.is_valid():
                produit.instance = self.object
                produit.save()


        return super(OrderCreate, self).form_valid(form)




def ma_vue(request):
    """
    A view that returns a list of Commande objects sorted by a given attribute.

    Parameters
    ----------
    request : HttpRequest
        The request object for the view.

    Returns
    -------
    HttpResponse
        A response containing the sorted list of Commande objects.
    """
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





def total_qty(request, commande_id):
    """
    Récupère la quantité totale de produits commandés pour une commande donnée.

    Parameters:
        request (HttpRequest): Objet représentant la requête HTTP.
        commande_id (int): Identifiant de la commande à traiter.

    Returns:
        JsonResponse: Objet JsonResponse contenant la quantité totale de produits commandés pour la commande donnée.
    """
    commande = Commande.objects.get(id=commande_id)
    total_qty = commande.total_qty
    return JsonResponse({'total_qty': total_qty})

def createCadre(request):
    """
    Crée un cadre en utilisant un formulaire de type CadreForms.

    :param request: l'objet HttpRequest reçu par le serveur.
    :type request: HttpRequest object
    :return: la vue rendue avec un formulaire pour la création d'un cadre ou une redirection vers la page précédente si le formulaire est valide.
    :rtype: HttpResponse object
    """
    form = CadreForms()
    if request.method == 'POST':
        form= CadreForms(request.POST)
        if form.is_valid():
            form.save()
            print("la")
            return redirect(request.META.get('HTTP_REFERER'))
    return render(request, 'ProduitApp/create_cadre.html', {'form': form})


    """
    Récupère toutes les commandes passées par un client spécifique et les renvoie à un template de vue pour les afficher.
    
    @param request : objet HttpRequest envoyé par le client
    @param client_id : identifiant unique du client dont les commandes doivent être récupérées
    
    @return : objet HttpResponse avec le contenu HTML de la page affichant les commandes du client
    
    @throws Http404 si aucun client n'est trouvé avec l'identifiant spécifié
    """
def commandes_client(request, client_id):
    client = Client.objects.get(id=client_id)
    commandes = Commande.objects.filter(client=client)
    context = {'client': client, 'dataCommande': commandes}
    return render(request, 'VenteApp/commandes_client.html', context)