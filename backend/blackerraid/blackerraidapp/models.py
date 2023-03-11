from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class CommonInfo(models.Model):
    GENDER_CHOICES = (
        ("male", "male"),
        ("female", "female"),
    )
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
    )
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now_add=False, auto_now=False)
    profile_image = models.ImageField(upload_to="media/profile_image")
    bio = models.TextField()

    class Meta:
        verbose_name = "CommonInfo"
        verbose_name_plural = "CommonInfos"

    def __str__(self):
        return f"{self.name}"


class Filmography(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Filmography"
        verbose_name_plural = "Filmography"

    def __str__(self):
        return f"{self.name}"


class Director(CommonInfo):
    directcs = models.ManyToManyField(
        Filmography
    )

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directors"

    def __str__(self):
        return f"{self.name}"


class Genre(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return f"{self.name}"


class Actor(CommonInfo):
    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"

    def __str__(self):
        return f"{self.name}"


class Rating(models.Model):
    image = models.ImageField(upload_to="media/rating")

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    def __str__(self):
        return f"{self.image}"


class Movie(models.Model):
    name = models.CharField(max_length=100)
    release = models.DateField(auto_now_add=False, auto_now=False)
    poster = models.ImageField(upload_to="media/thumbnail")
    duration = models.IntegerField()
    genres = models.ManyToManyField(
        Genre,
    )
    actors = models.ManyToManyField(
        Actor,
    )
    director = models.ManyToManyField(
        Director,
    )
    ratings = models.ManyToManyField(
        Rating,
    )

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"{self.name}"


class District(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"

    def __str__(self):
        return f"{self.name}"


class Theater(models.Model):
    name = models.CharField(max_length=80)
    location = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    total_seat = models.IntegerField()

    class Meta:
        verbose_name = "Theater"
        verbose_name_plural = "Theaters"

    def __str__(self):
        return f"{self.name}"


class Seat(models.Model):
    SEAT_TYPE = (
        ("Premium", "Premium"),
        ("Regular", "Regular"),
    )

    seat_no = models.IntegerField()
    seat_type = models.CharField(choices=SEAT_TYPE, max_length=7)
    theater = models.ForeignKey(Theater, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Seat"
        verbose_name_plural = "Seats"
        unique_together = (
            "seat_no",
            "seat_type",
            "theater",
        )

    def __str__(self):
        return f"{self.seat_no} - {self.seat_type} - {self.theater}"


class InTheater(models.Model):
    name = models.ForeignKey(Movie, default="", on_delete=models.DO_NOTHING)
    theater = models.ForeignKey(
        Theater, default="", on_delete=models.DO_NOTHING)
    show_date = models.DateField(auto_now_add=False, auto_now=False)
    show_time = models.TimeField(auto_now_add=False, auto_now=False)

    class Meta:
        verbose_name = "InTheater"
        verbose_name_plural = "InTheaters"

    def __str__(self):
        return f"{self.theater} - {self.name} - {self.show_date} - {self.show_time}"


class Booking(models.Model):
    number_of_seats = models.IntegerField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    booked = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, default="",
                             on_delete=models.DO_NOTHING)
    show = models.ForeignKey(InTheater, default="",
                             on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        unique_together = (
            "number_of_seats",
            "time_stamp",
            "booked",
            "user",
            "show",
        )

    def __str__(self):
        return (
            f"{self.number_of_seats} - {self.time_stamp} - {self.booked} - {self.show}"
        )


class ShowSeat(models.Model):
    price = models.IntegerField()
    seat = models.ForeignKey(
        Seat, default="", on_delete=models.DO_NOTHING, related_name="show_seat_seat"
    )
    intheater = models.ForeignKey(
        InTheater, default="", on_delete=models.DO_NOTHING)
    booking = models.ForeignKey(
        Booking, default="", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "ShowSeat"
        verbose_name_plural = "ShowSeats"
        unique_together = (
            "price",
            "seat",
            "intheater",
            "booking",
        )

    def __str__(self):
        return f"{self.booking.user.username} - {self.price} - {self.seat} - {self.intheater.name}"


class Payment(models.Model):
    amount = models.IntegerField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=80)
    payment_method = models.CharField(max_length=80)
    booking = models.ForeignKey(
        Booking, default="", on_delete=models.DO_NOTHING
    )

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return f"{self.amount} - {self.time_stamp} - {self.transactionId} - {self.payment_method} - {self.booking}"
