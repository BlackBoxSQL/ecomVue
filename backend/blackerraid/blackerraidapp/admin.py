from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import (
    CustomUser,
    Actor,
    Director,
    Genre,
    Movie
)


class CustomUserAdmin(UserAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)