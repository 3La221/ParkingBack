# Generated by Django 5.0.4 on 2024-05-02 08:30

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_park_cout_alter_park_datedebut_alter_park_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='dateDebut',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 2, 9, 30, 13, 226677)),
        ),
        migrations.AlterField(
            model_name='park',
            name='id',
            field=models.CharField(default=uuid.UUID('83d8649c-f9a8-428e-ac55-2f3843fadcad'), editable=False, max_length=8, primary_key=True, serialize=False),
        ),
    ]
