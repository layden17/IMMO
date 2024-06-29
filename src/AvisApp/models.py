from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
from django.db import models

class Message(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Avis(models.Model):
    nom = models.CharField(max_length=100)
    commentaire = models.TextField()
    note = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avis de {self.nom} le {self.date_creation}"


