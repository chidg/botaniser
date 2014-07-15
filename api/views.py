from django.shortcuts import render

from django_facebook.utils import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import logout

from core.models import Species, Report
from rest_framework import generics, viewsets, permissions, parsers
from rest_framework.authtoken.models import Token

from api.serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserCreate(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


def logout_view(request):
    logout(request)
    return render(request, 'index.html')
    # Redirect to a success page.