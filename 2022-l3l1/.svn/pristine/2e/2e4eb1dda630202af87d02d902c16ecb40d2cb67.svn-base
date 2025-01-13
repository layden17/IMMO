
from django.forms import ModelForm
from ClientApp.models import Client


class ClientForms(ModelForm):
    """
    Formulaire pour ajouter ou modifier un client.

    Le formulaire est basé sur le modèle Client.

    Champs :
    - prenom : champ pour saisir le prénom du client
    - nom : champ pour saisir le nom de famille du client
    - email : champ pour saisir l'adresse e-mail du client 
    - type : champ pour saisir le type de client (particulier ou professionnel)
    - adresse : champ pour saisir l'adresse du client
    - tel : champ pour saisir le numéro de téléphone du client
    - dette : champ pour saisir la dette du client (par défaut 0)
    - piece_ID : champ pour téléverser une pièce d'identité du client 
    """

    class Meta:
        model = Client
        fields = ['prenom', 'nom', 'email','type' , 'adresse', 'tel','dette','piece_ID']


