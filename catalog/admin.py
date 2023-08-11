from django.contrib import admin

from .models import Star, Director, Movie, Video, Genre


admin.site.register(Genre)


class VideoInline(admin.TabularInline):
    model = Video
    extra = 0


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
    ]


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
    ]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "movie",
        "file",
    ]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "display_director",
        "display_star",
        "display_genre",
        "type",
        "age_limit",
        "created_at"
    ]
    list_filter = [
        "type",
        "age_limit",
        "created_at",
    ]
    fieldsets = [
        (
            "General Information",
            {
                "fields": [
                    "title",
                    (
                        "director",
                        "star"
                    ),
                    "description",
                ],
            },
        ),
        (
            "Classification",
            {
                "fields": [
                    "genre",
                    "type",
                    "age_limit",
                ],
            },
        ),
        (
            "Media Information",
            {
                "fields": [
                    "image",
                ],
            },
        ),
        (
            "Additional Information",
            {
                "fields": [
                ],
            },
        ),
    ]
    inlines = [VideoInline, ]
