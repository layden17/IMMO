from django import forms
from .models import Achat,Facture
from django.forms import ModelForm
from ProduitApp.models import ProduitBrut,AutreProduit
from django.contrib.admin.widgets import AdminDateWidget
from .models import ProduitBrutLiaison
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.safestring import mark_safe



# On crée une classe de formulaire pour le modèle Achat
class AchatForm(ModelForm):
    # On ajoute des champs personnalisés au formulaire, avec des attributs HTML personnalisés
    Versement_totalite = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'id': 'id_Versement_totalite', 'onchange': 'updateVersementDetteValues();'}))
    Versement=forms.FloatField(widget=forms.TextInput(attrs={'id':'id_Versement'}))
    Dette=forms.FloatField(widget=forms.TextInput(attrs={'id':'id_Dette','readonly':'readonly'}))
    prix_total=forms.FloatField(widget=forms.TextInput(attrs={'id':'id_Prix_total','readonly':'readonly'}))

    # On définit les métadonnées du formulaire
    class Meta:
        # On précise le modèle utilisé pour le formulaire
        model = Achat
        # On indique les champs du modèle qui seront présents dans le formulaire
        fields = ['fournisseur','date_achat','prix_total','produits_bruts','autre_produits','Versement','Dette','Versement_totalite','fichier']
        # On définit les widgets utilisés pour chaque champ du formulaire
        widgets = {
            'date_achat':AdminDateWidget() 
        }

# On crée une classe de formulaire pour le modèle Facture
class FactureForm(forms.ModelForm):
    class Meta:
        # On précise le modèle utilisé pour le formulaire
        model = Facture
        # On indique les champs du modèle qui seront présents dans le formulaire
        fields = ['fichier']
