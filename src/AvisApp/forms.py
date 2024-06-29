from django import forms
from .models import Message, Avis


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['nom', 'email', 'message']


class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ['nom', 'commentaire', 'note']
        note = forms.ChoiceField(
            label='Note',
            choices=[(i, str(i)) for i in range(6)],  # Créer des choix de 0 à 5
            widget=forms.Select(attrs={'class': 'form-control'})  # Ajouter des classes CSS si nécessaire
        )
