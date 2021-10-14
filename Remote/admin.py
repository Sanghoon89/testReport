from django.contrib import admin

# Register your models here.

from Remote.models import Keep

@admin.register(Keep)
class KeepAdmin(admin.ModelAdmin):
    list_display = ('check_dt', 'volume_nm', 'pool_nm', 'cycle', 'due_dt', 'safein_chk', 'safeout_chk','safein_dt', 'safeout_dt',) # 변경
    list_display_link = ('check_dt', 'volume_nm',)
    list_editable = ('safein_chk', 'safeout_chk','safein_dt', 'safeout_dt',)
    list_filter = ('safein_chk','safeout_chk')
    search_fields = ('check_dt', 'volume_nm')