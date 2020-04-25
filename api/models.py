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
    title = models.CharField(max_length=500)
    background = models.CharField(max_length=500)
    poster = models.CharField(max_length=500)
    release_date = models.CharField(max_length=500)
    director = models.CharField(max_length=500)
    cast = models.CharField(max_length=500)
    synopsis = models.CharField(max_length=500)


class Genre(models.Model):
    name = models.CharField(max_length=500)
    movies = models.ManyToManyField(Movie)
