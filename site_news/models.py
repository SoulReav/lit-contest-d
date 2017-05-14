from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"Категории"


class News(models.Model):
    title = models.CharField(max_length=140, verbose_name='Заголовок новости')
    description = HTMLField(verbose_name='Описание конкурса')
    dateCreated = models.DateTimeField(verbose_name='Дата публикации')
    author = models.ForeignKey(User, verbose_name='Автор')
    publish = models.BooleanField(verbose_name='Опубликованно?')
    categories = models.ForeignKey(Categories, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/news/%s" % (self.dateCreated.strftime('%Y/%m/%d/') + str(self.id) + '/')

    class Meta:
        verbose_name_plural = u"Новости"