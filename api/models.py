from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    tconst = models.TextField(null=True, blank=True)
    titleType = models.TextField(null=True, blank=True)
    primaryTitle = models.TextField(null=True, blank=True)
    originalTitle = models.TextField(null=True, blank=True)
    isAdult = models.TextField(null=True, blank=True)
    startYear = models.TextField(null=True, blank=True)
    endYear = models.TextField(null=True, blank=True)
    runtimeMinutes = models.TextField(null=True, blank=True)
    genres = models.TextField(null=True, blank=True)

class CustomList(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)
