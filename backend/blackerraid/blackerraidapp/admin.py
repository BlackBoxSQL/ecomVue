from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    CustomUser,
    Actor,
    Director,
    Genre,
    Movie,
    Rate, 
    Show,
    Hall
)

class CustomUserAdmin(UserAdmin):
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Rate)
admin.site.register(Show)
admin.site.register(Hall)
