from django.conf.urls import url
from .views import home, submsion


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^sub, submission, name='submission')
]
