from django.db import models  #Importe les modèles nécessaires à l'utilisation de la base de données.
from django.core.validators import RegexValidator  #Un module Django qui permet de valider une expression régulière
from django.urls import reverse  #Permet d'avoir accès au bon URL 

class Fournisseurs(models.Model):
    Raison_social = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    Numero_Telephone = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)
    Fax = models.CharField(validators=[phoneNumberRegex], max_length=100, null=True, blank=True)
    Versement = models.FloatField(default=0)
    Dette = models.FloatField(default=0)
    def __str__(self):  
        return self.Raison_social 
