from django.conf.urls import url
from site_comments.views import post

urlpatterns = [
    url(r'^post/$', post, name='comments_post'),
]
