from django import forms
from .models import Fournisseurs
class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseurs
        fields = ['Raison_social','email','Numero_Telephone','Fax']
