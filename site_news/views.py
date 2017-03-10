from django.shortcuts import render
from .models import News

# Create your views here.

def news_full_description(request, year, month, day, id):
    news = News.objects.get(id=id)
    return render(request, 'site_news\site_news_full_description_t.html', {'news': news, })
