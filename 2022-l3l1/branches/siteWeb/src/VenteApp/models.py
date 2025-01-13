from _decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models, transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.views import View

from ClientApp.models import Client
from ProduitApp.models import Produit, ProduitBrut, Cadre, AutreProduit

"""
Modèle représentant une commande passée par un client.
"""

class Commande(models.Model):

    STATUS = (
        ( 'En attente','En attente'),
        ( 'Livré','Livré'),
    )

    client = models.ForeignKey(Client,null=True, on_delete=models.CASCADE)
    date_creation= models.DateTimeField(auto_now_add=True)
    date_reception=models.DateTimeField(verbose_name='Date_reception',blank=True,null=True)
    statut = models.CharField( max_length=200, null=True, choices=STATUS,verbose_name='Statut')
    remise = models.IntegerField(default=0)

    tax_amount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)
            # reduce the stock of cadres for this order
            articleCadres = ArticleCadre.objects.filter(commande=self.id)
            articlesBrut = Article.objects.filter(commande=self.id)
            articlesAutres = ArticleAutre.objects.filter(commande=self.id)

            for article in articlesAutres :
                produit = article.produit
                produit.quantite -= article.quantite
                produit.save()
            for article in articlesBrut :
                produit = article.produit

                if article.unite == 'Par quintal':
                    print("quintal")
                    print(produit.type_fer)
                    if produit.type_fer =='Fer /8':
                        print("fer 8")
                        produit.stock_quintal -= Decimal(article.quantite)
                        produit.stock_metre -= Decimal(article.quantite * 12)
                        produit.stock_barre -= Decimal(article.quantite * 20)
                        produit.save()
                    elif produit.type_fer=="Fer /10" :
                        produit.stock_quintal -= Decimal(article.quantite)
                        produit.stock_metre -= Decimal(article.quantite * 12)
                        produit.stock_barre -= Decimal(article.quantite * 12)
                        produit.save()
                    elif produit.type_fer=="Fer /12" :
                        produit.stock_quintal -= Decimal(article.quantite)
                        produit.stock_metre -= Decimal(article.quantite * 12)
                        produit.stock_barre -= Decimal(article.quantite * 9)
                        produit.save()
                    elif produit.type_fer=="Fer /14" :
                        produit.stock_quintal -= Decimal(article.quantite)
                        produit.stock_metre -= Decimal(article.quantite * 12)
                        produit.stock_barre -= Decimal(article.quantite * 7)
                        produit.save()
                    elif produit.type_fer=="Fer /16" :
                        produit.stock_quintal -= Decimal(article.quantite)
                        produit.stock_metre -= Decimal(article.quantite * 12)
                        produit.stock_barre -= Decimal(article.quantite * 5)
                        produit.save()

                elif article.unite == 'Par mètre':
                    if produit.type_fer=="Fer /8" :
                        produit.stock_metre -= Decimal(article.quantite)
                        produit.stock_quintal -= Decimal(article.quantite / 12)
                        produit.stock_barre -= Decimal(article.quantite * 5/3)
                        produit.save()
                    elif produit.type_fer=="Fer /10" :
                        produit.stock_metre -= Decimal(article.quantite)
                        produit.stock_quintal -= Decimal(article.quantite / 12)
                        produit.stock_barre -= Decimal(article.quantite)
                        produit.save()
                    elif produit.type_fer=="Fer /12" :
                        produit.stock_metre -= Decimal(article.quantite)
                        produit.stock_quintal -= Decimal(article.quantite / 12)
                        produit.stock_barre -= Decimal(article.quantite * 3/4)
                        produit.save()
                    elif produit.type_fer=="Fer /14" :
                        produit.stock_metre -= Decimal(article.quantite)
                        produit.stock_quintal -= Decimal(article.quantite / 12)
                        produit.stock_barre -= Decimal(article.quantite * 7/12)
                        produit.save()
                    elif produit.type_fer=="Fer /16" :
                        produit.stock_metre -= Decimal(article.quantite)
                        produit.stock_quintal -= Decimal(article.quantite / 12)
                        produit.stock_barre -= Decimal(article.quantite * 5/12)
                        produit.save()

                elif article.unite == 'Par barre':
                    if produit.type_fer=="Fer /8" :
                        produit.stock_barre -= Decimal(article.quantite)
                        produit.stock_quintal -= Decimal(article.quantite / 20)
                        produit.stock_metre -= Decimal(article.quantite * 3/5)
                        produit.save()
                    elif produit.type_fer=="Fer /10" :
                        produit.stock_barre -= Decimal(article.quantite)
                        produit.stock_quintal -= Decimal(article.quantite / 20)
                        produit.stock_metre -= Decimal(article.quantite)
                        produit.save()
                    elif produit.type_fer=="Fer /12" :
                        produit.stock_barre -= Decimal(article.quantite)
                        produit.stock_quintal -= Decimal(article.quantite / 20)
                        produit.stock_metre -= Decimal(article.quantite * 4/3)
                        produit.save()
                    elif produit.type_fer=="Fer /14" :
                        produit.stock_barre -= Decimal(article.quantite)
                        produit.stock_quintal -= Decimal(article.quantite / 20)
                        produit.stock_metre -= Decimal(article.quantite * 12/7)
                        produit.save()
                    elif produit.type_fer == "Fer /16":
                        produit.stock_barre -= Decimal(article.quantite)
                        produit.stock_quintal -= Decimal(article.quantite / 20)
                        produit.stock_metre -= Decimal(article.quantite * 12 / 5)
                        produit.save()

#supprimer une commande
    def delete(self, *args, **kwargs):
        with transaction.atomic():
            # augmenter la quantité de cadres pour chaque ArticleCadre lié à cette commande
            articleCadres = ArticleCadre.objects.filter(commande=self.id)
            articlesBrut = Article.objects.filter(commande=self.id)
            articlesAutres = ArticleAutre.objects.filter(commande=self.id)
            for article in articleCadres:
                cadre = article.cadre
                cadre.quantity += article.quantite
                cadre.save()
            for article in articlesAutres:
                produit = article.produit
                produit.quantite += article.quantite
                produit.save()
            for article in articlesBrut:
                produit = article.produit

                if article.unite == 'Par quintal':
                    if produit.type_fer == "Fer /8":
                        produit.stock_quintal += Decimal(article.quantite)
                        produit.stock_metre += Decimal(article.quantite * 12)
                        produit.stock_barre += Decimal(article.quantite * 20)
                        produit.save()
                    elif produit.type_fer == "Fer /10":
                        produit.stock_quintal += Decimal(article.quantite)
                        produit.stock_metre += Decimal(article.quantite * 12)
                        produit.stock_barre += Decimal(article.quantite * 12)
                        produit.save()
                    elif produit.type_fer == "Fer /12":
                        produit.stock_quintal += Decimal(article.quantite)
                        produit.stock_metre += Decimal(article.quantite * 12)
                        produit.stock_barre += Decimal(article.quantite * 9)
                        produit.save()
                    elif produit.type_fer == "Fer /14":
                        produit.stock_quintal += Decimal(article.quantite)
                        produit.stock_metre += Decimal(article.quantite * 12)
                        produit.stock_barre += Decimal(article.quantite * 7)
                        produit.save()
                    elif produit.type_fer == "Fer /16":
                        produit.stock_quintal += Decimal(article.quantite)
                        produit.stock_metre += Decimal(article.quantite * 12)
                        produit.stock_barre += Decimal(article.quantite * 5)
                        produit.save()

                elif article.unite == 'Par mètre':
                    if produit.type_fer == "Fer /8":
                        produit.stock_metre += Decimal(article.quantite)
                        produit.stock_quintal += Decimal(article.quantite / 12)
                        produit.stock_barre += Decimal(article.quantite * 5 / 3)
                        produit.save()
                    elif produit.type_fer == "Fer /10":
                        produit.stock_metre += Decimal(article.quantite)
                        produit.stock_quintal += Decimal(article.quantite / 12)
                        produit.stock_barre += Decimal(article.quantite)
                        produit.save()
                    elif produit.type_fer == "Fer /12":
                        produit.stock_metre += Decimal(article.quantite)
                        produit.stock_quintal += Decimal(article.quantite / 12)
                        produit.stock_barre += Decimal(article.quantite * 3 / 4)
                        produit.save()
                    elif produit.type_fer == "Fer /14":
                        produit.stock_metre += Decimal(article.quantite)
                        produit.stock_quintal += Decimal(article.quantite / 12)
                        produit.stock_barre += Decimal(article.quantite * 7 / 12)
                        produit.save()
                    elif produit.type_fer == "Fer /16":
                        produit.stock_metre += Decimal(article.quantite)
                        produit.stock_quintal += Decimal(article.quantite / 12)
                        produit.stock_barre += Decimal(article.quantite * 5 / 12)
                        produit.save()

                elif article.unite == 'Par barre':
                    if produit.type_fer == "Fer /8":
                        produit.stock_barre += Decimal(article.quantite)
                        produit.stock_quintal += Decimal(article.quantite / 20)
                        produit.stock_metre += Decimal(article.quantite * 3 / 5)
                        produit.save()
                    elif produit.type_fer == "Fer /10":
                        produit.stock_barre += Decimal(article.quantite)
                        produit.stock_quintal += Decimal(article.quantite / 20)
                        produit.stock_metre += Decimal(article.quantite)
                        produit.save()
                    elif produit.type_fer == "Fer /12":
                        produit.stock_barre += Decimal(article.quantite)
                        produit.stock_quintal += Decimal(article.quantite / 20)
                        produit.stock_metre += Decimal(article.quantite * 4 / 3)
                        produit.save()
                    elif produit.type_fer == "Fer /14":
                        produit.stock_barre += Decimal(article.quantite)
                        produit.stock_quintal += Decimal(article.quantite / 20)
                        produit.stock_metre += Decimal(article.quantite * 12 / 7)
                        produit.save()
                    elif produit.type_fer == "Fer /16":
                        produit.stock_barre += Decimal(article.quantite)
                        produit.stock_quintal += Decimal(article.quantite / 20)
                        produit.stock_metre += Decimal(article.quantite * 12 / 5)
                        produit.save()
            # supprimer la commande
            super().delete(*args, **kwargs)

    """
    Calcule le montant total de la commande en additionnant le prix de chaque article de la commande,
    ainsi que le prix de chaque cadre.
    
    Returns:
        Le montant total de la commande.
    """
    @property
    def total_order(self):
        order_items = Article.objects.filter(commande=self.id)
        order_cadre = ArticleCadre.objects.filter(commande=self.id)
        order_autre = ArticleAutre.objects.filter(commande=self.id)
        sum = 0
        for order_item in order_items:
            sum = sum + order_item.price
        for order_cadre in order_cadre:
            sum = sum + order_cadre.price
        for order_autre in order_autre:
            sum = sum + order_autre.price
        return (sum)

    """
    Calcule la quantité totale d'articles de la commande en additionnant la quantité de chaque article de la commande,
    ainsi que la quantité de chaque cadre.
    
    Returns:
        La quantité totale d'articles de la commande.
    """
    @property
    def total_qty(self):
        order_items = Article.objects.filter(commande=self.id)
        order_cadre = ArticleCadre.objects.filter(commande=self.id)
        order_autre = ArticleAutre.objects.filter(commande=self.id)
        total_qty = 0
        for order_item in order_items:
            total_qty = (order_item.quantite + total_qty)
        for order_cadre in order_cadre:
            total_qty = (order_cadre.quantite + total_qty)
        for order_autre in order_autre:
            total_qty = (order_autre.quantite + total_qty)
        return total_qty

    """
    Model représentant un article vendu dans une commande.

    Attributes:
        commande (Commande): La commande à laquelle cet article est associé.
        produit (ProduitBrut): Le produit brut vendu dans cet article.
        unite (str): L'unité de mesure dans laquelle est vendu le produit brut.
        quantite (int): La quantité de produit brut vendue.
        prix (float): Le prix unitaire de vente de l'article.
        total (float): Le prix total de l'article (prix unitaire x quantité).
    """


class Article(models.Model):

    UNITE = (
        ('Par barre', 'Par barre'),
        ('Par mètre', 'Par mètre'),
        ('Par quintal', 'Par quintal'),
    )
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(ProduitBrut, on_delete=models.CASCADE,verbose_name='Produit(s) brut(s)')
    unite = models.CharField(max_length=200, null=True, choices=UNITE, verbose_name='Unite')
    quantite = models.IntegerField(default=1)
    prix = models.FloatField(default=0)
    total = models.FloatField(default=0)
    #stock = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='saleitem')

    @property
    def price(self):
        calcul = 0
        if self.unite == 'Par barre':
            calcul = self.quantite * self.produit.prix_barre
        elif self.unite == 'Par mètre':
            calcul = self.quantite * self.produit.prix_metre
        elif self.unite == 'Par quintal':
            calcul = self.quantite * self.produit.prix_quintal
        return calcul

    def __str__(self):
        return f'{self.quantite} x {self.produit}'


    """
    A model representing an article of type 'cadre' in a command.

    Attributes:
        commande (ForeignKey): The command to which this article belongs.
        cadre (ForeignKey): The cadre that makes up this article.
        quantite (int): The quantity of this article in the command.
        prix_unite (int): The price of the cadre per unit.

    Methods:
        save(*args, **kwargs): Overrides the default save method to set the price per unit based on the cadre.
        price: Calculates and returns the total price of this article.
        __str__: Returns a string representation of this article, showing the quantity and the cadre name.

    """


class ArticleCadre(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    cadre = models.ForeignKey(Cadre, on_delete=models.CASCADE,verbose_name='Cadre(s)')
    quantite = models.IntegerField(default=0)
    prix_unite = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.prix_unite = self.cadre.prix
        super().save(*args, **kwargs)

    @property
    def price(self):
        return self.quantite * self.cadre.prix

    def __str__(self):
        return f'{self.quantite} x {self.cadre}'



    """
    A model representing an article of type 'cadre' in a command.

    Attributes:
        commande (ForeignKey): The command to which this article belongs.
        cadre (ForeignKey): The cadre that makes up this article.
        quantite (int): The quantity of this article in the command.
        prix_unite (int): The price of the cadre per unit.

    Methods:
        save(*args, **kwargs): Overrides the default save method to set the price per unit based on the cadre.
        price: Calculates and returns the total price of this article.
        __str__: Returns a string representation of this article, showing the quantity and the cadre name.

    """


class ArticleAutre(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(AutreProduit, on_delete=models.CASCADE,verbose_name='Autre(s) produit(s)')
    quantite = models.IntegerField(default=0)
    prix_unite = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.prix_unite = self.produit.prix_vente
        super().save(*args, **kwargs)

    @property
    def price(self):
        return self.quantite * self.produit.prix_vente

    def __str__(self):
        return f'{self.quantite} x {self.produit}'


