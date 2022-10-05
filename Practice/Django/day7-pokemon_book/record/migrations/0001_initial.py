# Generated by Django 4.0.6 on 2022-10-05 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=-1)),
                ('name', models.CharField(max_length=20)),
                ('types', models.TextField()),
            ],
        ),
    ]
