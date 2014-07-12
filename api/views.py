from django.shortcuts import render

from django.contrib.auth.models import User

from core.models import Species, Report
from rest_framework import generics, viewsets, permissions, parsers
from rest_framework.authtoken.models import Token

from api.serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserCreate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


