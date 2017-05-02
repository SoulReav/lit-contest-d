"""lit_contest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
from site_news import views as site_news
from contest import views as contest
from user_profile import views as user_profile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', include('user_profile.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^news/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<id>\d+)//?$', site_news.news_full_description, name='full_description_news'),
    url(r'^comments/', include('site_comments.urls')),
    url(r'^accounts/', user_profile.show_profile, name='user_profile'),
    url(r'^contest/', include('contest.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
