# Generated by Django 3.2.13 on 2022-10-05 11:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='types',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, size=None),
        ),
    ]