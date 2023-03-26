from django.urls import path, re_path, include
from . import views


urlpatterns = [
    re_path(
        r'^api/v1/movies/',
        views.all_movies,
        name='all_movies'
    ),
    re_path(
        r'^api/v1/movie/(?P<id>[0-9]+)$',
        views.single_movie,
        name='single_movie'
    ),
]