from django import template

register = template.Library()

@register.filter
def get_quantite(quantites, autre_produit):
    return quantites.get(autre_produit.pk, 0)
@register.filter
def get_quantite_brut(quantites_brut, produits_brut):
    return quantites_brut.get(produits_brut.pk, 0)
@register.filter
def get_quantite_quintal(quantites_quintal, produits_brut):
    return quantites_quintal.get(produits_brut.pk, 0)
@register.filter
def get_quantite_bar(quantites_bar, produits_brut):
    return quantites_bar.get(produits_brut.pk, 0)