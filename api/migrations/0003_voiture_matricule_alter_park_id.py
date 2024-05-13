# Generated by Django 5.0.4 on 2024-05-01 14:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_client_voiture_alter_park_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='voiture',
            name='matricule',
            field=models.CharField(default=2, max_length=12, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='park',
            name='id',
            field=models.CharField(default=uuid.UUID('a48bdaa4-2908-4d27-8d25-405682374054'), editable=False, max_length=8, primary_key=True, serialize=False),
        ),
    ]