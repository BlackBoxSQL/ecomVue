class MovieTheater:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.ticket_counter = TicketCounter()

    def list_movies(self):
        self.ticket_counter.list_movies()

    def purchase_ticket(self, movie, customer):
        self.ticket_counter.purchase_ticket(movie, customer)

class TicketCounter:
    def __init__(self):
        self.movies = []
        self.tickets_sold = {}

    def add_movie(self, movie):
        self.movies.append(movie)

    def list_movies(self):
        print("Available movies:")
        for movie in self.movies:
            print(movie.title)

    def purchase_ticket(self, movie, customer):
        if movie in self.movies:
            if movie.title not in self.tickets_sold:
                self.tickets_sold[movie.title] = 1
            else:
                self.tickets_sold[movie.title] += 1
            print(f"Ticket purchased for {movie.title} by {customer}")
        else:
            print("Movie not found.")

class Movie:
    def __init__(self, title, genre, release_year):
        self.title = title
        self.genre = genre
        self.release_year = release_year

class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
