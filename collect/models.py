from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
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
    contact = models.CharField(max_length=30)


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except Exception as error:
            print(error)


post_save.connect(post_save_user_model_receiver,
                  sender=settings.AUTH_USER_MODEL)


class Projects(models.Model):
    title = models.CharField(User, max_length=200)
    image = ImageField(
        manual_crop='1280x720')
    decription = models.TextField(max_length=200)
    link = models.URLField(null=True, blank=True, default='')


class Categories(models.Model):
    name = models.ManyToManyField(Projects)
