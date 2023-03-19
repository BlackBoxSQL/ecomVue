from datetime import date, time


class Actor:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


a1 = Actor(name='John')
a2 = Actor(name='Tom')
a3 = Actor(name='Carol')
a4 = Actor(name='Julia')
a5 = Actor(name='Brad')
a6 = Actor(name="Will")
a7 = Actor(name='Peter')
a8 = Actor(name='Linda')
a9 = Actor(name='Barbara')
a10 = Actor(name='Elizabeth')
a11 = Actor(name='Margaret')
a12 = Actor(name='Sue')
a13 = Actor(name='Betty')
a14 = Actor(name='Janet')
a15 = Actor(name='Carol')
a16 = Actor(name='Susan')
a17 = Actor(name='Margaret')
a18 = Actor(name='Sue')


class Writer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


w1 = Writer(name="Kamal")
w2 = Writer(name="John")
w3 = Writer(name="Carol")
w4 = Writer(name="Sue")
w5 = Writer(name="Margaret")
w6 = Writer(name="Susan")


class Director:
    def __init__(self, name):

        self.name = name

    def __str__(self):
        return self.name


d1 = Director(name="John")
d2 = Director(name="Carol")
d3 = Director(name="Sue")
d4 = Director(name="Margaret")


class Movie:
    def __init__(self, movie_name, actors, directors, writers, year):
        self.movie_name = movie_name
        self.actors = actors
        self.directors = directors
        self.writers = writers
        self.year = year

    def __str__(self):
        return self.movie_name, self.actors, self.directors, self.writers, self.year


m1 = Movie(movie_name="The Matrix",
           actors=[a1.name, a2.name, a3.name, a4.name, a5.name, a18.name],
           directors=[d2.name],
           writers=[w2.name],
           year=2020
           )


m2 = Movie(movie_name="The Lodge",
           actors=[a3.name, a4.name, a8.name, a17.name, a18.name],
           directors=[d3.name, d4.name],
           writers=[w4.name],
           year=2021
           )


class Customer:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __str__(self):
        return self.name, self.money


c1 = Customer(name="John", money=20)
c2 = Customer(name="Carol", money=120)
c3 = Customer(name="Sue", money=240)

customers = [c1, c2, c3]


class Screen:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


sc1 = Screen(name="Big")
sc2 = Screen(name="Small")


class Seat:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return self.type


seat1 = Seat(type="Premium")
seat2 = Seat(type="Regular")


class Hall:
    def __init__(self, name, seats, seat_count, screen_count, screens):
        self.name = name
        self.seat_count = seat_count
        self.seats = seats
        self.screen_count = screen_count
        self.screens = screens

    def __str__(self):
        return self.name, self.seat_count, self.seats, self.screen_count, self.screens


h1 = Hall(name="Pallabi",
          seat_count=14,
          seats=[
              seat1.type,
              seat1.type,
              seat1.type,
              seat1.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type
          ],
          screen_count=1,
          screens=[sc1.name])


h2 = Hall(name="Balaka",
          seat_count=20,
          seats=[
              seat1.type,
              seat1.type,
              seat1.type,
              seat1.type,
              seat1.type,
              seat1.type,
              seat1.type,
              seat1.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type,
              seat2.type
          ],
          screen_count=2,
          screens=[sc1.name, sc1.name])


class Show:
    def __init__(self, movie, start_time, end_time, date, hall, screen):
        self.movie = movie
        self.start_time = start_time
        self.end_time = end_time
        self.date = date
        self.hall = hall
        self.screen = screen

    def __str__(self):
        return self.movie_id, self.start_time, self.end_time, self.date, self.hall_id, self.screen_id


sh1 = Show(
    movie=m1.movie_name,
    start_time=time(hour=9, minute=30),
    end_time=time(hour=10, minute=30),
    date=date(year=2020, month=1, day=1),
    hall=h1.name,
    screen=h1.screens
)

print(sh1.movie, sh1.start_time, sh1.end_time, sh1.date, sh1.hall, sh1.screen)



