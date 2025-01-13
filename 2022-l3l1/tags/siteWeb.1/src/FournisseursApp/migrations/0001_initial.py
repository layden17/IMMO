# Generated by Django 4.1.7 on 2023-03-12 14:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Raison_social', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('Numero_Telephone', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('Fax', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('Versement', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Dette', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
