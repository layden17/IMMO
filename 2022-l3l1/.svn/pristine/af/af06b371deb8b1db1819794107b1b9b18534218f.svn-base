from _decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.views import View

from ClientApp.models import Client
from ProduitApp.models import Produit, ProduitBrut, Cadre


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

    def verifRemise(self):
        data = self.cleaned_data['remise']
        if data < 0 or data > 100:  # Les valeurs limites sont 10 et 100
            raise models.ValidationError("La remise doit être comprise entre 0 et 100.")
        return data

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.statut == '1' or self.statut == 'En attente' :
            self.date_reception = None
        super().save(*args, **kwargs)

    @property
    def total_order(self):
        order_items = Article.objects.filter(commande=self.id)
        order_cadre = ArticleCadre.objects.filter(commande=self.id)
        sum = 0
        for order_item in order_items:
            sum = sum + order_item.price
        for order_cadre in order_cadre:
            sum = sum + order_cadre.price
        return (sum)

    @property
    def total_qty(self):
        order_items = Article.objects.filter(commande=self.id)
        order_cadre = ArticleCadre.objects.filter(commande=self.id)
        total_qty = 0
        for order_item in order_items:
            total_qty = (order_item.quantite + total_qty)
        for order_cadre in order_cadre:
            total_qty = (order_cadre.quantite + total_qty)
        return total_qty


class Article(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    unProduit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    #stock = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='saleitem')

    @property
    def price(self):
        return self.quantite * self.unProduit.prix


    def __str__(self):
        return f'{self.quantite} x {self.unProduit}'

class ArticleCadre(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    cadre = models.ForeignKey(Cadre, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=0)

    @property
    def price(self):
        return self.quantite * self.cadre.prix

    def __str__(self):
        return f'{self.quantite} x {self.cadre}'