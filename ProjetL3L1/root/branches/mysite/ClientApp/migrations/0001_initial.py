# Generated by Django 4.1.7 on 2023-02-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=40)),
                ('nom', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=15)),
                ('adresse', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=20)),
                ('piece_ID', models.FileField(upload_to='piece_ID')),
            ],
        ),
    ]
