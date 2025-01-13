from django.db import models
from django.urls import reverse
from django.utils import timezone

from django.core.validators import MinValueValidator
from _decimal import Decimal


class Categorie(models.Model):
    """
    Modèle Django représentant une catégorie de produits.

    Attributes:
        name (str): Nom de la catégorie.

    """
    name=models.CharField(max_length=100)

    class Meta:
        """
        Classe interne utilisée par Django pour configurer le modèle.
        Définit les options du modèle, telles que les noms d'affichage.

        Attributes:
            verbose_name (str): Nom d'affichage singulier de l'objet.
            verbose_name_plural (str): Nom d'affichage pluriel de l'objet.

        """
        verbose_name="Categorie"
        verbose_name_plural="Categories"

    def __str__(self):
        """
        Méthode pour renvoyer une représentation en chaîne de caractères de l'objet Categorie.

        Returns:
            str: Nom de la catégorie.

        """
        return self.name

    def get_absolute_url(self):
        """
        Méthode pour obtenir l'URL absolue de l'objet Categorie.

        Returns:
            str: URL absolue de l'objet Categorie.

        """
        return reverse('ProduitApp:create_categorie', args=[str(self.id)])


"""
classe mère de tous les produits 
"""
class Produit(models.Model):
    """
    Modèle Django représentant un produit.

    Attributes:
        designation (str): Nom du produit.
        description (str): Description du produit.
        TVA (float): Taux de TVA du produit.
        prix (decimal): Prix du produit.
        categorie (Categorie): Catégorie du produit.
        quantity (int): Quantité du produit.
        is_deleted (bool): État du produit (supprimé ou non).
        stock_alerte (decimal): Niveau d'alerte du stock du produit.

    """
    designation = models.CharField(max_length=100)
    description = models.TextField(max_length=100) # non obligatoire   ,
    TVA= models.FloatField(default=0)
    prix = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))],null=True)
    categorie= models.ForeignKey( Categorie ,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)
    #providers = models.ManyToManyField(providers)  listes des fournissuers pas encore defini

    stock_alerte=models.DecimalField(max_digits=10, decimal_places=2,default=0)# definir en quintal
    #barre ou metre ?

                     
    class Meta:
        """
        Classe interne utilisée par Django pour configurer le modèle.
        Définit les options du modèle, telles que les noms d'affichage.

        Attributes:
            verbose_name (str): Nom d'affichage singulier de l'objet.
            verbose_name_plural (str): Nom d'affichage pluriel de l'objet.

        """
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        """
        Méthode pour renvoyer une représentation en chaîne de caractères de l'objet Produit.

        Returns:
            str: Nom du produit.

        """
        return self.designation
    
    def categorie_display(self):
        """
        Méthode pour renvoyer le nom de la catégorie du produit.

        Returns:
            str: Nom de la catégorie du produit.

        """
        return self.categorie

"""
autres produits divers qui ne seront ni des produits brut ni des cadres
"""
class AutreProduit(Produit):
    """
    Classe représentant un produit autre que les produits bruts.
    Hérite de la classe Produit.
s
    Attributes:
        prix_achat (Decimal): le prix d'achat du produit
        prix_vente (Decimal): le prix de vente du produit
        quantite (Decimal): la quantité du produit en stock

    Methods:
        get_absolute_url(): retourne l'URL de détail du produit

    """
    prix_achat=models.DecimalField(max_digits=10, decimal_places=2)
    prix_vente=models.DecimalField(max_digits=10, decimal_places=2)
    quantite=models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def get_absolute_url(self):
        """
        Retourne l'URL de détail du produit.

        Returns:
            str: l'URL de détail du produit
        """
        return reverse('ProduitApp:autre_produit_detail', args=[str(self.id)])


    class Meta:
        """
        Classe Meta pour la configuration de la classe AutreProduit.

        Attributes:
            verbose_name (str): le nom de la classe au singulier pour l'affichage dans l'interface d'administration
            verbose_name_plural (str): le nom de la classe au pluriel pour l'affichage dans l'interface d'administration
        """
        verbose_name = "Autre produit"
        verbose_name_plural = "Autres produits"

    

class CategorieFer(models.Model):
    """
    Modèle représentant une catégorie de produit en fer.

    Attributes:
        name (str): Le nom de la catégorie.
        nb_m_par_quintal (int): Le nombre de mètres par quintal.
        nb_bar_par_quintal (int): Le nombre de barres par quintal.
    """
    name=models.CharField(max_length=100)
    nb_m_par_quintal=models.IntegerField()
    nb_bar_par_quintal=models.IntegerField()

    class Meta:
        verbose_name = "Categorie_fer"
        verbose_name_plural = "Categories_fer"

    def __str__(self):
        """
        Renvoie la représentation en chaîne de caractères de l'objet.

        Returns:
            str: Le nom de la catégorie.
        """
        return self.name

"""
classe qui représente les produits bruts: fer avec différents diamètres possibles
"""
class ProduitBrut(Produit):
    """
    Classe représentant un produit brut.

    Attributes:
        type_fer (str): Le type de fer (choix prédéfinis).
        stock_quintal (Decimal): Le stock en quintal du produit brut.
        stock_barre (int): Le stock en barres du produit brut.
        stock_metre (Decimal): Le stock en mètres du produit brut.
        prix_quintal (Decimal): Le prix en quintal du produit brut.
        prix_metre (Decimal): Le prix au mètre du produit brut.
        prix_barre (Decimal): Le prix à la barre du produit brut.
        prix_achat_quintal (Decimal): Le prix d'achat en quintal du produit brut.
        prix_achat_barre (Decimal): Le prix d'achat à la barre du produit brut.
        prix_achat_metre (Decimal): Le prix d'achat au mètre du produit brut.

    Methods:
        get_absolute_url(): Retourne l'URL absolue de la vue détaillée pour ce produit brut.
        save(*args, **kwargs): Sauvegarde le produit brut avec la catégorie "produit brut".
    """
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
modele qui garde l'historique de chaque prix quintal pour les produit brut
"""
class HistoriquePrixAchatQuintal(models.Model):
    """
    Modèle représentant l'historique des prix d'achat au quintal d'un produit brut.

    Attributes:
        produit (ForeignKey): clé étrangère vers le modèle ProduitBrut représentant le produit associé à l'historique des prix.
        prix (DecimalField): le prix d'achat au quintal du produit associé.
        date (DateTimeField): la date à laquelle le prix d'achat au quintal a été enregistré.

    Meta:
        ordering (list): liste des champs de classe utilisée pour trier les résultats lors de la requête.

    Methods:
        __str__(): retourne une représentation sous forme de chaîne de caractères de l'objet courant.
    """
    produit = models.ForeignKey(ProduitBrut, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères de l'objet courant.

        Returns:
            str: une chaîne de caractères représentant l'objet courant.
        """
        return f"{self.produit} - {self.prix} - {self.date}"




"""
classe pour les cadre qui peuvent etre de plusieurs formes différentes  : carré, cercle...
"""
class Cadre(models.Model):
    """
    Classe représentant un type de cadre.

    Attributs:
        cadre_choix (models.CharField): type de cadre choisi parmi une liste de choix possibles.
        article_choix (models.ManyToManyField): articles choisis pour la confection du cadre.
        longueur (models.DecimalField): nombre total de mètre nécessaire pour la confection du cadre (par défaut 0).
        largeur (models.DecimalField): largeur du cadre (par défaut 0).
        crochet (models.DecimalField): crochet utilisé pour la confection du cadre (par défaut 0).
        prix_service (models.DecimalField): prix de service pour la confection du cadre (par défaut 0).
        chute (models.BooleanField): booléen indiquant si une chute est présente (par défaut False).
        prix_quntal (models.FloatField): prix par quintal (par défaut 0).
        nombre_barre (models.FloatField): nombre de barres nécessaires pour la confection du cadre (par défaut 0).
        consommation_sans_chute (models.DecimalField): consommation de métal nécessaire pour la confection du cadre sans la chute (par défaut 0).
        consommation (models.DecimalField): consommation de métal nécessaire pour la confection du cadre avec la chute (par défaut 0).
        chute_valeur (models.DecimalField): valeur de la chute (par défaut 0).
        max (models.DecimalField): nombre maximum de cadre pouvant être confectionnés (par défaut 0).
        prix (models.DecimalField): prix total pour la confection du cadre (par défaut 0).
    """
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

    """
    Formulaire
    """
    cadre_choix = models.CharField(max_length=100, choices=Cadre_choix, default='Cadre')
    article_choix = models.ManyToManyField(ProduitBrut)
    prix_metre = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    longueur = models.DecimalField(max_digits=10, decimal_places=2, default=0) # nombre total de mètre nécessaire pour la confection du cadre
    largeur =  models.DecimalField(max_digits=10, decimal_places=2, default=0)
    crochet = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prix_service = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    chute = models.BooleanField(default=False)

    """
    Resultats
    """
    consommation_sans_chute = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    consommation = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    crochet_opti = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    chute_valeur = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    max = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prix = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    class Meta:
        verbose_name = "Cadre"
        verbose_name_plural = "Cadres"

    def __str__(self):
        return f'{self.cadre_choix} de {self.article_choix}'
