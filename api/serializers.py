from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    reports = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'reports')