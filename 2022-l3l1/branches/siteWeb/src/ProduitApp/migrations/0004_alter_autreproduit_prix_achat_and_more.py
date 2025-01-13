# Generated by Django 4.1.6 on 2023-04-04 08:24

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProduitApp', '0003_remove_autreproduit_prix_vente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autreproduit',
            name='prix_achat',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='autreproduit',
            name='quantite',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.0'))]),
        ),
    ]
