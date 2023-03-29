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
    
    @property
    def acted(self):
        return Movie.objects.filter(actors=self)


class Director(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directors"

    def __str__(self):
        return self.name
    
    @property
    def directed(self):
        return Movie.objects.filter(directors=self)


class Genre(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name
    
    @property
    def moviesInThisGenre(self):
        return Movie.objects.filter(genres=self)


class Rate(models.Model):
    name = models.CharField(max_length=100)
    rate = models.ImageField(upload_to='rates')

    class Meta:
        verbose_name = "Rate"
        verbose_name_plural = "Rates"

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
    duration = models.PositiveIntegerField()
    rated = models.ForeignKey(Rate, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title
      
class Cinema(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    capacity = models.PositiveIntegerField()
    class Meta:
        verbose_name = "Cinema"
        verbose_name_plural = "Cinemas"

    def __str__(self):
        return self.name
    

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()

    class Meta:
        verbose_name = "Show"
        verbose_name_plural = "Shows"

    def __str__(self):
        return f"{self.movie.title} - {self.hall.name} - {self.date} - {self.start_time} - {self.end_time}"
    

class Ticket(models.Model):
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    purchase_time = models.DateTimeField(auto_now_add=True)
    customer  = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
