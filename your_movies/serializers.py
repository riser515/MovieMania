from rest_framework import serializers
from .models import UserInfo, Movie, Review


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'username', 'email', 'password', 'is_deleted']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=UserInfo.objects.all(), many=False)

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'director', 'description', 'user_id', 'release_date', 'is_deleted']

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=UserInfo.objects.all(), many=False)
    movie_id = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), many=False)

    class Meta:
        model = Review
        fields = ['id', 'user_id', 'movie_id', 'rating', 'comment', 'is_deleted']