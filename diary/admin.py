from django.contrib import admin
from diary.models import Log


class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_date')


admin.site.register(Log, LogAdmin)
