from django.db import models
from FournisseursApp.models import Fournisseurs
from ProduitApp.models import Produit

class Achat(models.Model):
    fournisseur = models.ForeignKey(Fournisseurs, on_delete=models.CASCADE)
    produits=models.ManyToManyField(Produit)
    date_achat = models.DateTimeField()
    Categorie=models.CharField(max_length=50)
    Quantite_en_Quintal=models.FloatField()
    Quantite_en_Bar=models.FloatField()
    Quantite_en_Metre=models.FloatField()
    tva_pourcentage = models.FloatField()
    tva = models.FloatField()
    prix = models.FloatField()
    prix_total = models.FloatField()
    type_facture = models.CharField(max_length=50)


# Create your models here.
