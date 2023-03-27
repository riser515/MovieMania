from django.contrib import admin
from .models import UserInfo, Movie, Review

admin.site.register(UserInfo)
admin.site.register(Movie)
admin.site.register(Review)