from django.shortcuts import render
from ProduitApp.models import ProduitBrut, Produit, Categorie, Cadre, AutreProduit, CategorieFer,HistoriquePrixAchatQuintal
from FournisseursApp.models import Fournisseurs
from ClientApp.models import Client
from AchatApp.models import Achat
from django.db.models import Count,Sum



# Create your views here.


def statistique(request):
    return render(request, "StatApp/statistique.html")




def all_stat(request):
    # Top 5 des cadres par prix
    labels1 = []
    data1 = []
    queryset1 = Cadre.objects.order_by('-prix')[:5]
    for cadre in queryset1:
        labels1.append(cadre.cadre_choix)
        data1.append(cadre.prix)

    #nombre de cadre
    nb_cadre = Cadre.objects.count()

    # Consommation total des cadres
    consommation_total = Cadre.objects.aggregate(Sum('consommation_sans_chute'))['consommation_sans_chute__sum']

    # Prix total des cadres
    prix_total_cadre = Cadre.objects.aggregate(Sum('prix'))['prix__sum']

    # Prix service total des cadres confectionnés
    prix_service_total= Cadre.objects.aggregate(Sum('prix_service'))['prix_service__sum']

    # nombre de fournisseur
    nb_fournisseur = Fournisseurs.objects.count()

    # nombre de client
    nb_client = Client.objects.count()
    # Prix total des achats
    prix_total_achat = Achat.objects.aggregate(Sum('prix_total'))['prix_total__sum']


    return render(request, 'StatApp/statistique.html', {
        'labels1': labels1,
        'data1': data1,
        'nb_cadre':nb_cadre,
        'consommation_total': consommation_total,
        'prix_total_cadre': prix_total_cadre,
        'prix_service_total':prix_service_total,
        'nb_fournisseur':nb_fournisseur,
        'nb_client':nb_client,
        'prix_total_achat': prix_total_achat,
    })


