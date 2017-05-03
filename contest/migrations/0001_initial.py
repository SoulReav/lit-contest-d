# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 11:44
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
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Без названия', max_length=140, verbose_name='Заголовок конкурса')),
                ('mainLogo', models.ImageField(upload_to='contest_images/slider/', verbose_name='Картинка к слайдеру')),
                ('descLogo', models.ImageField(upload_to='contest_images/desc/', verbose_name='Картинка к заголовку')),
                ('sliderDescription', models.TextField(verbose_name='Описание для слайдера')),
                ('description', tinymce.models.HTMLField(verbose_name='Описание')),
                ('startDate', models.DateField(verbose_name='Дата старта')),
                ('endDate', models.DateField(verbose_name='Дата завершения')),
                ('stage', models.CharField(choices=[('CT', 'Contest'), ('MD', 'Moderate'), ('VT', 'Vote'), ('CM', 'Completed')], max_length=2, verbose_name='Этапы')),
                ('contestants', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Участники')),
            ],
            options={
                'verbose_name_plural': 'Список конкурсов',
            },
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300, verbose_name='Приветствуется')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.Contest')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название жанра')),
            ],
            options={
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300, verbose_name='Обязательные требования')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.Contest')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('text_work', tinymce.models.HTMLField(verbose_name='Текст работы')),
                ('public', models.BooleanField(verbose_name='Опубликована?')),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.AddField(
            model_name='contest',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contest.Genre', verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='contest',
            name='works',
            field=models.ManyToManyField(blank=True, null=True, to='contest.Work', verbose_name='Работы участников'),
        ),
    ]
