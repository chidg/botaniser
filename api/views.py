from django.shortcuts import render

from django.contrib.auth.models import User
from core.models import Species, Report
from rest_framework import generics
from rest_framework import viewsets
from api.serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create your views here.
