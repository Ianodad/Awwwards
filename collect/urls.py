from django.conf.urls import url
from .views import home, submission, profile, add_profile, search


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^sub', submission, name='submission'),
    url(r'^profile', profile, name='profile'),
    url(r'^add_profile', add_profile, name='add_profile'),
    url(r'^results$', search, name='search')
]
