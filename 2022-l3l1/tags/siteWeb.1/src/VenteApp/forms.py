from django import forms
from django.forms import ModelForm, inlineformset_factory

from ProduitApp.models import Cadre
from VenteApp.models import Commande, Article, ArticleCadre


class VenteForms(ModelForm):
    class Meta:
        model = Commande
        fields = [ 'id', 'client','date_reception', 'statut','remise']

class ArticleForms(ModelForm):
    class Meta:
        model = Article
        fields = ['unProduit', 'quantite']

OrderItemFormset = inlineformset_factory(Commande, Article, form=ArticleForms)

class ArticleCadreForms(ModelForm):
    class Meta:
        model = ArticleCadre
        fields = ['cadre', 'quantite']

OrderCadreFormset = inlineformset_factory(Commande, ArticleCadre, form=ArticleCadreForms)