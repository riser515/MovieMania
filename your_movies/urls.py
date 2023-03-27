from django.urls import path, re_path, include
from . import views


urlpatterns = [
    re_path(
        r'^movies/create_movie',
        views.post_movie,
        name='post_movie'
    ),
    re_path(
        r'^movies/(?P<pk_movie_id>[0-9]+)$',
        views.specific_movie,
        name='specific_movie'
    ),
    re_path(
        r'^movies/',
        views.all_movies,
        name='all_movies'
    ),
    re_path(
        r'^reviews/create_review',
        views.post_review,
        name='post_review'
    ),
    re_path(
        r'^reviews/getmovie/(?P<fk_movie_id>[0-9]+)$',
        views.review_movie,
        name='review_movie'
    ),
    re_path(
        r'^reviews/getreview/(?P<pk_review_id>[0-9]+)$',
        views.update_review,
        name='update_review'
    ),
    re_path(
        r'^reviews/',
        views.all_reviews,
        name='all_reviews'
    ),
]