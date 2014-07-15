from django.shortcuts import render
from django.contrib.auth.models import User

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
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        #IsOwnerOrReadOnly, )

    def pre_save(self, obj):
        print 'trying to save a report....'
        species = self.request.DATA['name']
        obj.species = Species.objects.get(name=species)
        obj.points = obj.species.calculate_score()
        obj.user = User.objects.get(username='chid')
        lat = self.request.DATA['lat']
        lon = self.request.DATA['lon']
        obj.location = Location.objects.get_or_create(lat=lat, lon=lon)[0]
        print 'saved most things....'
        img_string = self.request.DATA['imageSrc']
        img_data = img_string.decode("base64")
        filename = str(obj.species.name.replace(' ', '_')) + 'photo.jpg'
        img_file = open(filename, "wb")
        img_file.write(img_data)
        img_file.close()
        print 'after photo process'
        obj.photo = img_file
        print 'after photo...'


def index(request):
    return render(request, 'index.html')

