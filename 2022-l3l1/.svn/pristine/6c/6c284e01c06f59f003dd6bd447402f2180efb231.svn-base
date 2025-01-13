
from .models import Achat
from .forms import AchatForm,FactureForm


from FournisseursApp.models import Fournisseurs
from .forms import FactureForm
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import AchatForm, FactureForm
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from ProduitApp.models import ProduitBrut,AutreProduit
from decimal import Decimal
from AchatApp.models import AutreProduitLiaison,ProduitBrutLiaison

# On définit une vue qui renvoie la liste de tous les objets Achat en contexte
def index(request):
    # On récupère tous les objets Achat de la base de données
    achats = Achat.objects.all()
    # On renvoie une réponse HTTP contenant le contenu HTML de la page "achat.html" et la liste des achats en contexte
    return render(request, "achat.html", {"achats": achats})



# On définit une vue qui permet d'ajouter une facture à un achat pour un fournisseur donné
def ajouter_facture(request, fournisseur_id, achat_id):
    # On récupère le fournisseur et l'achat correspondants aux identifiants fournis dans l'URL
    fournisseur = Fournisseurs.objects.get(id=fournisseur_id)
    achat = Achat.objects.get(id=achat_id)

    if request.method == 'POST':  # Si la requête est une soumission de formulaire
        form = FactureForm(request.POST, request.FILES)  # On crée une instance de formulaire FactureForm à partir des données de la requête
        if form.is_valid():  # Si le formulaire est valide
            facture = form.save(commit=False)  # On crée une instance de modèle Facture à partir des données du formulaire
            facture.fournisseur = fournisseur  # On lie la facture au fournisseur correspondant
            facture.achat = achat  # On lie la facture à l'achat correspondant
            facture.save()  # On enregistre la facture dans la base de données
            messages.success(request, "La facture a été ajoutée avec succès!")  # On affiche un message de succès à l'utilisateur
            return redirect('achat')  # On redirige l'utilisateur vers la page d'affichage des achats
    else:
        form = FactureForm()  # On crée une instance vide de formulaire FactureForm

    # On renvoie une réponse HTTP contenant le contenu HTML de la page "ajout_facture.html", avec le formulaire et les fournisseur/achat correspondants passés en contexte
    return render(request, 'ajout_facture.html', {'form': form, 'fournisseur': fournisseur, 'achat': achat})




# On définit une vue de suppression pour les objets Achat
class AchatDeleteView(DeleteView):
    model = Achat  # On spécifie le modèle à utiliser (Achat)
    success_url = reverse_lazy('achat')  # On spécifie l'URL de redirection après la suppression (ici, la vue d'affichage des achats)
    template_name = 'supprimer_achat.html'  # On spécifie le nom du template HTML à utiliser pour afficher la confirmation de suppression


class AchatUpdateView(UpdateView):
    model = Achat
    form_class = AchatForm
    template_name = 'modifier_achat.html'
    success_url = reverse_lazy('achat')
    
    def form_valid(self, form):
        achat = form.save(commit=False)
        autres_produits = form.cleaned_data['autre_produits']
        produits_bruts=form.cleaned_data['produits_bruts']
        achat.save()

        # Traitement des produits supplémentaires
        if autres_produits:
            for autre_produit2 in autres_produits:
                quantite = self.request.POST.get(f'quantity_autre_produit_{autre_produit2.id}',0)
                prix2=self.request.POST.get(f'prix_{autre_produit2.id}',0)
                autre_produit2.prix_achat=prix2
                autre_produit2.quantite += Decimal(quantite)
                prix_total = float(quantite) * float(prix2)
                liaison = AutreProduitLiaison.objects.filter(achat=achat, autre_produit=autre_produit2).first()
                autre_produit2.quantite += Decimal(abs(Decimal(quantite)-Decimal((liaison.quantite))))
                autre_produit2.save()
                if liaison:
                    liaison.quantite,
                    liaison.prix_total=prix_total
                liaison.save()

        # Traitement des produits bruts
        if produits_bruts:
            for produit_brut2 in produits_bruts:
                quantite = self.request.POST.get(f'quantite_produit_brut_{produit_brut2.id}',0)
                quantitequintal = self.request.POST.get(f'quantite_quintal_produit_brut_{produit_brut2.id}',0)
                quantitebarre = self.request.POST.get(f'quantite_barre_produit_brut_{produit_brut2.id}',0)
                prixquintal=self.request.POST.get(f'prix_brut_{produit_brut2.id}',0)

                produit_brut2.save()
                prix_total = float(prixquintal)*float(quantitequintal)
                liaison = ProduitBrutLiaison.objects.filter(achat=achat,produit_brut=produit_brut2).first()
                produit_brut2.stock_quintal+=Decimal(abs(Decimal(quantitequintal)-Decimal(liaison.quantite_quintal)))
                produit_brut2.stock_barre+=Decimal(abs(Decimal(quantitebarre)-Decimal(liaison.quantite_bar)))
                produit_brut2.stock_metre+=Decimal(abs(Decimal(quantite)-Decimal(liaison.quantite_metre)))
                produit_brut2.prix_achat_quintal=prixquintal
                produit_brut2.save()
                liaison.quantite_quintal=quantitequintal
                liaison.quantite_bar=quantitebarre
                liaison.quantite_metre=quantite
                liaison.prix_total=prix_total
                liaison.save()

        response = super().form_valid(form)
        return response

    def get_context_data(self, **kwargs):
    # Appelle la méthode "get_context_data" de la super-classe et stocke le dictionnaire de contexte renvoyé dans la variable "context".
        context = super().get_context_data(**kwargs)

        # Récupère tous les objets de la classe "AutreProduit" et les stocke dans la variable "Autre_produits".
        Autre_produits = AutreProduit.objects.all()

        # Récupère tous les objets de la classe "ProduitBrut" et les stocke dans la variable "Produits_brut".
        Produits_brut=ProduitBrut.objects.all()

        # Initialise un dictionnaire vide "quantites" qui sera utilisé pour stocker les quantités de chaque "autre produit".
        quantites = {}

        # Pour chaque "autre produit" dans "Autre_produits", on récupère la liaison entre cet "autre produit" et l'achat en cours ("self.object").
        # Si la liaison existe, on stocke la quantité associée dans le dictionnaire "quantites".
        # Sinon, on initialise la quantité à zéro.
        for autre_produit in Autre_produits:
            liaison = AutreProduitLiaison.objects.filter(achat=self.object, autre_produit=autre_produit).first()
            if liaison is not None:
                quantites[autre_produit.pk] = liaison.quantite
            else:
                quantites[autre_produit.pk] = 0

        # Initialise trois dictionnaires vides "quantites_brut", "quantites_quintal" et "quantites_bar" qui seront utilisés pour stocker les quantités de chaque "produit brut".
        # Pour chaque "produit brut" dans "Produits_brut", on récupère la liaison entre ce "produit brut" et l'achat en cours ("self.object").
        # Si la liaison existe, on stocke les quantités associées dans les dictionnaires "quantites_brut", "quantites_quintal" et "quantites_bar".
        # Sinon, on initialise les quantités à zéro.
            quantites_brut={}
            for produit_brut in Produits_brut:
                liaison=ProduitBrutLiaison.objects.filter(achat=self.object,produit_brut=produit_brut).first()
                if liaison is not None:
                    quantites_brut[produit_brut.pk]=liaison.quantite_metre
                else:
                    quantites_brut[produit_brut.pk]=0
            quantites_quintal={}
            for produit_brut in Produits_brut:
                liaison=ProduitBrutLiaison.objects.filter(achat=self.object,produit_brut=produit_brut).first()
                if liaison is not None:
                    quantites_quintal[produit_brut.pk]=liaison.quantite_quintal
                else:
                    quantites_quintal[produit_brut.pk]=0
            quantites_bar={}
            for produit_brut in Produits_brut:
                liaison=ProduitBrutLiaison.objects.filter(achat=self.object,produit_brut=produit_brut).first()
                if liaison is not None:
                    quantites_bar[produit_brut.pk]=liaison.quantite_bar
                else:
                    quantites_bar[produit_brut.pk]=0

            # Ajoute 
            context['autre_produits'] = AutreProduit.objects.filter(achat=self.object)
            context["Autre_produits"]=Autre_produits
            context['produits_bruts'] = ProduitBrut.objects.filter(achat=self.object)
            context["Produits_brut"]=Produits_brut
            context['quantites'] = quantites
            context['quantites_brut'] = quantites_brut
            context['quantites_quintal'] = quantites_quintal
            context['quantites_bar'] = quantites_bar

            return context
# views.py


# On importe les modèles nécessaires
from .models import AutreProduit, ProduitBrut
from .forms import AchatForm

# On définit la vue qui permet d'ajouter des produits
def ajouter_produits(request):
    
    # On récupère tous les autres produits, produits bruts 
    autre_produits = AutreProduit.objects.all()
    produits_brut=ProduitBrut.objects.all()
    

    # Si la requête est une requête POST
    if request.method == 'POST':
        
        # On récupère les données du formulaire
        form = AchatForm(request.POST, request.FILES)
        
        # Si le formulaire est valide
        if form.is_valid():
            
            # On crée un objet achat à partir des données du formulaire
            achat = form.save(commit=False)
            
            # On récupère les autres produits et produits bruts sélectionnés dans le formulaire
            autres_produits = form.cleaned_data['autre_produits']
            produits_bruts=form.cleaned_data['produits_bruts']

            # On sauvegarde l'objet achat
            achat.save()

            # Si des autres produits ont été sélectionnés
            if autres_produits:
                
                # Pour chaque autre produit sélectionné
                for autre_produit2 in autres_produits:
                    
                    # On récupère la quantité et le prix associés à cet autre produit
                    quantite = request.POST.get(f'quantity_autre_produit_{autre_produit2.id}',0)
                    prix2=request.POST.get(f'prix_{autre_produit2.id}',0)
                    
                    # On met à jour les informations de l'autre produit
                    autre_produit2.prix_achat=prix2
                    autre_produit2.quantite += int(quantite)
                    autre_produit2.save()
                    
                    # On calcule le prix total de l'achat pour cet autre produit
                    prix_total = float(quantite) * float(prix2)
                    
                    # On crée une liaison entre l'autre produit et l'achat avec les informations associées
                    liaison = AutreProduitLiaison(
                        autre_produit=autre_produit2,
                        achat=achat,
                        quantite=quantite,
                        prix_total=prix_total
                    )
                    
                    # On sauvegarde la liaison
                    liaison.save()

            # Si des produits bruts ont été sélectionnés   
            if produits_bruts:    
                
                # Pour chaque produit brut sélectionné
                for produit_brut2 in produits_bruts:
                    
                    # On récupère la quantité en mètre, en quintal et en barre associée à ce produit brut, ainsi que le prix d'achat au quintal
                    quantite = request.POST.get(f'quantite_produit_brut_{produit_brut2.id}',0)
                    quantitequintal = request.POST.get(f'quantite_quintal_produit_brut_{produit_brut2.id}',0)
                    quantitebarre = request.POST.get(f'quantite_barre_produit_brut_{produit_brut2.id}',0)
                    prixquintal=request.POST.get(f'prix_brut_{produit_brut2.id}',0)

                    # On met à jour les informations du produit brut
                    produit_brut2.stock_quintal+=Decimal(quantitequintal)
                    produit_brut2.stock_barre+=Decimal(quantitebarre)
                    produit_brut2.stock_metre+=Decimal(quantite)
                    produit_brut2.prix_achat_quintal=prixquintal
                    
                    
                    produit_brut2.save()
                    prix_total = float(prixquintal)*float(quantitequintal)
                    liaison = ProduitBrutLiaison(
                        produit_brut=produit_brut2,
                        achat=achat,
                        quantite_quintal=quantitequintal,
                        quantite_bar=quantitebarre,
                        quantite_metre=quantite,
                        prix_total=prix_total
    )
                
                    liaison.save()
            
            
            messages.success(request, "L'achat a été ajouté avec succès!")
            return redirect('achat')
    else:
        form = AchatForm()
    
    context = {'form': form, 'autre_produits': autre_produits,'produits_bruts':produits_brut}
    return render(request, 'ajouter_produits.html', context)
