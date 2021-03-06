# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-28 23:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название категории')),
            ],
            options={
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='Заголовок новости')),
                ('description', tinymce.models.HTMLField()),
                ('dateCreated', models.DateTimeField(verbose_name='Дата публикации')),
                ('publish', models.BooleanField(verbose_name='Опубликованно?')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_news.Categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
