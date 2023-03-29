class Screen:
    def __init__(self, screen_num, seat_capacity):
        self.screen_num = screen_num
        self.seat_capacity = seat_capacity
        self.movie_showtimes = []

    def add_movie_showtime(self, movie_showtime):
        self.movie_showtimes.append(movie_showtime)

    def get_movie_schedule(self):
        return self.movie_showtimes


class Cinema:
    def __init__(self, name, location, num_screens):
        self.name = name
        self.location = location
        self.num_screens = num_screens
        self.screens = []

    def add_screen(self, screen):
        self.screens.append(screen)

    def get_movie_schedule(self):
        movie_showtimes = []
        for screen in self.screens:
            movie_showtimes.extend(screen.get_movie_schedule())
        return movie_showtimes

    def get_screen_movie_schedule(self, screen_num):  # sourcery skip: use-next
        for screen in self.screens:
            if screen.screen_num == screen_num:
                return screen.get_movie_schedule()
        return []


class MovieShowtime:
    def __init__(self, movie, screening_time, screen):
        self.movie = movie
        self.screening_time = screening_time
        self.screen = screen
        self.available_seats = screen.seat_capacity

    def buy_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            print(
                f"You have successfully purchased {num_tickets} tickets for {self.movie.title} on {self.screening_time}")
        else:
            print(
                f"Sorry, there are only {self.available_seats} seats available for {self.movie.title} on {self.screening_time}.")
