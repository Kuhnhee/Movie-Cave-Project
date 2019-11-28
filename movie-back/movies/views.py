from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import AllowAny # 회원가입은 인증 X

from .models import *
from .serializers import *
from rest_framework import pagination, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

import random

# .../user/
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid():
        user=serializer.save()
        user.set_password(user.password)
        user.save()
        return Response(status=200, data={'message': '회원가입 성공'})

# .../user/user_pk/
@api_view(['GET'])
def user_info(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    user_serializer = UserSerializer(user)
    return Response(user_serializer.data)

# .../my_movies/
@api_view(['GET'])
def my_movies(request):
    user = request.user
    user_serializer = UserSerializer(user)
    return Response(user_serializer.data)

# .../movie/
@api_view(['GET'])
def movie(request):
    movies = Movie.objects.all()

    movie_serializer = MovieSerializer(movies, many=True)
    return Response(movie_serializer.data)

# .../movie/pk/
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    movie_detail_serializer = MovieSerializer(movie)
    return Response(movie_detail_serializer.data)

# .../actor/
@api_view(['GET'])
def actor(request):
    actors = Actor.objects.all()

    actors_serializer = ActorSerializer(actors, many=True)
    return Response(actors_serializer.data)

# .../actor/pk/
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)

    actor_serializer = ActorSerializer(actor)
    return Response(actor_serializer.data)

# .../director/
@api_view(['GET'])
def director(request):
    directors = Director.objects.all()

    directors_serializer = DirectorSerializer(directors, many=True)
    return Response(directors_serializer.data)

# .../director/pk/
@api_view(['GET'])
def director_detail(request, director_pk):
    director = get_object_or_404(Director, pk=director_pk)

    director_serializer = DirectorSerializer(director)
    return Response(director_serializer.data)

# .../genre/
@api_view(['GET'])
def genre(request):
    genres = Genre.objects.all()
    genres_serializer = GenreSerializer(genres, many=True)
    return Response(genres_serializer.data)

# .../genre/pk/
@api_view(['GET'])
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    genre_serializer = GenreSerializer(genre)
    return Response(genre_serializer.data)


# .../worldcup/
@api_view(['GET'])
def random_worldcup(request):
    # random & filterting 자료 https://stackoverflow.com/questions/32389519/django-get-10-random-instances-from-a-queryset-and-order-them-into-a-new-querys
    random_movies = random.sample(list(Movie.objects.all()), 32)
    # random_movies = Movie.objects.all().order_by('?')[:32]

    worldcup = Worldcup()
    worldcup.save()
    worldcup.movies.set(random_movies)

    # worldcup = Worldcup.create(random_movies)
    worldcup_serializer = WorldcupSerializer(worldcup)
    return Response(worldcup_serializer.data)

# .../worldcup/pk/
@api_view(['GET'])
def worldcup_detail(request, worldcup_pk):
    worldcup = get_object_or_404(Worldcup, pk=worldcup_pk)
    worldcup_serializer = WorldcupSerializer(worldcup)
    return Response(worldcup_serializer.data)

# .../worldcup/custom/
@api_view(['POST'])
def create_worldcup(request):
    serializer = WorldcupSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400)

# .../score_update/
@api_view(['POST'])
def score_update(request):
    '''
    기대하는 request.POST 데이터 형태
    {
        'movie_pk': ?,
        'worldcup_pk': ?,
    }   
    '''
    data = request.POST
    movie_pk = int(data.get('movie_pk'))
    worldcup_pk = int(data.get('worldcup_pk'))
    movie = get_object_or_404(Movie, pk=movie_pk)
    worldcup = get_object_or_404(Worldcup, pk=worldcup_pk)

    target_record = Ranking.objects.get(movie=movie, worldcup=worldcup)
    target_record.score += 1
    target_record.save()

    result = {
        'movie_pk': movie_pk,
        'worldcup': worldcup_pk,
        'changed_score': target_record.score,
    }

    return Response(result)

# .../review/
@api_view(['POST'])
def review_create(request):
    r_data = request.data
    review_serializer = ReviewSerializer(data=r_data)
    if review_serializer.is_valid():
        review_serializer.save()
        return Response(review_serializer.data)
    return Response(status=400)

# .../review/delete/review_pk/
@api_view(['GET'])
def review_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return Response(status=200)

# .../review/movie/movie_pk/
@api_view(['GET'])
def review_movie(request, movie_pk):
    # movie_pk에 달려있는 모든 리뷰를 가져온다.
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = movie.review_set

    reviews_serializer = ReviewSerializer(reviews, many=True)
    return Response(reviews_serializer.data)

# .../review/user/user_pk/
@api_view(['GET'])
def review_user(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    reviews = user.review_set

    reviews_serializer = ReviewSerializer(reviews, many=True)
    return Response(reviews_serializer.data)


# for infinite scroll(Pagination)
class MoviePagination(pagination.PageNumberPagination):
    page_size = 20

# for infinite scroll(ListAPIView)
class MovieListAPI(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination