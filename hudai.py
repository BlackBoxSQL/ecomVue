from datetime import date

class Ticket:
    def __init__(self, id, no, price, type, date, movie_id):
        self.id = id
        self.no = no
        self.price = price
        self.type = type
        self.date_range = date
        self.movie_id = movie_id



class Customer:
    def __init__(self, customer_name, paid, ticket_count, ticket_type):
        self.customer_name = customer_name
        self.paid = paid
        self.ticket_count = ticket_count
        self.ticket_type = ticket_type



ticket = []
ticket.append(Ticket(1, 456, 45.7, "premium", date(2022, 6, 10)))
