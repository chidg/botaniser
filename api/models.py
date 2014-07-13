from django.db import models
from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel
from django.db.models.signals import post_save
from django_facebook.utils import get_user_model, get_profile_model
from botaniser import settings


from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


"""
class BotaniserProfile(FacebookModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    score = models.PositiveIntegerField()

    def calculate_score(self):
        return 3


@receiver(post_save)
def create_profile(sender, instance, created, **kwargs):
#Create a matching profile whenever a user object is created.
    if sender == get_user_model():
        user = instance
        profile_model = get_profile_model()
        if profile_model == MyCustomProfile and created:
            profile, new = BotaniserProfile.objects.get_or_create(user=instance)
"""