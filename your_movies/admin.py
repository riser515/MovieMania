from django.contrib import admin
from ..models import User, Movie, Review

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Review)