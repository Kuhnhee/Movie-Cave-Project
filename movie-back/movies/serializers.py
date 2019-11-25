from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

from .models import *

# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     # todo_set = TodoSerializer(many=True)

#     # email = serializers.EmailField(
#     #         required=True,
#     #         validators=[UniqueValidator(queryset=User.objects.all())]
#     #         )
#     username = serializers.CharField(
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )
#     password = serializers.CharField(min_length=8)

#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'],
#              validated_data['password'])
#         return user

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', )

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name', 'role', 'img_url', 'description')

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'role', 'img_url', 'description')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'title_en', 'rate', 'img_url', 'description', 'directors', 'actors', 'genres')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'content', 'score', 'movie',)
    
class WorldcupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worldcup
        fields = ('id', 'movies')
