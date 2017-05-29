from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Структура данных, описывающая категории новостей, публикуеммых на сервисе.
class Categories(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')

    def __str__(self):  # Функция, возвращающая название категори для Django Admin.
        return self.name

    class Meta:  # Класс описывающий мета информацию о модели данных.
        verbose_name_plural = u"Категории"  # Имя модели данных для Django Admin.


# Структура данных, описывающая модель новости, публикуемой на сайте
class News(models.Model):
    title = models.CharField(max_length=140, verbose_name='Заголовок новости')
    description = HTMLField(verbose_name='Описание конкурса')
    dateCreated = models.DateTimeField(verbose_name='Дата публикации')
    author = models.ForeignKey(User, verbose_name='Автор')
    publish = models.BooleanField(verbose_name='Опубликованно?')
    categories = models.ForeignKey(Categories, verbose_name='Категория')

    def __str__(self):  # Функция, возвращающая название категори для Django Admin.
        return self.title

    # Функция, возвращающая уникальный URL для каждой новости
    def get_absolute_url(self):
        return "/news/%s" % (self.dateCreated.strftime('%Y/%m/%d/') + str(self.id) + '/')

    class Meta:  # Класс описывающий мета информацию о модели данных.
        verbose_name_plural = u"Новости"  # Имя модели данных для Django Admin.