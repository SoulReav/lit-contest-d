from django.conf.urls import include, url
from .views import contest_page, edit_work_page, public_work, delete_work, get_in_contest, leave_contest

urlpatterns = [
        url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<id>\d+)//?$', contest_page, name='contest_page'),
        url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<id>\d+)/edit_work//?$', edit_work_page, name='edit_work_page'),
        url(r'public_work/(?P<id>\d+)//?$', public_work, name='public_work'),
        url(r'delete_work/(?P<id>\d+)//?$', delete_work, name='delete_work'),
        url(r'get_in_contest/(?P<id>\d+)//?$', get_in_contest, name='get_in_contest'),
        url(r'leave_contest/(?P<id>\d+)//?$', leave_contest, name='leave_contest'),
]