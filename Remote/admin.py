from django.contrib import admin

# Register your models here.

from Remote.models import Keep
from django.utils.safestring import mark_safe
from datetime import datetime

@admin.register(Keep)
class KeepAdmin(admin.ModelAdmin):
    list_display = ('check_dt', 'volume_nm', 'pool_nm', 'cycle', 'due_dt', 'safein_chk', 'safeout_chk','safein_dt', 'safeout_dt',) # 변경
    list_display_links = ('check_dt', 'volume_nm',)
    list_editable = ('safein_chk', 'safeout_chk','safein_dt', 'safeout_dt',)
    list_filter = ('safein_chk','safeout_chk')
    list_per_page = 20
    search_fields = ('check_dt', 'volume_nm')
    actions = ('check_safein','check_safeout')

    def check_safein(self, request, queryset):
        updated_count = queryset.update(safein_chk='o', safein_dt=Keep('check_dt')) #queryset.update
        self.message_user(request, '{}건의 볼륨을 입고확인 상태로 변경'.format(updated_count)) #django message framework 활용
    check_safein.short_description = '지정 볼륨을 입고확인 상태로 변경'

    def check_safeout(self, request, queryset):
        updated_count = queryset.update(safeout_chk='o', safeout_dt=datetime.now()) #queryset.update
        self.message_user(request, '{}건의 볼륨을 출고확인 상태로 변경'.format(updated_count)) #django message framework 활용
    check_safeout.short_description = '지정 볼륨을 출고확인 상태로 변경'
