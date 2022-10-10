from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

class Song(models.Model):
    title = models.CharField(max_length=50)
    date_relaesed = models.DateTimeField()
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

class Lyrics(models.Model):
    content = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)