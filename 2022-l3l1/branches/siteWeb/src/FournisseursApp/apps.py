from django.apps import AppConfig

# Configuration de l'application 'FournisseursApp'
class FournisseursappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Définit le champ par défaut pour les clés primaires
    name = 'FournisseursApp'  # Nom de l'application
