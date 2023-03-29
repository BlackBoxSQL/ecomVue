from rest_framework import viewsets
from .models import Movie, Show
from .serializers import (
    CustomUserSerializer,
    MovieSerializer,
    ShowSerializer
)
from datetime import date, timedelta
from django.http import HttpResponse
from rest_framework import generics

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ComingSoonViewSet(viewsets.ModelViewSet):
    start_date = date.today()
    end_date = start_date + timedelta(days=90)
    queryset = Movie.objects.filter(release_date__range=[start_date, end_date])
    serializer_class = MovieSerializer


class MovieShowCase(viewsets.ModelViewSet):
    pass


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


def home(request):
    return HttpResponse("<h2> Hello world! </h2>")
