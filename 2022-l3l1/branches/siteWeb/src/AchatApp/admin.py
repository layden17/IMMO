# On importe la classe admin de Django et les modèles que l'on souhaite utiliser dans l'interface d'administration
from django.contrib import admin
from .models import Achat, Facture, ProduitBrutLiaison, AutreProduitLiaison
# On crée des classes Inline pour les modèles qui ont une relation ManyToMany avec Achat
class ProduitBrutinLine(admin.TabularInline):
    model=ProduitBrutLiaison
    extra=0

class AutreProduitinLine(admin.TabularInline):
    model=AutreProduitLiaison
    extra=0

# On crée une classe qui représente l'interface d'administration pour le modèle Achat
class Achatadmin(admin.ModelAdmin):
    # On ajoute les classes Inline pour les modèles liés à Achat
    inlines=[ProduitBrutinLine,AutreProduitinLine]
    
    class Meta:
        # On précise le modèle que l'on souhaite utiliser pour cette interface d'administration
        model=Achat

# On enregistre les modèles que l'on souhaite utiliser dans l'interface d'administration
admin.site.register(Achat,Achatadmin)
admin.site.register(Facture)
admin.site.register(ProduitBrutLiaison)
admin.site.register(AutreProduitLiaison)


