from django.shortcuts import render
from .models import News
from contest.models import Contest

# Create your views here.

def news_cut_description(request):

    # Загружает в переменую public_news данные из таблицы СУБД о последних 5-ти опубликованных новостях
    public_news = News.objects.order_by('-dateCreated').filter(publish=True)[0:5]

    for p in public_news:
        # Ищет в тексте каждой загруженной новости тег <!--more-->
        cut = p.description.find('<!--more-->')
        # Если тег найден...
        if cut != -1:
            # текст новости обрезается до начала вхождения тега
            p.description = p.description[0:cut]

    # Узнаем авторизирован ли пользователь, и записываем в переменную u_auth
    u_auth = request.user.is_authenticated()

    # записывает в переменную contests данные о трёх свежих конкурсах.
    contests = Contest.objects.order_by('-startDate')[0:3]
    # передает в шаблон site_news_cut_descriptiion переменные с данными для визуализации,
    # и возвращает пользователю HTML документ, сгенерированный на базе шаблона и переданных данных
    return render(request, 'site_news\site_news_cut_description_t.html', {'u_auth': u_auth, 'public_news': public_news,
                                                                          'contests': contests, }, )


def news_full_description(request, year, month, day, id):
    news = News.objects.get(id=id)
    contests = Contest.objects.order_by('-startDate')[0:3]
    return render(request, 'site_news\site_news_full_description_t.html', {'news': news, 'contests': contests, })

