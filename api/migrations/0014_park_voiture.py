# Generated by Django 5.0.4 on 2024-05-02 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_park_datedebut'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='voiture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parks', to='api.voiture'),
        ),
    ]
