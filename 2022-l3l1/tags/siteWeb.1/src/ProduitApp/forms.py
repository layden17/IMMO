from django import forms
from .models import Categorie, ProduitBrut, Cadre, AutreProduit
from django.forms import ModelForm

class CategorieForm(forms.Form):
    name = forms.CharField(max_length=100)

    class Meta:
        model = Categorie
        fields = ['name']


class CadreForms(forms.ModelForm):
    class Meta:
        model = Cadre
        fields = '__all__'



class AutreProduitForm(forms.ModelForm):
    class Meta:
        model = AutreProduit
        fields = '__all__'



class ProduitBrutForm(forms.ModelForm):
    class Meta:
        model = ProduitBrut
        exclude = ['categorie']
        description= forms.CharField(required=False)
    
    stock_quintal = forms.FloatField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'oninput': 'convert_stock()'}), required=False)
    prix_achat_quintal=forms.FloatField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'oninput': 'convert_prix_achat()'}), required=False)
    prix_quintal=forms.FloatField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'oninput': 'convert_prix_vente()'}), required=False)
    