from rest_framework import serializers
from .models import User, Movie, Review


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'description', 'user_id', 'release_date', 'is_deleted']

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user_id', 'movie_id', 'rating', 'comment', 'is_deleted']