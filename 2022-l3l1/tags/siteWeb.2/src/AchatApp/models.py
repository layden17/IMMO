from django.db import models
import FournisseursApp
from FournisseursApp.models import Fournisseurs
from ProduitApp.models import Produit

class Achat(models.Model):
    fournisseur = models.ForeignKey(Fournisseurs, on_delete=models.CASCADE)
    produits=models.ManyToManyField(Produit)
    date_achat = models.DateTimeField()
    categorie=models.CharField(max_length=50,null=True)
    prix_total = models.FloatField()
    Versement=models.FloatField(null=True)
    Dette=models.FloatField(null=True)
    type_facture = models.CharField(max_length=50)
    fichier = models.FileField(upload_to='factures/', null=True,blank=True)
    
    def save(self,  *args, **kwargs):
        # Enregistrer le nouvel achat
        super().save(*args, **kwargs)
        if self.factures.exists():
            # Mettre à jour les factures associées à l'achat, si elles existent
            for facture in self.factures.all():
                facture.Dette = self.Dette
                facture.Versement = self.Versement
                facture.montant = self.prix_total
                facture.fichier=self.fichier
                facture.save()
        else:
             facture = Facture.objects.create(
                achat=self,
                fournisseur=self.fournisseur,
                fichier=self.fichier,
                montant=self.prix_total,
                Versement = self.Versement,
                Dette = self.Dette)
             facture.save()
        fournisseur = self.fournisseur
        fournisseur.Dette = fournisseur.Dette + self.Dette
        fournisseur.Versement=fournisseur.Versement+self.Versement
        fournisseur.save()
   

class Facture(models.Model):
        achat = models.ForeignKey(Achat, on_delete=models.CASCADE, related_name='factures',default='')
        fournisseur = models.ForeignKey(Fournisseurs, on_delete=models.CASCADE, related_name='factures')
        fichier = models.FileField(upload_to='factures/', null=True,blank=True)
        date_creation = models.DateTimeField(auto_now_add=True)
        montant = models.DecimalField(max_digits=10, decimal_places=2,null=True) # Champ supplémentaire pour stocker les informations de facture
        Versement = models.DecimalField(max_digits=10, decimal_places=2,null=True)
        Dette = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    
        def __str__(self):
            return f"Facture-{self.pk} ({self.fournisseur})"
        
        def save(self, *args, **kwargs):
        # Remplir automatiquement les champs Dette et Versement avec les valeurs correspondantes de l'achat associé
            if not self.id:  # Si la facture n'existe pas encore
                self.Dette = self.achat.Dette
                self.Versement = self.achat.Versement
                self.montant=self.achat.prix_total
                self.fichier=self.achat.fichier
            
            super().save(*args, **kwargs)



# Create your models here.
