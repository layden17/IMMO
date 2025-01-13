from django import forms
from django.urls import reverse
from django.utils.safestring import mark_safe

class PrixQuintalHistoriqueWidget(forms.widgets.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        historique_url = reverse('historique_prix_quintal')
        icon_url = "https://www.flaticon.com/fr/icones-gratuites/en-attente"
        icon_html = f'<a href="{historique_url}"><img src="{icon_url}"></a>'
        return mark_safe(f'{html}{icon_html}')
   