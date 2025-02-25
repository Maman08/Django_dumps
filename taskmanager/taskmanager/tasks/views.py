from django.shortcuts import render


from django.contrib.auth.models import User
from .serializers import UserSerializers
from rest_framework import generics, permissions
# Create your views here.


class UserCreate(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializers
    permissions_classes=[permissions.AllowAny]

