from django.urls import path, re_path, include
from . import views


urlpatterns = [
    re_path(
        r'^api/v1/movies/',
        views.all_movies,
        name='all_movies'
    ),
    re_path(
        r'^api/v1/reviews/',
        views.all_reviews,
        name='all_reviews'
    ),
    re_path(
        r'^api/v1/movie/(?P<id>[0-9]+)$',
        views.single_movie,
        name='single_movie'
    ),
    re_path(
        r'^api/v1/review/(?P<id>[0-9]+)$',
        views.single_review,
        name='single_review'
    ),
    re_path(
        r'^api/v1/update_review/(?P<id>[0-9]+)$',
        views.update_review,
        name='update_review'
    ),
]