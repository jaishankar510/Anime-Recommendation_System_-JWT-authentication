# api/models.py

from django.db import models
from django.contrib.auth.models import User

class Anime(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_genre = models.CharField(max_length=255, blank=True, null=True)
    watched_anime = models.ManyToManyField(Anime)

    def __str__(self):
        return f"{self.user.username}'s Preferences"
