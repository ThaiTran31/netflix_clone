import uuid

from django.db import models


class Star(models.Model):
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        unique_together = ("first_name", "last_name")


class Director(models.Model):
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        unique_together = ("first_name", "last_name")


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    genre = models.ManyToManyField(Genre)
    director = models.ManyToManyField(Director)
    star = models.ManyToManyField(Star)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="covers", null=True, blank=True)
    MOVIE_TYPE_CHOICES = [
        ("f", "Feature"),
        ("s", "Series"),
    ]
    type = models.CharField(choices=MOVIE_TYPE_CHOICES, max_length=1)
    AGE_CHOICES = [
        ("all", "All"),
        ("kids", "Kids"),
    ]
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)

    def display_genre(self):
        return ", ".join([genre.name for genre in self.genre.all()[:3]])
    display_genre.short_description = "Genre"

    def display_director(self):
        return ", ".join([str(director) for director in self.director.all()[:2]])
    display_director.short_description = "Director"

    def display_star(self):
        return ", ".join([str(star) for star in self.star.all()[:2]])
    display_star.short_description = "Star"

    def __str__(self):
        return self.title


class Video(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID for this particular video across whole system"
    )
    title = models.CharField(max_length=100, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    file = models.FileField(upload_to="movie_videos", null=True, blank=True)

    def __str__(self):
        return self.title
