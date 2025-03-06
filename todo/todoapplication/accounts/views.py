from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserSerializer


class RegisterView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=AllowAny

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

# Create your views here.permission_classes




































    # djoser.urls includes:
    #     /auth/users/ → Get all users.
    #     /auth/users/me/ → Get the currently logged-in user.
    #     /auth/users/confirm/ → Confirm email (if configured).
    #     /auth/users/reset_password/ → Reset password.
    # djoser.urls.authtoken includes:
    #     /auth/token/login/ → Login and get an authentication token.
    #     /auth/token/logout/ → Logout (delete the token).

