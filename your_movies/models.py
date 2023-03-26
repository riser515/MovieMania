from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=15)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Movies(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    release_date = models.DateField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.movie_name
    
class Reviews(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)