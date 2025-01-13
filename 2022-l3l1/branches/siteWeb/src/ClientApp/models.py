from _decimal import Decimal

from django.db import models


class Client(models.Model):
        """
        Modèle représentant un client.

        Attributs:
        - prenom : champ CharField pour stocker le prénom du client
        - nom : champ CharField pour stocker le nom de famille du client
        - email : champ EmailField pour stocker l'adresse e-mail du client 
        - type : champ CharField pour stocker le type de client (particulier ou professionnel)
        - adresse : champ CharField pour stocker l'adresse du client
        - tel : champ CharField pour stocker le numéro de téléphone du client
        - dette : champ DecimalField pour stocker la dette du client (par défaut 0)
        - piece_ID : champ FileField pour stocker une pièce d'identité du client (facultatif)

        Méthodes:
        - __str__ : méthode pour représenter le client sous forme de chaîne de caractères
        """

        TYPE = (
                ('Particulier', 'Particulier'),
                ('Professionnel', 'Professionel'),
        )

        prenom = models.CharField(max_length=40)
        nom = models.CharField(max_length=40)
        email = models.EmailField(max_length=254,default=None)
        type = models.CharField( max_length=200, null=True, choices=TYPE)
        adresse = models.CharField(max_length=100)
        tel = models.CharField(max_length=20)
        dette = models.DecimalField(max_digits=10, decimal_places=2,default=Decimal('0'))
        piece_ID = models.FileField(upload_to='piece_ID',blank=True)


        class Meta:
                verbose_name="Client"
                verbose_name_plural="Clients"

        def __str__(self):
                return f"{self.prenom} {self.nom}"
