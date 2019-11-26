from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

from .models import *

# from django.contrib.auth.models import User


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name', 'role', 'img_url', 'description', 'movies')

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'role', 'img_url', 'description', 'movies')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_en', 'rate', 'img_url', 'description', 'directors', 'actors', 'genres', 'users')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'content', 'score', 'movie',)
    
class WorldcupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worldcup
        fields = ('id', 'movies')

class UserSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True)
    movies = MovieSerializer(many=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'review_set', 'movies')

    