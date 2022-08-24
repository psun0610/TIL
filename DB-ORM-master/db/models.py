from django.db import models

# class Genre(models.Model):
#     name = models.CharField(max_length = 30)

class Director(models.Model):
    name = models.TextField(default='default_name')
    debut = models.DateTimeField(default='2022-08-24')
    country = models.TextField(default='default_country')

class Genre(models.Model):
    title = models.TextField(default='default_title')