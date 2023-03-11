from rest_framework import serializers

from .models import (Actor, Booking, CustomUser, Director, District, Genre,
                     InTheater, Movie, Seat, ShowSeat, Theater, Rating)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username",)


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ("name",)


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ("name",)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            "name",
            "profile_image",
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name",)

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("image",)

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    director = DirectorSerializer(many=True)
    ratings = RatingSerializer(many=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "name",
            "release",
            "poster",
            "duration",
            "genres",
            "actors",
            "director",
            "ratings",
        )


class ComingSoonMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("poster",)


class TheaterSerializer(serializers.ModelSerializer):
    location = DistrictSerializer()

    class Meta:
        model = Theater
        fields = (
            "name",
            "location",
            "total_seat",
        )


class InTheaterSerializer(serializers.ModelSerializer):
    name = MovieSerializer()
    theater = TheaterSerializer()

    class Meta:
        model = InTheater
        fields = (
            "name",
            "theater",
            "show_date",
            "show_time",
        )


class SeatSerializer(serializers.ModelSerializer):
    theater = TheaterSerializer()

    class Meta:
        model = Seat
        fields = (
            "seat_no",
            "seat_type",
            "theater",
        )


class BookingSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    show = InTheaterSerializer()

    class Meta:
        model = Booking
        fields = (
            "number_of_seats",
            "time_stamp",
            "booked",
            "user",
            "show",
        )


class ShowSeatSerializer(serializers.ModelSerializer):
    seat = SeatSerializer()
    intheater = InTheaterSerializer()
    booking = BookingSerializer()

    class Meta:
        model = ShowSeat
        fields = (
            "price",
            "seat",
            "intheater",
            "booking",
        )
