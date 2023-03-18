from hudai import Actor, Writer, Director, Movie, Ticket, Customer, Screen, Hall, Seat, Show

actors = []

def insert_actors():
    name = str(input("Actor Name > "))
    actors.append(Actor(name=name)) 
    show_actors()

def show_actors():
    total = len(actors)
    print("Total Actors: ", total)
    for actor in actors:
        print(actor, sep="\n", end=" ")

insert_actors()
show_actors()