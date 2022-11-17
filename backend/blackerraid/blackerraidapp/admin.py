from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import (
    CustomUser,
    Actor,
    Director,
    Genre,
    Movie,
    District,
    Theater,
    InTheater,
    Booking,
    ShowSeat,
    Payment,
    Seat,
)


class CustomUserAdmin(UserAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(District)
admin.site.register(Theater)
admin.site.register(InTheater)
admin.site.register(Booking)
admin.site.register(ShowSeat)
admin.site.register(Payment)
admin.site.register(Seat)