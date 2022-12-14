from django.db import models
import datetime
# Create your models here.

class Song(models.Model):

    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField(default=datetime.date.today)
    genre = models.CharField(max_length=255)
    likes = models.IntegerField(default = 0)
    link = models.CharField(max_length=3000, default = '')
    img = models.CharField(max_length=3000, default = '')
