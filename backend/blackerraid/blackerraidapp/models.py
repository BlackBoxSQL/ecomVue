from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Actor(models.Model):
    name = models.CharField(max_length=150)
    profile = models.ImageField(upload_to="profiles")

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directors"

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    directors = models.ManyToManyField(Director)
    genres = models.ManyToManyField(Genre)
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor)
    poster = models.ImageField(
        upload_to="posters")

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title


