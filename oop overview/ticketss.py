from datetime import datetime

class Cinema:
    def __init__(self, name, location, num_screens):
        self.name = name
        self.location = location
        self.num_screens = num_screens
        self.screens = []

    def add_screen(self, screen):
        self.screens.append(screen)

    def get_screen_by_num(self, screen_num):  # sourcery skip: use-next
        for screen in self.screens:
            if screen.screen_num == screen_num:
                return screen
        return None

    def get_movies_on_screen(self, screen_num):
        # sourcery skip: use-named-expression
        screen = self.get_screen_by_num(screen_num)
        if screen:
            return [movie_showtime.movie for movie_showtime in screen.movie_showtimes]
        return []

class Screen:
    def __init__(self, screen_num, seating_capacity):
        self.screen_num = screen_num
        self.seating_capacity = seating_capacity
        self.movie_showtimes = []

    def add_movie_showtime(self, movie_showtime):
        self.movie_showtimes.append(movie_showtime)

    def get_available_seats(self, movie_showtime):
        taken_seats = [ticket.seat_num for ticket in movie_showtime.tickets]
        return [seat for seat in range(1, self.seating_capacity+1) if seat not in taken_seats]

class Movie:
    def __init__(self, title, genre, runtime, rating):
        self.title = title
        self.genre = genre
        self.runtime = runtime
        self.rating = rating

class Ticket:
    def __init__(self, ticket_num, seat_num, movie_showtime, customer):
        self.ticket_num = ticket_num
        self.seat_num = seat_num
        self.movie_showtime = movie_showtime
        self.customer = customer
        self.purchase_time = datetime.now()

    def cancel(self):
        self.customer.cancel_ticket(self)

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.tickets = []

    def purchase_ticket(self, ticket):
        self.tickets.append(ticket)

    def cancel_ticket(self, ticket):
        self.tickets.remove(ticket)

    def get_purchase_history(self):
        return [ticket.movie_showtime.movie.title for ticket in self.tickets]

class MovieShowtime:
    def __init__(self, movie, screening_time, screen):
        self.movie = movie
        self.screening_time = screening_time
        self.screen = screen
        self.tickets = []

    def get_available_seats(self):
        return self.screen.get_available_seats(self)

    def purchase_ticket(self, seat_num, customer):
        available_seats = self.get_available_seats()
        if seat_num not in available_seats:
            return None
        ticket_num = len(self.tickets) + 1
        ticket = Ticket(ticket_num, seat_num, self, customer)
        self.tickets.append(ticket)
        customer.purchase_ticket(ticket)
        return ticket



