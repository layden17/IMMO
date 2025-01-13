# Generated by Django 4.1.6 on 2023-03-01 14:26

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClientApp', '0004_alter_client_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='dette',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10),
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='client',
            name='type',
            field=models.CharField(choices=[('Particulier', 'Particulier'), ('Professionnel', 'Professionel')], max_length=200, null=True),
        ),
    ]
