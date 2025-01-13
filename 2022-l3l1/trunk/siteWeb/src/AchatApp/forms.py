from django import forms
from .models import Achat,Facture
from django.forms import ModelForm
from ProduitApp.models import Produit


class AchatForm(ModelForm):
    class Meta:
        model = Achat
        fields = '__all__'

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['fichier']
