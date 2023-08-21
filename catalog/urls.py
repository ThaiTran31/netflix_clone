from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="index"),
    path("movies/<uuid:profile_id>/", views.MovieList.as_view(), name="movie-list"),
    path("movie/<int:pk>/", views.MovieDetail.as_view(), name="movie-detail"),
    path("movie/watching/<uuid:pk>/", views.VideoShow.as_view(), name="video-detail"),
]
