from django.shortcuts import render
from site_news.models import News

def index(request):

    public_news = News.objects.order_by('-dateCreated').filter(publish=True)[0:5]
    for p in public_news:
        cut = p.description.find('<!--more-->')
        if cut != -1:
            p.description = p.description[0:cut]

    u_auth = request.user.is_authenticated()
    return render(request, 'site_news/site_news_cut_description_t.html', {'u_auth': u_auth, 'public_news': public_news, }, )

