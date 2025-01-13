from django import forms
from django.forms import ModelForm, inlineformset_factory

from ProduitApp.models import Cadre
from VenteApp.models import Commande, Article, ArticleCadre, ArticleAutre


class VenteForms(ModelForm):
    """
    Formulaire pour créer ou mettre à jour une commande.
    """

    class Meta:
        model = Commande
        fields = [ 'id', 'client','date_reception', 'statut','remise']

class ArticleForms(ModelForm):
    """
    Formulaire pour créer ou mettre à jour un article dans une commande.
    """
    class Meta:
        model = Article
        fields = ['produit', 'unite','quantite']

OrderItemFormset = inlineformset_factory(Commande, Article, form=ArticleForms)

class ArticleCadreForms(ModelForm):
    """
    Formulaire pour créer ou mettre à jour un article cadre dans une commande.
    """

    class Meta:
        model = ArticleCadre
        fields = ['cadre','quantite']

OrderCadreFormset = inlineformset_factory(Commande, ArticleCadre, form=ArticleCadreForms)

class ArticleAutreForms(ModelForm):
    """
    Formulaire pour créer ou mettre à jour un autre article dans une commande.
    """
    class Meta:
        model = ArticleAutre
        fields = ['produit','quantite']

OrderAutreFormset = inlineformset_factory(Commande, ArticleAutre, form=ArticleAutreForms)