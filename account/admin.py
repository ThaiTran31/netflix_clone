from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Profile


class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 0


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "name",
        "age_limit",
    ]
    list_filter = [
        "age_limit",
    ]


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    inlines = [
        *UserAdmin.inlines,
        ProfileInline,
    ]
