# Generated by Django 4.1.6 on 2023-03-10 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProduitApp', '0003_produit_prix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='prix',
        ),
    ]
