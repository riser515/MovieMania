from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import HyperlinkedRelatedField
from ..models import User, Movie, Review
from ..serializers import UserSerializer, MovieSerializer, ReviewSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def all_movies(request):
    try:
        movies = Movie.objects.all()
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        user = User.objects.get(id = 1)
        
        data = {
            'user_id': user.id,
            'movie_name': request.data.get('movie_name'),
            'description': request.data.get('description'),
            'release_date': request.data.get('release_date'),
            'is_deleted': False
        }
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def single_movie(request, id):
    try:
        movie = Movie.objects.get(id = id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        user = User.objects.get(id = 1)
        data = request.data
        data["user_id"] = user.id
        data["id"] = id
        data["is_deleted"] = False
        serializer = MovieSerializer(movie, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user = User.objects.get(id = 1)
        try:
            movie = Movie.objects.get(id = id)
            movie.is_deleted = True
            movie.user_id = user
            movie.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    