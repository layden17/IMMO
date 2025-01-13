from io import BytesIO

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

from ClientApp.forms import ClientForms
from ClientApp.models import Client
from ProduitApp.models import Produit
from VenteApp.models import Commande






def index(request):

    """
    Vue qui gère la page d'accueil.

    Cette vue affiche le formulaire d'ajout de client et les statistiques
    générales de l'application.

    Si le formulaire est validé (via une requête POST), un nouveau client
    est ajouté à la base de données.

    Le contexte contient les variables suivantes :
    - form : le formulaire pour ajouter un client
    - dataClient : tous les clients dans la base de données
    - product : le nombre total de produits dans la base de données
    - customer : le nombre total de clients dans la base de données
    - order : le nombre total de commandes dans la base de données
    """

    form = ClientForms()

    total_produit = Produit.objects.count()
    total_client = Client.objects.count()
    total_oder = Commande.objects.count()

    if request.method == 'POST':
        form = ClientForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clientApp')

    context = {
        'form': form,
        'dataClient': Client.objects.all(),
        'product': total_produit,
        'customer': total_client,
        'order': total_oder,

    }
    return render(request, "ClientApp/index.html", context)



def createCustomer(request):
    """
    Vue qui gère la création d'un nouveau client.

    Affiche un formulaire permettant de créer un nouveau client.
    Si le formulaire est validé (via une requête POST), un nouveau client est
    ajouté à la base de données.

    Le contexte contient les variables suivantes :
    - form : le formulaire pour créer un nouveau client
    """

    form = ClientForms()

    if request.method == 'POST':
        form = ClientForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ClientApp:clientApp')

    context = {'form' : form}
    return render(request, 'ClientApp/customer_form.html', context)


def updateCustomer(request, pk):
    """
    Vue qui gère la mise à jour d'un client existant.

    Affiche un formulaire prérempli avec les informations d'un client
    existant permettant de modifier ses données. Si le formulaire est validé
    (via une requête POST), les informations du client sont mises à jour dans
    la base de données.

    Le contexte contient les variables suivantes :
    - form : le formulaire prérempli pour modifier les données du client
    """

    order = Client.objects.get(id=pk)
    form = ClientForms(instance=order)

    if request.method == 'POST':
        form = ClientForms(request.POST,request.FILES,instance=order)
        if form.is_valid():
            form.save()
            return redirect('ClientApp:clientApp')
    context = {'form': form}
    return render(request, 'ClientApp/customer_form.html', context)


def deleteCustomer(request,pk):
    """
    Cette fonction supprime un objet de la classe Client en utilisant son ID (pk).

    Arguments:
        request: objet HttpRequest
        pk : entier, identifiant de l'objet Client à supprimer.

    Returns:
        redirige l'utilisateur vers la vue 'clientApp' si la méthode HTTP est 'POST'.
        Affiche un message de confirmation de suppression de l'objet 'order' s'il est appelé avec la méthode HTTP 'GET'.
    """
    order = Client.objects.get(id=pk)
    if request.method == "POST" :
        order.delete()
        return redirect('ClientApp:clientApp')
    context = {'item':order}
    return render(request,'ClientApp/delete.html', context)


def searchBar(request):
    """
    Cette fonction permet de rechercher les clients dont le prénom contient
    une chaîne de caractères donnée via une barre de recherche.

    Arguments:
        request: objet HttpRequest

    Returns:
        Renvoie un objet HttpResponse qui affiche les résultats de la recherche
        si la méthode HTTP est 'GET', sinon une erreur 404.
    """

    if request.method=='GET':
        query = request.GET.get('requete')
        if query:
            clients = Client.objects.filter(prenom__icontains=query)
            return render(request, 'ClientApp/searchbar.html', {'clients':clients})
        else:
            print("Aucun résultat")
            return request(request, 'ClientApp/searchbar.html', {})

def render_to_pdf(template, context_dict):
        
        """
        Cette fonction prend en entrée un template et un dictionnaire de contexte,
        et renvoie un fichier PDF généré à partir du template et du contexte fourni.

        Arguments:
            template (str): Le nom du template à utiliser pour générer le PDF.
            context_dict (dict): Un dictionnaire de contexte contenant les données à utiliser dans le template.

        Returns:
            HttpResponse: Un objet HttpResponse contenant le fichier PDF généré.

        """
        dataClients = Client.objects.all()
        context = {'dataCommande': dataClients}
        template = get_template(template)
        html = template.render(context)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO_8859-1")), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None

data = {
            "company": "Gestion commercial",
            "address": "Adresse de l'entreprise",
            "city": "Ville",
            "state": "Pays",
            "zipcode": "Code postal",

            "phone": "00 00 00 00 00",
            "email": "email@gmail.com",
        }



# Opens up page as PDF

class ViewPDF(View):
        
        """
        Méthode GET qui génère un fichier PDF à partir d'un template HTML.

        Arguments:
            request: La requête HTTP envoyée par le client.
            args: Arguments non nommés.
            kwargs: Arguments nommés.

        Returns:
            Une réponse HTTP contenant le fichier PDF.
        """
        def get(self, request, *args, **kwargs):
            pdf = render_to_pdf('ClientApp/pdf_template.html', data)
            return HttpResponse(pdf, content_type='application/pdf')



# Automaticly downloads to PDF file
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('ClientApp/pdf_template.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "listeClients_%s.pdf" % ("12341231")
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response





def creerArticle(request):
    """
    Cette fonction permet de créer un nouvel article/client en utilisant un formulaire 'ClientForms'.

    Parameters:
    ----------
    request : HttpRequest
        L'objet request de Django représentant la requête HTTP.

    Returns:
    -------
    HttpResponse
        La réponse HTTP de la vue.
    """

    form = ClientForms()

    if request.method == 'POST':
        form = ClientForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ClientApp:clientApp')

    context = {'form' : form}
    return render(request, 'ClientApp/customer_form.html', context)