from django.db import models

class User(models.Model):
    class Meta:
        verbose_name_plural = 'Users'

    username = models.CharField(max_length=15)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Movie(models.Model):
    class Meta:
        verbose_name_plural = 'Movies'

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    release_date = models.DateField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.movie_name
    
class Review(models.Model):
    class Meta:
        verbose_name_plural = 'Reviews'

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)