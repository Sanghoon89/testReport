from django.contrib import admin

# Register your models here.

from Event.models import Log

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('backup_dt', 'schedule_tm', 'schedule_nm', 'nodename', 'domain_nm', 'start_tm', 'end_tm', 'taken', 'status', 'returncode', 'action', 'note') # 변경
    list_display_links = ('backup_dt', 'schedule_nm',)
    list_editable = ('status', 'action', 'note',)
    list_filter = ('status', 'returncode',)
    search_fields = ('schedule_nm', 'nodename', 'status', 'returncode')
