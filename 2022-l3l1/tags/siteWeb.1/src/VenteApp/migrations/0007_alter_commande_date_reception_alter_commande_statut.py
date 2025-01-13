# Generated by Django 4.1.6 on 2023-03-14 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VenteApp', '0006_alter_commande_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='date_reception',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='statut',
            field=models.CharField(choices=[('1', 'En attente'), ('2', 'Livré')], max_length=200, null=True, verbose_name='Statut'),
        ),
    ]
