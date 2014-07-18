from django.contrib.auth.models import User
from django_facebook.utils import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('url', 'username', 'email', 'groups')