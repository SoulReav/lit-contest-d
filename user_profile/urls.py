from django.conf.urls import include, url
from .views import upload_avatar, edit_name

urlpatterns = [
    url(r'^profile/upload/', upload_avatar, name='upload_avatar'),
    url(r'^profile/edit_name/', edit_name, name='edit_name'),
]

