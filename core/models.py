from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from easy_thumbnails.fields import ThumbnailerImageField
from botaniser.settings import settings


#######thumbnails stuff #########
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global

saved_file.connect(generate_aliases_global)


# Create your models here.


def imagePath(instance, filename):
    """A static function used by the Photo :class:`botaniser.core.models.Photo`
    It is used to determine the upload location for photos at runtime.

    Accepts two parameters (instance and filename).
    Returns the upload path as a String.
    """

    #The name of the model type which is associated with the photo
    reportid = instance.report.id

    path = list(['uploads', 'images', reportid, filename])
    return str('/').join(path)



class Report(models.Model):
    """
    user
    location
    photo/s
    species
    description
    status
    points
    """

    statusChoices=(
        ('pending','Pending'),
        ('accepted','Accepted'),
        ('disputed', 'Disputed'),
        ('rejected', 'Rejected'),
        )


    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='reports')
    location = models.ForeignKey('Location', null=True, related_name='reports')
    photo = ThumbnailerImageField(upload_to=imagePath)
    species = models.ForeignKey('Species', null=True, related_name='reports')
    description = models.TextField(max_length=400)
    status = models.CharField(max_length=12, choices=statusChoices, default='accepted', help_text="The current status of this report.")
    points = models.PositiveIntegerField()
    creationTime = models.DateTimeField('Time created', auto_now_add=True)


class Location(models.Model):
    lat = models.DecimalField('Latitude', max_digits=10,decimal_places=8, help_text="Latitude in decimal degrees. For example -32.49293.")
    lon = models.DecimalField('Longitude', max_digits=11,decimal_places=8, help_text="Longitude in decimal degrees. For example 122.9213s.")


class Species(models.Model):
    name = models.CharField("Name", max_length=100)
    guid = models.CharField(max_length=100)
    occurrenceCount = models.PositiveIntegerField()

    def calculate_score(self):
        score_map = {
            4:[1,5],
            3:[6,10],
            2:[11,20],
            1.5:[21,50],
            1.2:[51,75],
            1:[76,102],
            }

        for value in score_map:
            if self.occurrenceCount in range(score_map[value][0], score_map[value][1]):
                return 10 * value
        return 10


