from django.db import models
from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_facebook.utils import get_user_model, get_profile_model

from core.utils import get_settings_module

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from rest_framework.authtoken.models import Token

@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        print 'token created...'


class BotaniserProfile(FacebookModel):
    user = models.OneToOneField(get_settings_module().AUTH_USER_MODEL, related_name='profile')
    score = models.PositiveIntegerField()

    def calculate_score(self):
        score = sum([r.score for r in user.reports.all()])
        return score


@receiver(post_save)
def create_profile(sender, instance, created, **kwargs):
#Create a matching profile whenever a user object is created.
    if sender == get_user_model():
        user = instance
        profile_model = get_profile_model()
        if profile_model == BotaniserProfile and created:
            profile, new = BotaniserProfile.objects.get_or_create(user=instance)

