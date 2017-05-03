from django.conf.urls import include, url
from .views import contest_page, edit_work_page, public_work

urlpatterns = [
        url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<id>\d+)//?$', contest_page, name='contest_page'),
        url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<id>\d+)/edit_work//?$', edit_work_page, name='edit_work_page'),
        url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<id>\d+)/edit_work//?$', edit_work_page, name='edit_work_page'),
        url(r'(?P<id>\d+)/?$', public_work, name='public_work'),
]

