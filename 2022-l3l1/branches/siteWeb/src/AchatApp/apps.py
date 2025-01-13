# On importe la classe AppConfig de Django
from django.apps import AppConfig

# On crée une classe de configuration pour l'application AchatApp
class AchatappConfig(AppConfig):
    # On définit deux attributs pour la classe de configuration
    default_auto_field = 'django.db.models.BigAutoField'  # Spécifie le champ auto-incrémenté à utiliser pour les nouveaux modèles créés
    name = 'AchatApp'  # Spécifie le nom de l'application
