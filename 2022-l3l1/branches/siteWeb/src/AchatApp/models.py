from django.db import models
import FournisseursApp
from FournisseursApp.models import Fournisseurs
from ProduitApp.models import Produit,ProduitBrut,AutreProduit



# On importe la classe Model de Django
from django.db import models

# On crée une classe de modèle pour les achats
class Achat(models.Model):
    # On définit les champs du modèle
    fournisseur = models.ForeignKey(Fournisseurs, on_delete=models.CASCADE)
    date_achat = models.DateTimeField()
    prix_total = models.FloatField()
    Versement=models.FloatField(null=True)
    Versement_totalite=models.BooleanField(blank=True,default=False)
    Dette=models.FloatField(null=True)
    fichier = models.FileField(upload_to='factures/', null=True,blank=True)
    produits_bruts=models.ManyToManyField(ProduitBrut,blank=True,through='ProduitBrutLiaison')
    autre_produits=models.ManyToManyField(AutreProduit,blank=True,through='AutreProduitLiaison')
    
    
    # On définit une méthode de sauvegarde personnalisée pour le modèle
    def save(self,  *args, **kwargs):
        # On enregistre le nouvel achat
        super().save(*args, **kwargs)
        if self.factures.exists():
            # Si des factures sont associées à l'achat, on les met à jour avec les nouvelles valeurs
            for facture in self.factures.all():
                facture.Dette = self.Dette
                facture.Versement = self.Versement
                facture.montant = self.prix_total
                facture.fichier=self.fichier
                facture.save()
        else:
            # Sinon, on crée une nouvelle facture pour l'achat
            facture = Facture.objects.create(
                achat=self,
                fournisseur=self.fournisseur,
                fichier=self.fichier,
                montant=self.prix_total,
                Versement = self.Versement,
                Dette = self.Dette)
            facture.save()
        # On met à jour la dette et les versements du fournisseur associé à l'achat
        fournisseur = self.fournisseur
        fournisseur.Dette = fournisseur.Dette + self.Dette
        fournisseur.Versement=fournisseur.Versement+self.Versement
        fournisseur.save()




# On crée une classe de modèle pour la liaison entre les achats et les produits bruts
class ProduitBrutLiaison(models.Model):
    # On définit les champs du modèle
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE)
    produit_brut = models.ForeignKey(ProduitBrut, on_delete=models.CASCADE)
    quantite_quintal=models.FloatField()
    quantite_metre=models.FloatField()
    quantite_bar=models.FloatField()
    prix_total=models.FloatField()



# On crée une classe de modèle pour la liaison entre les achats et les autres produits
class AutreProduitLiaison(models.Model):
    # On définit les champs du modèle
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE)
    autre_produit = models.ForeignKey(AutreProduit, on_delete=models.CASCADE)
    quantite=models.FloatField()
    prix_total=models.FloatField()



   

# On importe la classe Model de Django
from django.db import models

# On crée une classe de modèle pour les factures
class Facture(models.Model):
    # On définit les champs du modèle
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE, related_name='factures',default='')
    fournisseur = models.ForeignKey(Fournisseurs, on_delete=models.CASCADE, related_name='factures')
    fichier = models.FileField(upload_to='factures/', null=True,blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2,null=True) # Champ supplémentaire pour stocker les informations de facture
    Versement = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    Dette = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    
    # On définit une méthode pour retourner une représentation sous forme de chaîne de caractères de l'objet
    def __str__(self):
        return f"Facture-{self.pk} ({self.fournisseur})"
    
    # On définit une méthode de sauvegarde personnalisée pour le modèle
    def save(self, *args, **kwargs):
        # Si la facture n'existe pas encore, on remplit automatiquement les champs Dette et Versement avec les valeurs correspondantes de l'achat associé
        if not self.id:
            self.Dette = self.achat.Dette
            self.Versement = self.achat.Versement
            self.montant=self.achat.prix_total
            self.fichier=self.achat.fichier
        super().save(*args, **kwargs)

