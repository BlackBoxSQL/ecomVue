class Screen:
    def __init__(self, screen_number, seat_capacity):
        self.screen_number = screen_number
        self.seat_capacity = seat_capacity
        self.movie_showtimes = []
        self.booked_seats = set()

    def add_movie_showtime(self, movie_showtime):
        self.movie_showtimes.append(movie_showtime)

    def get_booked_seats(self, showtime):  # sourcery skip: assign-if-exp
        if showtime in self.movie_showtimes:
            return showtime.booked_seats
        else:
            return set()

    def get_available_seats(self, showtime):
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        if showtime in self.movie_showtimes:
            booked_seats = showtime.booked_seats
            return self.seat_capacity - len(booked_seats)
        else:
            return self.seat_capacity


class MovieShowtime:
    def __init__(self, movie, screening_time, screen):
        self.movie = movie
        self.screening_time = screening_time
        self.screen = screen
        self.available_seats = screen.seat_capacity
        self.booked_seats = set()

    def buy_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            self.booked_seats.update(set(range(self.screen.seat_capacity - self.available_seats,
                                     self.screen.seat_capacity - self.available_seats + num_tickets)))
            print(
                f"You have successfully purchased {num_tickets} tickets for {self.movie.title} on {self.screening_time}")
        else:
            print(
                f"Sorry, there are only {self.available_seats} seats available for {self.movie.title} on {self.screening_time}.")

    def get_booked_seats(self):
        return self.booked_seats

    def get_available_seats(self):
        return self.available_seats





'''
We need to define the following models for our ticket hub:

Cinema: Represents a cinema that screens movies.
Movie: Represents a movie that can be screened in a cinema.
Screening: Represents a screening of a movie in a cinema at a particular time.
Ticket: Represents a ticket for a particular screening.
Here's what the models might look like:

'''

# tickets/models.py

from django.db import models

class Cinema(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Screening(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

    def __str__(self):
        return f'{self.movie.title} at {self.cinema.name}'

class Ticket(models.Model):
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f'Ticket for {self.screening.movie.title} at {self.screening.cinema.name}'