from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import HyperlinkedRelatedField
from .models import UserInfo, Movie, Review, User
from .serializers import UserSerializer, MovieSerializer, ReviewSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from dotenv import load_dotenv
import os

load_dotenv()

# API to access all movies using movies/
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_movies(request):
    try:
        movies = Movie.objects.all()
    except Movie.DoesNotExist:
        return Response("No movies exist", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
# API to post a movie using movies/create_movie
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_movie(request):
    if request.method == 'GET':
        return Response("Please enter your movie here...", status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        user = UserInfo.objects.get(id=os.environ.get('STATIC_USER_ID'), is_deleted=False)
        data = request.data
        data["user_id"] = user.id
        
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API to access movies based on movie_id using movies/movie_id/
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def specific_movie(request, pk_movie_id):
    try:
        movie = Movie.objects.get(id=pk_movie_id, is_deleted=False)
    except Movie.DoesNotExist:
        return Response("Movie does not exist", status=status.HTTP_404_NOT_FOUND)
    
    user = UserInfo.objects.get(id=os.environ.get('STATIC_USER_ID'))
        
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = request.data
        data["user_id"] = user.id
        data["id"] = pk_movie_id

        if "movie_name" not in data:
            data["movie_name"] = movie.movie_name

        serializer = MovieSerializer(movie, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            movie = Movie.objects.get(id = pk_movie_id, is_deleted=False)
            movie.is_deleted = True
            movie.user_id = user
            movie.save()
            return Response("Movie has been deleted", status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
# API to access all reviews using reviews/
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_reviews(request):
    try:
        reviews = Review.objects.all()
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
# API to access reviews using reviews/movie_id/
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_movie(request, fk_movie_id):
    try:
        review = Review.objects.filter(movie_id=fk_movie_id, user_id = os.environ.get('STATIC_USER_ID'), is_deleted=False)
    except Review.DoesNotExist:
        return Response("No review", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        user = UserInfo.objects.get(id = os.environ.get('STATIC_USER_ID'), is_deleted=False) 
        data = request.data     
        data['user_id'] = user.id
        data["movie_id"] = fk_movie_id   

        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API to update a review by review_id using reviews/review_id
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_review(request, pk_review_id):
    try:
        review = Review.objects.get(id=pk_review_id, is_deleted=False)
    except Review.DoesNotExist:
        return Response("No review", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = request.data
        data["user_id"] = review.user_id.id
        data["movie_id"] = review.movie_id.id
        serializer = ReviewSerializer(review, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            review.is_deleted = True
            review.save()
            return Response("Your review has been deleted", status=status.HTTP_204_NO_CONTENT)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
# API to post a review using reviews/create_review 
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_review(request):
    if request.method == 'GET':
        return Response("Please post your review here", status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        user = UserInfo.objects.get(id = os.environ.get('STATIC_USER_ID'), is_deleted=False) 
        data = request.data
        data['user_id'] = user.id

        if "movie_id" not in data:
            return Response("Movie ID is required", status=status.HTTP_400_BAD_REQUEST)
        else:
            movie = Movie.objects.filter(id=request.data["movie_id"], user_id=user.id, is_deleted=False)
            if not movie:
                return Response("Invalid movie id", status=status.HTTP_400_BAD_REQUEST)

        serializer = ReviewSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    try:
        email = request.data['email']
        password =request.data['password']

        user = User.objects.filter(email=email)
        user_exists = user.exists()

        if user_exists:
            user = user[0]
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                data = {
                    "email": user.email,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
                return JsonResponse(data=data, status=200)
            else:
                return Response("Invalid Email or Password", status=status.HTTP_403_FORBIDDEN)
        else:
            return Response("No User Found", status=status.HTTP_404_NOT_FOUND)

    except Exception as error:
        return Response(str(error) ,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST'])
def signup(request):
    try:
        username = request.data['username']
        first_name = request.data['first_name'] 
        last_name = request.data['last_name']
        email = request.data['email']
        user = User.objects.filter(email=email)
        email_exists = user.exists()
        password = request.data['password']

        if email_exists:
            return Response("User Already exist with this email", status=status.HTTP_409_CONFLICT)
        else:
            new_user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            data = {
                "username": new_user.username,
                "first_name": new_user.first_name,
                "last_name": new_user.last_name,
                "email": new_user.email,
            }
            return JsonResponse(data=data, status=200)
    
    except Exception as error:
        return Response(str(error) ,status=status.HTTP_500_INTERNAL_SERVER_ERROR)