from core.models import Report, Species, Photo
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    thumbnail = serializers.CharField(source='get_thumbnail', read_only=True)

    class Meta:
        model = Photo
        fields = ('photo', 'thumbnail')


class SpeciesSerializer(serializers.ModelSerializer):
    reports = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Species
        fields = ('id', 'name', 'guid', 'occurrenceCount', 'reports')


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True, required=True)
    species = SpeciesSerializer(many=False, read_only=True)
    user = serializers.RelatedField(many=False)
    location = serializers.RelatedField(many=False)

    class Meta:
        model = Report
        fields = ('id', 'user', 'location', 'description', 'creationTime', 'photos')
