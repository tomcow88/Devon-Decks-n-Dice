from django.db import models

# Create your models here.

STATUS = ((0, "Unavailable"), (1, "Available"))

class BoardGame(models.Model):
    name = models.CharField(max_length=200, unique=True)
    bgg_id = models.IntegerField(unique=True)
    year_published = models.IntegerField()
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    playing_time = models.IntegerField()
    age = models.IntegerField()
    image = models.URLField(unique=True)
    thumbnail = models.URLField(unique=True)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
