# Generated by Django 5.0.4 on 2024-05-02 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_park_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parks', to='api.client'),
        ),
    ]
