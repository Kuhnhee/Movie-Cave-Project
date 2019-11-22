from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['POST'])
def signup(request):
    #만약 로그인 되어있으면, articles/로 리다이렉트
    # if request.user.is_authenticated:
    #     return Reponse(status=400)

    serializer = UserSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) #index 페이지로 리다이렉트
    else:
        return Response(status=400)

# @api_view(['POST'])
# def create_auth(request):
#     serializer = UserSerializer(data=request.DATA)
#     if serializer.is_valid():
#         User.objects.create_user(
#             serializer.init_data['email'],
#             serializer.init_data['username'],
#             serializer.init_data['password']
#         )
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)