from django.conf.urls import include, url
from .views import upload_avatar, edit_name, show_profile

urlpatterns = [
    url(r'^profile/$', show_profile, name='user_profile'),
    url(r'^profile/upload/$', upload_avatar, name='upload_avatar'),
    url(r'^profile/edit_name/$', edit_name, name='edit_name'),
    url(r'^$', show_profile,),

]

