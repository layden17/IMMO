from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.template import loader

from .forms import ProduitBrutForm, CadreForms, AutreProduitForm


# Create your views here.

from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .models import ProduitBrut, Produit, Categorie, Cadre, AutreProduit, CategorieFer,HistoriquePrixAchatQuintal
from .forms import CategorieForm, CadreForms

def index(request):
    """
    Vue qui retourne la page d'accueil du site.

    Arguments:
    - request: l'objet HttpRequest envoyé par le navigateur

    Returns:
    - HttpResponse : la réponse HTTP avec la page HTML demandée (produit_base.html)
    """
    return render(request, 'ProduitApp/produit_base.html')


"""
view pour afficher les autres produits 
"""
def autre_produit(request):
    """
    Vue pour afficher tous les autres produits dans le modèle AutreProduit
    et les afficher dans un template HTML approprié.

    Arguments:
    - request: objet HttpRequest contenant les détails de la requête HTTP entrante.

    Renvoie:
    - HttpResponse: réponse HTTP renvoyée à l'utilisateur, contenant le contenu HTML
                    généré dynamiquement pour afficher tous les autres produits dans le modèle AutreProduit.
"""
    autre_produit = AutreProduit.objects.all()
    return render(request, 'ProduitApp/autre_produit.html',
                            {'autres_produits': autre_produit})




"""
view pour afficher les produits brut (barre de fer)
"""
def produit_brut(request):
    """
    Renvoie la page de liste des produits bruts.

    Args:
        request: La requête HTTP envoyée par le client.

    Returns:
        La réponse HTTP avec la page de liste des produits bruts rendue à l'aide d'un template.
        Le contexte contient la liste de tous les produits bruts stockés dans la base de données.
    """
    produits_bruts = ProduitBrut.objects.all()
    return render(request, 'ProduitApp/produits_bruts.html',
                            {'produits_bruts': produits_bruts})

"""
view pour afficher les cadres 
"""
def cadre(request):
    """
    Vue qui affiche la liste des cadres.

    Args:
        request: la requête HTTP reçue.

    Returns:
        Un objet HttpResponse contenant le rendu HTML de la page d'affichage des cadres.

    """
    cadres = Cadre.objects.all()

    return render(request, 'ProduitApp/cadres.html', {'cadres': cadres})




def categories(request):
    """
    Cette fonction prend une requête HTTP en entrée et récupère toutes les catégories depuis la base de données.
    Elle retourne ensuite une réponse HTTP qui affiche toutes les catégories dans un template appelé 'ProduitApp/categorie.html'.

    Arguments:
    - request: requête HTTP

    Retour:
    - HTTP response : réponse HTTP qui affiche toutes les catégories

    """
    categories= Categorie.objects.all()
    return render(request, 'ProduitApp/categorie.html', 
                  {'categories': categories})


def createCadre(request):
    """
    Cette fonction permet de créer un nouveau cadre en utilisant un formulaire.

    Args:
    - request: une requête HTTP.

    Returns:
    - Une page HTML affichant un formulaire pour la création d'un nouveau cadre.
    - Si les données soumises dans le formulaire sont valides, la fonction crée un nouveau cadre et redirige l'utilisateur vers la page d'accueil des cadres.
    """
    form = CadreForms()
    if request.method == 'POST':
        form= CadreForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cadre/')
    return render(request, 'ProduitApp/create_cadre.html', {'form': form})




def supprimer_cadre(request, id):
    """
    Supprime un objet Cadre spécifié par son ID de la base de données.

    :param request: Objet HttpRequest contenant les données de la requête.
    :type request: django.http.HttpRequest
    :param id: ID de l'objet Cadre à supprimer.
    :type id: int
    :return: Redirige l'utilisateur vers la page '/cadre/'.
    :rtype: django.http.HttpResponseRedirect
    """
    cadre = Cadre.objects.get(id=id)
    cadre.delete()
    return redirect('/cadre/')



class modifier_cadre(UpdateView):
    """
    Classe basée sur UpdateView qui permet la modification d'un objet Cadre existant.

    :ivar model: Classe du modèle à utiliser pour la vue (obligatoire).
    :vartype model: django.db.models.Model
    :ivar form_class: Classe du formulaire à utiliser pour la vue (obligatoire).
    :vartype form_class: django.forms.ModelForm
    :ivar template_name: Nom du modèle à utiliser pour le rendu de la vue.
    :vartype template_name: str
    """
    model = Cadre
    form_class = CadreForms
    template_name = 'ProduitApp/modifier_cadre.html'
    def form_valid(self, form):
        """
        Méthode appelée lorsque le formulaire de modification d'un objet Cadre est valide.

        :param form: Formulaire validé avec les données de la requête.
        :type form: django.forms.ModelForm
        :return: Redirige l'utilisateur vers la page '/cadre/'.
        :rtype: django.http.HttpResponseRedirect
        """
        form.save()
        return redirect('/cadre/')



def tri_cadre(request, tri):
    if tri == 'Cadre_choix':
        # Si le paramètre 'tri' est égal à 'Cadre_choix'
        # Alors, trier les objets 'Cadre' par l'attribut 'cadre_choix'
        cadre = Cadre.objects.order_by('cadre_choix')

    elif tri == 'Article_choix':
        # Sinon, si le paramètre 'tri' est égal à 'Article_choix'
        # Alors, trier les objets 'Cadre' par l'attribut 'article_choix'
        cadre = Cadre.objects.order_by('article_choix')

    elif tri == 'prix_metre':
        # Sinon, si le paramètre 'tri' est égal à 'prix_metre'
        # Alors, trier les objets 'Cadre' par l'attribut 'prix_metre'
        cadre = Cadre.objects.order_by('prix_metre')

    elif tri == 'longueur':
        # Sinon, si le paramètre 'tri' est égal à 'longueur'
        # Alors, trier les objets 'Cadre' par l'attribut 'longueur'
        cadre = Cadre.objects.order_by('longueur')

    elif tri == 'largeur':
        # Sinon, si le paramètre 'tri' est égal à 'largeur'
        # Alors, trier les objets 'Cadre' par l'attribut 'largeur'
        cadre = Cadre.objects.order_by('largeur')

    elif tri == 'crochet':
        # Sinon, si le paramètre 'tri' est égal à 'crochet'
        # Alors, trier les objets 'Cadre' par l'attribut 'crochet'
        cadre = Cadre.objects.order_by('crochet')

    elif tri == 'prix_service':
        # Sinon, si le paramètre 'tri' est égal à 'prix_service'
        # Alors, trier les objets 'Cadre' par l'attribut 'prix_service'
        cadre = Cadre.objects.order_by('prix_service')

    elif tri == 'chute':
        # Sinon, si le paramètre 'tri' est égal à 'chute'
        # Alors, trier les objets 'Cadre' par l'attribut 'chute'
        cadre = Cadre.objects.order_by('chute')

    elif tri == 'consommation_sans_chute':
        # Sinon, si le paramètre 'tri' est égal à 'consommation_sans_chute'
        # Alors, trier les objets 'Cadre' par l'attribut 'consommation_sans_chute'
        cadre = Cadre.objects.order_by('consommation_sans_chute')

    elif tri == 'consommation':
        # Sinon, si le paramètre 'tri' est égal à 'consommation'
        # Alors, trier les objets 'Cadre' par l'attribut 'consommation'
        cadre = Cadre.objects.order_by('consommation')

    elif tri == 'crochet_opti':
        # Sinon, si le paramètre 'tri' est égal à 'crochet_opti'
        # Alors, trier les objets 'Cadre' par l'attribut 'crochet_opti'
        cadre = Cadre.objects.order_by('crochet_opti')

    elif tri == 'chute_valeur':
        # Sinon, si le paramètre 'tri' est égal à 'chute_valeur'
        # Alors, trier les objets 'Cadre' par l'attribut 'chute_valeur'
        cadre = Cadre.objects.order_by('chute_valeur')

    elif tri == 'max':
        # Sinon, si le paramètre 'tri' est égal à 'max'
        # Alors, trier les objets 'Cadre' par l'attribut 'max'
        cadre = Cadre.objects.order_by('max')

    elif tri == 'prix':
        # Sinon, si le paramètre 'tri' est égal à 'prix'
        # Alors, trier les objets 'Cadre' par l'attribut 'prix'
        cadre = Cadre.objects.order_by('prix')

    else:
        # Sinon, si le paramètre 'tri' n'est pas égal à un des choix ci-dessus
        # Alors, renvoyer tous les objets 'Cadre' non triés
        cadre = Cadre.objects.all()
    return render(request, 'ProduitApp/cadres.html', {'cadres': cadre})


def categorie(request):
    """
    Affiche une liste de toutes les catégories d'objets de produit à l'exception de 'produit brut' et 'cadre'.

    :param request: Objet HttpRequest contenant les données de la requête.
    :type request: django.http.HttpRequest
    :return: HttpResponse contenant la page de liste des catégories d'objets de produit.
    :rtype: django.http.HttpResponse
    """
    categories = Categorie.objects.exclude(name__in=['produit brut', 'cadre'])
    context = {
        'categories': categories,
    }
    return render(request, 'ProduitApp/categorie.html', context)


def create_category(request):
    """
    Affiche un formulaire de création de catégorie pour les objets de produit et crée une nouvelle catégorie lorsqu'il est soumis.

    :param request: Objet HttpRequest contenant les données de la requête.
    :type request: django.http.HttpRequest
    :return: Redirige l'utilisateur vers la page '/categorie/' après la création d'une nouvelle catégorie, ou affiche un formulaire de création de catégorie.
    :rtype: django.http.HttpResponseRedirect ou django.http.HttpResponse
    """
    form = CategorieForm
    categories=Categorie.objects.all()

    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            categorie = Categorie(name=form.cleaned_data['name'])
            categorie.save()
            return HttpResponseRedirect('/categorie/')
    else:
        form = CategorieForm
    return render(request, 'ProduitApp/create_categorie.html', {'form': form,
                  'categories':categories})




class supprimer_categorie(DeleteView):
    """
    Affiche une page de confirmation pour supprimer une catégorie d'objet de produit existante et supprime la catégorie lorsqu'elle est confirmée.

    :ivar model: Modèle de la classe de la catégorie d'objet de produit.
    :vartype model: django.db.models.Model
    :ivar template_name: Nom du modèle de template à utiliser pour la vue.
    :vartype template_name: str
    :ivar success_url: URL de redirection après la suppression de la catégorie d'objet de produit.
    :vartype success_url: str
    """
    model=Categorie
    template_name='ProduitApp/supprimer_categorie.html'
    success_url = reverse_lazy('ProduitApp:categorie')



class modifier_categorie(UpdateView):
    """
    Affiche un formulaire de modification pour une catégorie d'objet de produit existante et met à jour la catégorie lorsqu'elle est soumise.

    :ivar model: Modèle de la classe de la catégorie d'objet de produit.
    :vartype model: django.db.models.Model
    :ivar form_class: Classe de formulaire à utiliser pour la vue.
    :vartype form_class: type
    :ivar template_name: Nom du modèle de template à utiliser pour la vue.
    :vartype template_name: str
    :ivar success_url: URL de redirection après la mise à jour de la catégorie d'objet de produit.
    :vartype success_url: str
    """
    model = Categorie
    form_class = CategorieForm
    template_name = 'ProduitApp/modifier_categorie.html'
    success_url = reverse_lazy('ProduitApp:categorie')




def add_produit_brut(request):
    form = ProduitBrutForm()
    if request.method == 'POST':
        form = ProduitBrutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/produit_brut/')
    else:
        form = ProduitBrutForm()

    context = {'form': form}
    return render(request, 'ProduitApp/add_produit_brut.html', context)


def add_autre_produit(request):
    """
    Affiche un formulaire pour ajouter un nouveau produit brut et l'ajoute à la base de données lorsqu'il est soumis.

    :param request: La requête HTTP envoyée au serveur.
    :type request: django.http.HttpRequest
    :return: Le template HTML pour ajouter un nouveau produit brut, ou une redirection vers la liste des produits bruts.
    :rtype: django.http.HttpResponse
    """
    form = AutreProduitForm()
    if request.method == 'POST':
        form = AutreProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/autre_produit/')
    else:
        form = AutreProduitForm()

    context = {'form': form}
    return render(request, 'ProduitApp/add_autre_produit.html', context)


class produit_detail(DetailView):
    """
    Affiche les détails d'un produit brut existant.

    :ivar model: Modèle de la classe de produit brut.
    :vartype model: django.db.models.Model
    :ivar template_name: Nom du modèle de template à utiliser pour la vue.
    :vartype template_name: str
    """
    model = ProduitBrut
    template_name = 'ProduitApp/produit_detail.html'


class autre_produit_detail(DetailView):
    """
    Affiche les détails d'un autre produit existant.

    :ivar model: Modèle de la classe d'autre produit.
    :vartype model: django.db.models.Model
    :ivar template_name: Nom du modèle de template à utiliser pour la vue.
    :vartype template_name: str
    """
    model = AutreProduit
    template_name = 'ProduitApp/autre_produit_detail.html'


class modifier_produit(UpdateView):
    """
    Une vue basée sur une classe Django pour modifier un objet `ProduitBrut` dans la base de données.

    Attributes:
        model (Model): Le modèle de la base de données sur lequel la vue opère.
        form_class (Form): La classe de formulaire à utiliser pour la modification de l'objet.
        template_name (str): Le nom du template à utiliser pour afficher la vue.

    Methods:
        get_success_url(): Renvoie l'URL de redirection après une modification réussie.
        form_valid(form): Enregistre les modifications apportées au formulaire et à l'objet dans la base de données.
    """
    model = ProduitBrut
    form_class = ProduitBrutForm
    template_name = 'ProduitApp/modifier_produit.html'

    def get_success_url(self) :
        return reverse_lazy("ProduitApp:produit_detail",kwargs={'pk':self.object.id})

    def form_valid(self, form):
        # Récupérer le produit et le nouveau prix d'achat quintal
        produit = form.save(commit=False)
        nouveau_prix_achat_quintal = form.cleaned_data['prix_achat_quintal']

        # Vérifier si le prix a changé depuis la dernière modification
        dernier_historique = HistoriquePrixAchatQuintal.objects.filter(produit=produit).order_by('-date').first()
        if dernier_historique is None or dernier_historique.prix != nouveau_prix_achat_quintal:
            # Enregistrer un nouvel historique
            historique = HistoriquePrixAchatQuintal(produit=produit, prix=nouveau_prix_achat_quintal)
            historique.save()

        # Enregistrer les modifications sur le produit
        produit.save()
        return super().form_valid(form)


def historique_prix_achat_quintal(request,pk):
   # historique_prix_achat_quintal = HistoriquePrixAchatQuintal.objects.all()
    historique_prix_achat_quintal = HistoriquePrixAchatQuintal.objects.filter(produit__id=pk)
    return render(request, 'ProduitApp/histo_pa_quintal.html',
                   {'historique_prix_achat_quintal': historique_prix_achat_quintal})









class modifier_autre_produit(UpdateView):
    model = AutreProduit
    form_class = AutreProduitForm
    template_name = 'ProduitApp/modifier_autre_produit.html'

    def get_success_url(self) :
        return reverse_lazy("ProduitApp:autre_produit_detail",kwargs={'pk':self.object.id})



class supprimer_produit_brut(DeleteView):
    model=ProduitBrut
    template_name='ProduitApp/supprimer_produit_brut.html'
    success_url = reverse_lazy('ProduitApp:produit_brut')



class supprimer_autre_produit(DeleteView):
    model=AutreProduit
    template_name='ProduitApp/supprimer_autre_produit.html'
    success_url = reverse_lazy('ProduitApp:autre_produit')



