from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    pass

class Genre(models.Model):
    name = models.CharField(max_length=20)

class Director(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    img_url = models.TextField()
    description = models.TextField()

class Actor(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    img_url = models.TextField()
    description = models.TextField()

class Movie(models.Model):
    title = models.CharField(max_length=140)
    title_en = models.CharField(max_length=140)
    rate = models.CharField(max_length=100)
    directors = models.ManyToManyField(Director, related_name='movies', blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies', blank=True)
    img_url = models.TextField()
    description = models.TextField()
    open_date = models.CharField(max_length=50)
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='movies', blank=True)

class Review(models.Model):
    content = models.CharField(max_length=40)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Worldcup(models.Model):
    movies = models.ManyToManyField(Movie, related_name='worldcups', through='Ranking', blank=True)

class Ranking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    worldcup = models.ForeignKey(Worldcup, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)