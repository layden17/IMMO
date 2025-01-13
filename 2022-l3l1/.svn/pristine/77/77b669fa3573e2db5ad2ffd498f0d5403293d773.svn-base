from django.db import models
from django.core.validators import RegexValidator

class Fournisseurs(models.Model):

    Raison_social=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    Numero_Telephone = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    Fax=models.CharField(validators = [phoneNumberRegex],max_length=100,null=True,blank=True)
    Versement=models.DecimalField(max_digits=10, decimal_places=2)
    Dette=models.DecimalField(max_digits=10, decimal_places=2)
    Facture = models.FileField(upload_to='invoices', null=True, blank=True) # nouveau champ pour les factures
# Create your models here.
    def __str__(self):
        return self.Raison_social