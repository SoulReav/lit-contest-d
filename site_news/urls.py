from django.conf.urls import url
from .views import news_full_description

urlpatterns = [
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<id>\d+)//?$', news_full_description,
        name='full_description_news'),
    ]
