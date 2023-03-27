from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class UserInfo(models.Model):
    class Meta:
        verbose_name_plural = 'Users'

    username = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Movie(models.Model):
    class Meta:
        verbose_name_plural = 'Movies'

    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=255)
    director = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.movie_name
    
class Review(models.Model):
    class Meta:
        verbose_name_plural = 'Reviews'

    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)