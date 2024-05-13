# Generated by Django 5.0.4 on 2024-05-02 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_park_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='voiture',
            name='model',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='voiture',
            name='numero_type',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='matricule',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
