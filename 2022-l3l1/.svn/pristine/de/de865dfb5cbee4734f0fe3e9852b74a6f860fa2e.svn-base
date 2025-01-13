from django.db import models
from django.urls import reverse

from django.core.validators import MinValueValidator
from _decimal import Decimal

"""
classe catégorie pour les produits
"""
class Categorie(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name="Categorie"
        verbose_name_plural="Categories"

    def __str__(self):
        return self.name


"""
classe mère de tous les produits 
"""
class Produit(models.Model):
    designation = models.CharField(max_length=100)
    description = models.TextField(max_length=100) # non obligatoire   ,
    TVA= models.FloatField(default=0)
    prix = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    categorie= models.ForeignKey( Categorie ,on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)
    #providers = models.ManyToManyField(providers)  listes des fournissuers pas encore defini

    stock_alerte=models.DecimalField(max_digits=10, decimal_places=2,default=0)# definir en quintal
    #barre ou metre ?

                     
    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.designation

"""
autres produits divers qui ne seront ni des produits brut ni des cadres
"""
class AutreProduit(Produit):
    prix_achat=models.DecimalField(max_digits=10, decimal_places=2)
    prix_vente=models.DecimalField(max_digits=10, decimal_places=2)
    quantite=models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def get_absolute_url(self):
        return reverse('ProduitApp:autre_produit_detail', args=[str(self.id)])


    class Meta:
        verbose_name = "Autre produit"
        verbose_name_plural = "Autres produits"

    

class CategorieFer(models.Model):
    name=models.CharField(max_length=100)
    nb_m_par_quintal=models.IntegerField()
    nb_bar_par_quintal=models.IntegerField()

    class Meta:
        verbose_name = "Categorie_fer"
        verbose_name_plural = "Categories_fer"

    def __str__(self):
        return self.name

"""
classe qui représente les produits bruts: fer avec différents diamètres possibles
"""
class ProduitBrut(Produit):

    type_fer = (
        ('Fer /6','Fer /6'),
        ('Fer /8','Fer /8'),
        ('Fer /10','Fer /10'),
        ('Fer /12','Fer /12'),
        ('Fer /14','Fer /14'),
        ('Fer /16','Fer /16'),

    )
    type_fer = models.CharField(max_length=100, choices=type_fer, default='Fer /6')

    
    stock_quintal=models.DecimalField(max_digits=10, decimal_places=2)
    stock_barre=models.IntegerField()
    stock_metre= models.DecimalField(max_digits=10, decimal_places=2)

    prix_quintal = models.DecimalField(max_digits=10, decimal_places=2)
    prix_metre = models.DecimalField(max_digits=10, decimal_places=2)
    prix_barre = models.DecimalField(max_digits=10, decimal_places=2)


    prix_achat_quintal = models.DecimalField(max_digits=10, decimal_places=2)
    prix_achat_barre = models.DecimalField(max_digits=10, decimal_places=2)
    prix_achat_metre = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return reverse('ProduitApp:produit_detail', args=[str(self.id)])


    class Meta:
        verbose_name = "Produit brut"
        verbose_name_plural = "Produits bruts"

    def save(self, *args, **kwargs):
        self.categorie = Categorie.objects.get(name='produit brut')
        super(ProduitBrut, self).save(*args, **kwargs)


"""
classe pour les cadre qui peuvent etre de plusieurs formes différentes  : carré, cercle...
"""
class Cadre(models.Model):
    Cadre_choix = (
        ('Cadre','Cadre'),
        ('Octogone','Octogone'),
        ('Hexagon','Hexagon'),
        ('Losange','Losange'),
        ('Epingle','Epingle'),
        ('Crochet','Crochet'),
        ('Higes','Higes'),
        ('Senelle','Senelle'),
        ('Fiche Poteau','Fiche Poteau'),
        ('S','S'),
    )

    Article_choix = (
        ('Fer /6','Fer /6'),
        ('Fer /8','Fer /8'),
        ('Fer /10','Fer /10'),
        ('Fer /12','Fer /12'),
        ('Fer /14','Fer /14'),
    )

    cadre_choix = models.CharField(max_length=100, choices=Cadre_choix, default='Cadre')
    article_choix = models.CharField(max_length=100, choices=Article_choix, default='Fer /6')

    longueur = models.DecimalField(max_digits=10, decimal_places=2, default=0) # nombre total de mètre nécessaire pour la confection du cadre
    largeur =  models.DecimalField(max_digits=10, decimal_places=2, default=0)
    crochet = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prix_service = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    chute = models.BooleanField(default=False)

    consommation_sans_chute = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    consommation = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    chute_valeur = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    max = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prix = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Cadre"
        verbose_name_plural = "Cadres"

    def __str__(self):
        return f'{self.cadre_choix} de {self.article_choix}'
