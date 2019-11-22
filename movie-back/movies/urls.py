from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('user/', views.signup, name='signup')
]