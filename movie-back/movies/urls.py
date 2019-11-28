from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('user/', views.signup, name='signup'),
    path('my_movies/', views.my_movies, name='my_movies'),
    path('movie/', views.movie, name='movie'),
    path('movie/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('actor/', views.actor, name='actor'),
    path('actor/<int:actor_pk>/', views.actor_detail, name='actor_detail'),
    path('director/', views.director, name='director'),
    path('director/<int:director_pk>/', views.director_detail, name='director_detail'),
    path('genre/', views.genre, name='genre'),
    path('genre/<int:genre_pk>/', views.genre_detail, name='genre_detail'),
    path('worldcup/', views.random_worldcup, name='random_worldcup'),
    path('worldcup/<int:worldcup_pk>/', views.worldcup_detail, name='worldcup_detail'),
    path('worldcup/custom/', views.create_worldcup, name='create_worldcup'),
    path('score_update/', views.score_update, name='score_update'),

    # for infinite scroll
    path('movie/list/', views.MovieListAPI.as_view(), name='movie_list')
]
