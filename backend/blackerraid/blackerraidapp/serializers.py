from rest_framework import serializers

from .models import (Actor, CustomUser, Director,  Genre, Movie)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username",)


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ("name",)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            "name",
            "profile",
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name",)


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    directors = DirectorSerializer(many=True)

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
        )


# class ComingSoonMovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ("poster_avatar", "poster",)
