from django.contrib import admin

# Register your models here.

from Event.models import Log

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('backup_dt', 'schedule_tm', 'schedule_nm', 'nodename', 'domain_nm', 'start_tm', 'end_tm', 'taken', 'status', 'returncode', 'action', 'note') # 변경
    list_filter = ('returncode',)
    search_fields = ('schedule_nm', 'nodename')

class LogInline(admin.TabularInline)
