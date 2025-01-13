
from django.db import models

class Client(models.Model):
        prenom = models.CharField(max_length=40)
        nom = models.CharField(max_length=40)
        type = models.CharField(max_length=15)
        adresse = models.CharField(max_length=100)
        tel = models.CharField(max_length=20)
        #date_ajout = models.DateTimeField()
        #compteur_commande = models.PositiveIntegerField()
        piece_ID = models.FileField(upload_to='piece_ID')

        class Meta:
                verbose_name="Client"
                verbose_name_plural="Clients"

        def __str__(self):
                return self.nom
