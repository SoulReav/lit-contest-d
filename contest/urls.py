from django.conf.urls import include, url
from .views import contest_page

urlpatterns = [
        url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<id>\d+)//?$', contest_page, name='contest_page'),
]

