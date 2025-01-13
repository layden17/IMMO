from django.db import models  # Importe les modèles nécessaires à l'utilisation de la base de données.
from django.core.validators import RegexValidator  # Un module Django qui permet de valider une expression régulière
from django.urls import reverse  # Permet d'avoir accès au bon URL 

class Fournisseurs(models.Model):
    Raison_social = models.CharField(max_length=100)  # Champ pour le nom de la société
    email = models.EmailField(max_length=100)  # Champ pour l'adresse e-mail
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")  # Validation de l'expression régulière pour les numéros de téléphone
    Numero_Telephone = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)  # Champ pour le numéro de téléphone, validé par l'expression régulière phoneNumberRegex et unique
    Fax = models.CharField(validators=[phoneNumberRegex], max_length=100, null=True, blank=True)  # Champ pour le numéro de fax, validé par l'expression régulière phoneNumberRegex et qui peut être null et vide
    Versement = models.FloatField(default=0)  # Champ pour les versements, qui a une valeur par défaut de 0
    Dette = models.FloatField(default=0)  # Champ pour les dettes, qui a une valeur par défaut de 0
    
    def __str__(self):  # Méthode pour retourner le nom de la société
        return self.Raison_social 
