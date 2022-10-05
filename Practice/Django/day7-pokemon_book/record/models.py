from distutils.command.upload import upload
from django.db import models
from django.contrib.postgres.fields import ArrayField  

# Create your models here.
class Pokemon(models.Model):
    number = models.IntegerField(default=-1)
    name = models.CharField(max_length=20)
    # types = ArrayField(models.TextField(blank=False), blank=True)
    types = models.TextField(blank=False)
    image = models.ImageField(upload_to = 'images/', null=True, blank=True)

    # admin 모드에서 제목으로 파일 구분할 수 있게 함
    def __str__(self):
        return str(self.name)