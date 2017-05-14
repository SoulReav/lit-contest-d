from django.contrib import admin
from .models import News, Categories

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'dateCreated','publish', 'author')
    list_filter = ('title', 'dateCreated', 'publish', 'author')
    date_hierarchy = 'dateCreated'

admin.site.register(Categories)

admin.site.register(News, NewsAdmin)