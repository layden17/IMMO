from django import forms
from .models import Categorie, ProduitBrut, Cadre, AutreProduit, Produit
from django.forms import ModelForm
from django.core.validators import MinValueValidator


class CategorieForm(forms.ModelForm):
    """
    Classe de formulaire Django pour créer et valider des instances de modèle Categorie.
    Utilise la classe ModelForm de Django pour générer automatiquement les champs du formulaire
    à partir des champs du modèle Categorie.

    Attributes:
        model (Categorie): Modèle Django à utiliser pour le formulaire.
        fields (list[str]): Liste des champs à inclure dans le formulaire.

    """
    class Meta:
        """
        Classe interne utilisée par Django pour configurer le formulaire.
        Définit les options du formulaire, telles que le modèle à utiliser et les champs à inclure.

        Attributes:
            model (Categorie): Modèle Django à utiliser pour le formulaire.
            fields (list[str]): Liste des champs à inclure dans le formulaire.

        """
        model = Categorie
        fields = ['name']


class CadreForms(ModelForm):
    """
    Classe de formulaire Django pour créer et valider des instances de modèle Cadre.
    Utilise la classe ModelForm de Django pour générer automatiquement les champs du formulaire
    à partir des champs du modèle Cadre.

    Attributes:
        model (Cadre): Modèle Django à utiliser pour le formulaire.
        fields (list[str]): Liste des champs à inclure dans le formulaire.

    """
    class Meta:
        """
        Classe interne utilisée par Django pour configurer le formulaire.
        Définit les options du formulaire, telles que le modèle à utiliser et les champs à inclure.

        Attributes:
            model (Cadre): Modèle Django à utiliser pour le formulaire.
            fields (list[str]): Liste des champs à inclure dans le formulaire.
            article_choix (forms.ModelMultipleChoiceField): Champ multiple pour choisir les ProduitBrut liés.

        """
        model = Cadre
        fields = ['cadre_choix','article_choix','longueur','largeur','crochet','prix_service','chute',
                  'consommation_sans_chute','consommation','crochet_opti','chute_valeur','max','prix']
        article_choix = forms.ModelMultipleChoiceField(queryset=ProduitBrut.objects.all(),
                                                       widget=forms.SelectMultiple(attrs={'id':'id_produit_brut'}))







class AutreProduitForm(forms.ModelForm):

    """
    Classe de formulaire Django pour créer et valider des instances de modèle AutreProduit.
    Utilise la classe ModelForm de Django pour générer automatiquement les champs du formulaire
    à partir des champs du modèle AutreProduit.


    Attributes:
        model (AutreProduit): Modèle Django à utiliser pour le formulaire.
        fields (list[str] or str): Liste des champs à inclure dans le formulaire, ou '__all__' pour tous les champs.

    """

    class Meta:
        """
        Classe interne utilisée par Django pour configurer le formulaire.
        Définit les options du formulaire, telles que le modèle à utiliser et les champs à inclure.

        Attributes:
            model (AutreProduit): Modèle Django à utiliser pour le formulaire.
            fields (list[str] or str): Liste des champs à inclure dans le formulaire, ou '__all__' pour tous les champs.

        """

        
        prix_achat = forms.DecimalField(validators=[MinValueValidator(0)])
        prix_vente = forms.DecimalField(validators=[MinValueValidator(0)])
        quantite = forms.DecimalField(validators=[MinValueValidator(0)])

        model = AutreProduit
        exclude = ['prix']

    categorie = forms.ModelChoiceField(
        queryset=Categorie.objects.exclude(name__in=['produit brut', 'cadre']),
        required=True
    )



class ProduitBrutForm(forms.ModelForm):
    class Meta:
        model = ProduitBrut
        exclude = ['categorie']
        description= forms.CharField(required=False)
