from django.conf.urls import url
from .views import home, submission, profile


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^sub', submission, name='submission'),
    url(r'profile', profile, name='profile')
]
