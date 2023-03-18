from datetime import date, time


class Actor:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Writer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Director:
    def __init__(self, name):

        self.name = name

    def __str__(self):
        return self.name


class Movie:
    def __init__(self, movie_name, actors, directors, writers, year):
        self.movie_name = movie_name
        self.actors = actors
        self.directors = directors
        self.writers = writers
        self.year = year

    def __str__(self):
        return self.movie_name, self.actors, self.directors, self.writers, self.year


class Ticket:
    def __init__(self, price, type, show_id):
        self.price = price
        self.type = type
        self.show_id = show_id

    def __str__(self):
        return self.price, self.type, self.show_id


class Customer:
    def __init__(self, name):

        self.name = name

    def __str__(self):
        return self.customer_name


class Screen:
    def __init__(self, name):

        self.name = name

    def __str__(self):
        return self.screen_name


class Hall:
    def __init__(self, name, seats, seat_count, screen_count, screens):

        self.name = name
        self.seat_count = seat_count
        self.seats = seats
        self.screen_count = screen_count
        self.screens = screens

    def __str__(self):
        return self.hall_name, self.seat_count, self.seats, self.screen_count, self.screens

    def seat_plan(self):
        for self.seat in self.seats:
            return self.seat


class Seat:
    def __init__(self, seat):
        self.seat = seat

    def __str__(self):
        return self.seat_no


class Show:
    def __init__(self, movie_id, start_time, end_time, date, hall_id, screen_id):
        self.movie_id = movie_id
        self.start_time = start_time
        self.end_time = end_time
        self.date = date
        self.hall_id = hall_id
        self.screen_id = screen_id

    def __str__(self):
        return self.movie_id, self.start_time, self.end_time, self.date, self.hall_id, self.screen_id
