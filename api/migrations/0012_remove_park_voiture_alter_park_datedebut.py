# Generated by Django 5.0.4 on 2024-05-02 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_park_datedebut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='park',
            name='voiture',
        ),
        migrations.AlterField(
            model_name='park',
            name='dateDebut',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 2, 10, 1, 46, 493407, tzinfo=datetime.timezone.utc)),
        ),
    ]
