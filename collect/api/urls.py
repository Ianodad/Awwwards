from django.conf.urls import url
from .views import ProfileView
from rest_framework import routers


urlpatterns = [
    url(r'^profile', ProfileView, name='profileview'),
]
