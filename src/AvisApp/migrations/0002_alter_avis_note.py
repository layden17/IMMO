# Generated by Django 4.0.3 on 2023-08-18 09:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AvisApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avis',
            name='note',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
