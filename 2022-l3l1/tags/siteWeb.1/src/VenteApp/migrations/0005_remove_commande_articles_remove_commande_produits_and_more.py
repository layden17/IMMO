# Generated by Django 4.1.6 on 2023-03-13 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VenteApp', '0004_alter_article_commande_alter_article_unproduit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='articles',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='produits',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='produitsBruts',
        ),
    ]