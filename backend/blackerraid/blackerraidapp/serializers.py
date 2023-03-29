from rest_framework import serializers
from .models import Actor, CustomUser, Director, Genre, Hall, Movie, Rate, Show


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username",)


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ("id", "name",)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            "id",
            "name",
            "profile",
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name",)


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ("id", "name", "rate",)


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    directors = DirectorSerializer(many=True)
    rated = RateSerializer(many=False)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "directors",
            "genres",
            "release_date",
            "actors",
            "poster",
            "duration",
            "rated",
        )


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = (
            "id",
            "name",
            "location",
            "p_capacity",
            "r_capacity",
        )

class ShowSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=False)
    hall = HallSerializer(many=False)
    class Meta:
        model = Show
        fields = (
            "movie",
            "hall",
            "date",
            "start_time",
            "end_time",
        )