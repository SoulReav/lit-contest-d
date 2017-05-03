from django.shortcuts import render
from .models import News
from contest.models import Contest

# Create your views here.

def news_full_description(request, year, month, day, id):
    news = News.objects.get(id=id)
    contests = Contest.objects.order_by('-startDate')[0:3]
    return render(request, 'site_news\site_news_full_description_t.html', {'news': news, 'contests': contests, })

