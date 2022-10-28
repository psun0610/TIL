from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True)
    thumbnail = ProcessedImageField(upload_to='images/', blank=True, processors=[ResizeToFill(30, 30)], format='png', options={'quality': 80})
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likeuser")


class Comment(models.Model):
    content = models.CharField(max_length=80)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

