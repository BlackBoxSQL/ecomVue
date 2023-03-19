from rest_framework import viewsets
from .models import Movie
from .serializers import (
    CustomUserSerializer,
    MovieSerializer,
)
from datetime import date, timedelta
from django.http import HttpResponse


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# class ComingSoonViewSet(viewsets.ModelViewSet):
#     start_date = date.today()
#     end_date = start_date + timedelta(days=90)
#     queryset = Movie.objects.filter(release_date__range=[start_date, end_date])
#     serializer_class = MovieSerializer


def home(request):
    return HttpResponse("<h2> Hello world! </h2>")
