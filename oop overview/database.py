from hudai import Actor, Actor, Writer, Director, Movie, Ticket, Customer, Screen, Hall, Seat, Show

actors = [
    Actor(id=1, name='Mila Kunis'),
    Actor(id=2, name='Tom Cruize'),
    Actor(id=3, name='Michael Kunis'),
    Actor(id=4, name='Mike Blue'),
    Actor(id=5, name='Mike Green'),
    Actor(id=6, name='Mike Red'),
    Actor(id=7, name='Mike White'),
    Actor(id=8, name='Mike Yellow'),
    Actor(id=9, name='Mike Blue'),
]

for actor in actors:
    print(actor.id, actor.name)

writers = [
    Writer(id=1, name='Mila Kunis'),
    Writer(id=2, name='Tom Cruize'),
    Writer(id=3, name='Michael Kunis'),
    Writer(id=4, name='Mike Blue'),
    Writer(id=5, name='Mike Green'),
]

for writer in writers:
    print(writer.id, writer.name)

directors = [
    Director(id=1, name='Mila Kunis'),
    Director(id=2, name='Tom Cruize'),
    Director(id=3, name='Michael Kunis'),
    Director(id=4, name='Mike Blue'),
    Director(id=5, name='Mike Green'),
]

for director in directors:
    print(director.id, director.name)


customers = [
    Customer(id=1, name='Mila Kunis'),
    Customer(id=2, name='Tom Cruize'),
    Customer(id=3, name='Michael Kunis'),
    Customer(id=4, name='Mike Blue'),
    Customer(id=5, name='Mike Green'),
]

for customer in customers:
    print(customer.id, customer.name)

screens = [
    Screen(id=1, name='DivX 4'),
    Screen(id=2, name='4k'),
    Screen(id=3, name='IMAX'),
    Screen(id=4, name='3D'),
    Screen(id=5, name='1080 P')
]

for screen in screens:
    print(screen.id, screen.name)

seats = [
    Seat(id=1, seat=[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                     [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                     [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]])
]
