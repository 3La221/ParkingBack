# Generated by Django 5.0.4 on 2024-05-02 10:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_park_voiture_alter_park_datedebut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='dateDebut',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
