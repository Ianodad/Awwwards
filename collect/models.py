from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
from pyuploadcare.dj.models import ImageField


# Create your models here.


class Profile(models.Model):
    '''
    profile class holding all the models
    '''
    username = models.OneToOneField(
        settings.AUTH_USER_MODEL)
    profile_picture = ImageField(
        manual_crop='200x200')
    bio = models.TextField(default="Tell us more")
    contact = models.CharField(max_length=300)


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except Exception as error:
            print(error)


post_save.connect(post_save_user_model_receiver,
                  sender=settings.AUTH_USER_MODEL)
