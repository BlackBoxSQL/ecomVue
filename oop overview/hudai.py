from datetime import date, time


class Actor:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.id, self.name


class Writer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.id, self.name


class Director:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.id, self.name


class Movie:
    def __init__(self, id, movie_name, actors, directors, writers, year):
        self.id = id
        self.movie_name = movie_name
        self.actors = actors
        self.directors = directors
        self.writers = writers
        self.year = year

    def __str__(self):
        return self.id, self.movie_name, self.actors, self.directors, self.writers, self.year


class Ticket:
    def __init__(self, id, price, type, show_id):
        self.id = id
        self.price = price
        self.type = type
        self.show_id = show_id

    def __str__(self):
        return self.id, self.price, self.type, self.show_id


class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.id, self.customer_name


class Screen:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.id, self.screen_name


class Hall:
    def __init__(self, id, hall_name, seats, seat_count, screen_count, screens):
        self.id = id
        self.hall_name = hall_name
        self.seat_count = seat_count
        self.seats = seats
        self.screen_count = screen_count
        self.screens = screens

    def __str__(self):
        return self.id, self.hall_name, self.seat_count, self.seats, self.screen_count, self.screens


class Seat:
    def __init__(self, id, seat):
        self.id = id
        self.seat = seat

    def __str__(self):
        return self.id, self.seat_no


class Show:
    def __init__(self, id, movie_id, start_time, end_time, date, hall_id, screen_id):
        self.id = id
        self.movie_id = movie_id
        self.start_time = start_time
        self.end_time = end_time
        self.date = date
        self.hall_id = hall_id
        self.screen_id = screen_id

    def __str__(self):
        return self.id, self.movie_id, self.start_time, self.end_time, self.date, self.hall_id, self.screen_id
