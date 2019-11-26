from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

import random

# .../users/pk/
@api_view(['GET'])
def user_detail(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)

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