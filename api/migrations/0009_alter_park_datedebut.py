# Generated by Django 5.0.4 on 2024-05-02 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_park_datedebut_alter_park_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='dateDebut',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 2, 9, 35, 58, 481680), unique=True),
        ),
    ]