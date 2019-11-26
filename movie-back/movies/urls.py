from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    # path('user/', views.signup, name='signup')
    path('user/<int:user_pk>/', views.user_detail, name='user_detail'),
    path('movie/', views.movie, name='movie'),
    path('movie/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('actor/', views.actor, name='actor'),
    path('actor/<int:actor_pk>/', views.actor_detail, name='actor_detail'),
    path('director/', views.director, name='director'),
    path('director/<int:director_pk>/', views.director_detail, name='director_detail'),
    path('genre/', views.genre, name='genre'),
    path('genre/<int:genre_pk>/', views.genre_detail, name='genre_detail'),
]