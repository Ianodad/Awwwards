from django.db import models

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
    contact = models.CharField(default="Anonymous")
