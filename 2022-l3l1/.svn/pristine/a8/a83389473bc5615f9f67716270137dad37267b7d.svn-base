from django import forms
from .models import Fournisseurs  # Importation du modèle Fournisseurs

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseurs  # Utilisation du modèle Fournisseurs pour créer un formulaire
        fields = ['Raison_social','email','Numero_Telephone','Fax'] # Définition des champs du formulaire
