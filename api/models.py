from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_picture = models.CharField(max_length=500)
    pass


class Comment(models.Model):
    username = models.ForeignKey('api.User', on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=datetime.now())
    score = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=500, blank=True)
    background = models.CharField(max_length=500, blank=True)
    poster = models.CharField(max_length=500, blank=True)
    release_date = models.CharField(max_length=500, blank=True)
    director = models.CharField(max_length=500, blank=True)
    cast = models.CharField(max_length=500, blank=True)
    synopsis = models.CharField(max_length=500, blank=True)


class Genre(models.Model):
    name = models.CharField(max_length=500)
    movies = models.ManyToManyField(Movie)
