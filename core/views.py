from django.shortcuts import render

from core.models import Species, Report, Location
from core.permissions import IsOwnerOrReadOnly
from rest_framework import generics, viewsets, permissions
from core.serializers import SpeciesSerializer, ReportSerializer


class SpeciesList(generics.ListAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

    def get_paginate_by(self):
        """
        Use smaller pagination for HTML representations.
        """
        if self.request.accepted_renderer.format == 'html':
            return 20
        return 100


class SpeciesDetail(generics.RetrieveAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer


class ReportList(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def pre_save(self, obj):
        obj.user = self.request.user


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportCreate(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly, )

    def pre_save(self, obj):
        species = self.request.DATA['species']
        obj.species = Species.objects.get(name=species)
        obj.user = self.request.user
        lat = self.request.DATA['lat']
        lon = self.request.DATA['lon']
        obj.location = Location.objects.get_or_create(lat=lat, lon=lon)[0]
        photo = self.request.DATA['photo']
        obj.photo = Photo(photo=photo)

