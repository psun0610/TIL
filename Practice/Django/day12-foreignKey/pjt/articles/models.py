from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()

class Comment(models.Model):
    content = models.CharField(max_length=80)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)