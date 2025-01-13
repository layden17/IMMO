from django import forms
from .models import Achat
from django.forms import ModelForm


class AchatForm(ModelForm):
    class Meta:
        model = Achat
        fields = '__all__'