from django.contrib import admin
from .models import Commande, Article, ArticleAutre, ArticleCadre
admin.site.register(Commande)
admin.site.register(Article)
admin.site.register(ArticleAutre)
admin.site.register(ArticleCadre)

# Register your models here.
