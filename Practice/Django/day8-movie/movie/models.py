from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20, null=True)
    summary = models.TextField(blank=True)
    running_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)