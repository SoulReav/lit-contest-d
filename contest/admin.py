from django.contrib import admin
from .models import Contest, Genre, Work, Vote

class ContestAdmin(admin.ModelAdmin):
    list_display = ('title', 'startDate', 'endDate', 'stage')
    list_filter = ('title', 'startDate', 'endDate', 'stage')


admin.site.register(Contest, ContestAdmin)
admin.site.register(Genre)
admin.site.register(Work)
admin.site.register(Vote)
