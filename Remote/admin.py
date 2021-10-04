from django.contrib import admin

# Register your models here.

from Event.models import Keep

@admin.register(Keep)
class KeepAdmin(admin.ModelAdmin):
    list_display = ('check_dt', 'volume_nm', 'pool_nm', 'cycle', 'due_dt', 'safein_chk', 'safeout_chk') # 변경
    list_filter = ('safein_chk',)
    search_fields = ('check_dt', 'volume_nm')