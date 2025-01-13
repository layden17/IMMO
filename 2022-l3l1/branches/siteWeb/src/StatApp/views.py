from django.shortcuts import render
from ProduitApp.models import ProduitBrut, Produit, Categorie, Cadre, AutreProduit, CategorieFer,HistoriquePrixAchatQuintal
from FournisseursApp.models import Fournisseurs
from ClientApp.models import Client
from AchatApp.models import Achat
from StatApp.forms import DateForm
from VenteApp.models import Article, Commande, ArticleAutre, ArticleCadre
from django.db.models import Count,Sum



# Create your views here.


def statistique(request):
    return render(request, "StatApp/statistique.html")



def all_stat(request):
    # Informations produits
    nb_categorie = Categorie.objects.count()
    nb_produit = Produit.objects.count()
    nb_autre_produit = AutreProduit.objects.count()


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



    # Total de vente
    prix_total_vente = 0
    #total prix de toutes les commandes
    for commande in Commande.objects.all():
        articles_brut = commande.article_set.all()
        prix_article = sum(article.price for article in articles_brut)

        articles_cadre = commande.articlecadre_set.all()
        prix_cadre = sum(article.price for article in articles_cadre)

        articles_autre = commande.articleautre_set.all()
        prix_autre_produit = sum(article.price for article in articles_autre)
        prix_total_vente += prix_article + prix_autre_produit +prix_cadre


    # Total de dette client
    dette_client = Client.objects.aggregate(Sum('dette'))['dette__sum']
    # Total de dette fournisseur
    dette_fournisseur = Fournisseurs.objects.aggregate(Sum('Dette'))['Dette__sum']

    # nombre de fournisseur
    nb_fournisseur = Fournisseurs.objects.count()

    # nombre de client
    nb_client = Client.objects.count()
    # dette de client
    nb_dette = Client.objects.aggregate(Sum('dette'))['dette__sum']
    # Top 5 dette de client
    labels3 = []
    data3 = []
    queryset3 = Client.objects.order_by('-dette')[:5]
    for client in queryset3:
        labels3.append(client.prenom)
        data3.append(client.dette)


    # Prix total des achats
    prix_total_achat = Achat.objects.aggregate(Sum('prix_total'))['prix_total__sum']

    # Top 5 des fournisseurs par nombre d'achats

    #labels8= []
    #data8 = []
    #queryset = Achat.objects.values('fournisseur__nom').annotate(total_achats=Count('id')).order_by('-total_achats')[:5]
    #for fournisseur in queryset:
    #    labels8.append(fournisseur['fournisseur__nom'])
    #    data8.append(fournisseur['total_achats'])

    # Quantité des articles de la commande

    '''
    # tous les cadres pour chaque commande
    labels9 = []
    data9 = []
    commandes = Commande.objects.all()
    quantite_totale = commandes.aggregate(total_quantite=Sum('articlecadre__quantite'))
    labels9.append('Total')
    data9.append(quantite_totale['total_quantite'])
    for commande in commandes:
        articles = commande.articlecadre_set.all()
        for article in articles:
            labels9.append(str(article.cadre))
            data9.append(article.quantite)
    
    '''

    #regroupe chaque cadre de chaque commande
    labels9 = []
    data9 = []
    cadre_quantites = {}

    commandes = Commande.objects.all()
    quantite_totale = commandes.aggregate(total_quantite=Sum('articlecadre__quantite'))
    labels9.append('Total')
    data9.append(quantite_totale['total_quantite'])

    for commande in commandes:
        articles = commande.articlecadre_set.all()
        for article in articles:
            cadre_nom = str(article.cadre)
            if cadre_nom not in cadre_quantites:
                cadre_quantites[cadre_nom] = article.quantite
            else:
                cadre_quantites[cadre_nom] += article.quantite

    for cadre_nom, quantite in cadre_quantites.items():
        labels9.append(cadre_nom)
        data9.append(quantite)




    '''
    #tous les articles bruts pour chaque commande
    labels10 = []
    data10 = []
    commandes = Commande.objects.all()
    quantite_totale = commandes.aggregate(total_quantite=Sum('article__quantite'))
    labels10.append('Total')
    data10.append(quantite_totale['total_quantite'])
    for commande in commandes:
        articles = commande.article_set.all()

        for article in articles:
            labels10.append(str(article.produit))
            data10.append(article.quantite)
    '''

    # tous les articles bruts pour chaque commande
    labels10 = []
    data10 = []
    produit_quantites = {}

    commandes = Commande.objects.all()
    quantite_totale = commandes.aggregate(total_quantite=Sum('article__quantite'))
    labels10.append('Total')
    data10.append(quantite_totale['total_quantite'])

    for commande in commandes:
        articles = commande.article_set.all()
        for article in articles:
            produit_nom = str(article.produit)
            if produit_nom not in produit_quantites:
                produit_quantites[produit_nom] = article.quantite
            else:
                produit_quantites[produit_nom] += article.quantite

    for produit_nom, quantite in produit_quantites.items():
        labels10.append(produit_nom)
        data10.append(quantite)

    #Top 5 autre produit
    labels11 = []
    data11 = []
    autre_produit_quantites = {}

    commandes = Commande.objects.all()

    for commande in commandes:
        articles = commande.articleautre_set.all()
        for article in articles:
            autre_produit_nom = str(article.produit)
            if autre_produit_nom not in autre_produit_quantites and autre_produit_nom != 'AutreProduit':
                autre_produit_quantites[autre_produit_nom] = article.quantite
            elif autre_produit_nom != 'AutreProduit':
                autre_produit_quantites[autre_produit_nom] += article.quantite

    top_5_produits = sorted(autre_produit_quantites.items(), key=lambda x: x[1], reverse=True)[:5]

    for produit, quantite in top_5_produits:
        labels11.append(produit)
        data11.append(quantite)


    """
        date_form = DateForm(request.GET or None)
    if date_form.is_valid():
        date = date_form.cleaned_data['date']
        start_date = date_form.cleaned_data['start_date']
        end_date = date_form.cleaned_data['end_date']
        commandes = Commande.objects.filter(date_creation__date=date, date_creation__range=(start_date, end_date))
        prix_total_vente = 0
        for commande in commandes:
            articles_brut = commande.article_set.all()
            prix_article = sum(article.price for article in articles_brut)

            articles_cadre = commande.articlecadre_set.all()
            prix_cadre = sum(article.price for article in articles_cadre)

            articles_autre = commande.articleautre_set.all()
            prix_autre_produit = sum(article.price for article in articles_autre)

            prix_total_vente += prix_article + prix_autre_produit + prix_cadre
    else:
        prix_total_vente = None

    context = {
        'nb_categorie': nb_categorie,
        'nb_produit': nb_produit,
        'nb_autre_produit': nb_autre_produit,
        # ...
        'prix_total_vente': prix_total_vente,
        'date_form': date_form,
    }

    """




    return render(request, 'StatApp/statistique.html', {
        'nb_categorie':nb_categorie,
        'nb_produit':nb_produit,
        'nb_autre_produit':nb_autre_produit,
        'labels1': labels1,
        'data1': data1,
        'nb_cadre':nb_cadre,
        'consommation_total': consommation_total,
        'prix_total_cadre': prix_total_cadre,
        'prix_service_total':prix_service_total,


        'prix_total_vente': prix_total_vente,
        'prix_total_achat': prix_total_achat,

        'nb_fournisseur':nb_fournisseur,

        'nb_client':nb_client,
        'nb_dette':nb_dette,
        'labels3': labels3,
        'data3': data3,



        'dette_client':dette_client,
        'dette_fournisseur': dette_fournisseur,

        #'labels8': labels8,
        #'data8': data8,

        'labels9': labels9,
        'data9': data9,

        'labels10': labels10,
        'data10': data10,

        'labels11': labels11,
        'data11': data11,
    })


