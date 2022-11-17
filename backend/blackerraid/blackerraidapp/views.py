from rest_framework import viewsets
from django.db.models import Max, F

from .models import Movie, InTheater, ShowSeat, Seat
from .serializers import (
    MovieSerializer,
    ComingSoonMovieSerializer,
    InTheaterSerializer,
    ShowSeatSerializer,
    SeatSerializer,
)
from datetime import date, timedelta
from django.http import HttpResponse


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ComingSoonViewSet(viewsets.ModelViewSet):
    start_date = date.today()
    end_date = start_date + timedelta(days=90)
    queryset = Movie.objects.filter(release__range=[start_date, end_date])
    serializer_class = ComingSoonMovieSerializer


class InTheaterMovieViewSet(viewsets.ModelViewSet):
    queryset = InTheater.objects.all()
    serializer_class = InTheaterSerializer


class ShowSeatSerializerViewSet(viewsets.ModelViewSet):
    queryset = ShowSeat.objects.all()
    serializer_class = ShowSeatSerializer


class SeatSerializerViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


def home(request):
    return HttpResponse("<h2> Hello world! </h2>")
