from core.models import Report, Species
from rest_framework import serializers


class SpeciesSerializer(serializers.ModelSerializer):
    reports = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Species
        fields = ('id', 'name', 'guid', 'occurrenceCount', 'reports')


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    thumbnail = serializers.CharField(source='photo.get_thumbnail', read_only=True)

    species = SpeciesSerializer(many=False, read_only=True)
    user = serializers.RelatedField(many=False)
    location = serializers.RelatedField(many=False)

    class Meta:
        model = Report
        fields = ('id', 'user', 'location', 'description', 'creationTime', 'photo', 'thumbnail')