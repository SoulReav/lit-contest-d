from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Genre(models.Model):
    title = models.CharField(max_length=30, verbose_name=u'Название жанра', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = u"Жанры"

class Work(models.Model):
    title = models.CharField(max_length=140)
    author = models.ForeignKey(User, verbose_name='Автор')
    text_work = HTMLField(verbose_name='Текст работы')
    public = models.NullBooleanField(verbose_name='Опубликована?', null=True, blank=True,)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    raiting_work = models.IntegerField(verbose_name='Рейтинг', default=0)


    def __str__(self):
        return self.title + ' | Автор: ' + self.author.username

    class Meta:
        verbose_name_plural = u"Работы участников"


# Create your models here.
class Contest(models.Model):
    title = models.CharField(max_length=140, verbose_name=u'Заголовок конкурса', default='Без названия')
    mainLogo = models.ImageField(upload_to='contest_images/slider/', verbose_name=u'Картинка к слайдеру')
    descLogo = models.ImageField(upload_to='contest_images/desc/', verbose_name=u'Картинка к заголовку')
    sliderDescription = models.TextField(verbose_name=u'Описание для слайдера')
    description = HTMLField(verbose_name=u'Описание')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name=u'Жанр')
    terms = HTMLField(verbose_name=u'Обязательные требования', null=True)
    extra = HTMLField(verbose_name=u'Дополнительная информация', null=True)
    startDate = models.DateField(verbose_name=u'Дата старта')
    endDate = models.DateField(verbose_name=u'Дата завершения')
    contestants = models.ManyToManyField(User, blank=True, verbose_name=u'Участники')
    st = ((u'CT', u'Contest'),
          (u'MD', u'Moderate'),
          (u'VT', u'Vote'),
          (u'CM', u'Completed'),)
    stage = models.CharField(max_length=2, choices=st, verbose_name=u'Этапы')
    works = models.ManyToManyField(Work,  blank=True, verbose_name=u'Работы участников')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = u"Список конкурсов"


    def get_absolute_url(self):
        return "/contest/%s" % (self.startdate.strftime('%Y/%m/%d/') + str(self.id)+'/')


class Vote(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор')
    voted = models.BooleanField(default=False)
    contest = models.ForeignKey(Contest, blank=True, null=True, verbose_name=u'Конкурс')

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name_plural = u"Голоса"





