from django.contrib import admin

# Register your models here.
from Remote.models import Keep
#from django.utils.safestring import mark_safe
from datetime import datetime, date
from django.db.models import F
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

@admin.register(Keep)
class KeepAdmin(admin.ModelAdmin):
    list_display = ('check_dt','volume_nm','pool_nm','due_dt','safein_chk','safein_dt','safeout_chk','safeout_dt',) # 변경
    list_display_links = ('check_dt', 'volume_nm',)
    list_editable = ('safein_chk', 'safeout_chk','safein_dt', 'safeout_dt',)
    list_filter = (('check_dt', DateRangeFilter), ('due_dt', DateRangeFilter),
                    'safein_chk','safeout_chk',)
    list_per_page = 20
    search_fields = ('check_dt', 'volume_nm',)
    actions = ('check_safein','check_safeout')

    def check_safein(self, request, queryset):
        updated_count = queryset.update(safein_chk='o', safein_dt=F('check_dt')) #queryset.update
        self.message_user(request, '{}건의 볼륨을 입고확인 상태로 변경'.format(updated_count)) #django message framework 활용
    check_safein.short_description = '지정 볼륨 입고확인'

    def check_safeout(self, request, queryset):
        updated_count = queryset.update(safeout_chk='o', safeout_dt=datetime.now()) #queryset.update
        self.message_user(request, f'{updated_count}건의 볼륨을 출고확인 상태로 변경') #django message framework 활용
    check_safeout.short_description = '지정 볼륨 출고확인'

    # If you would like to add a default range filter
    # method pattern "get_rangefilter_{field_name}_default"
    def get_rangefilter_check_dt_default(self, request):
        return (date.today(), date.today())
    def get_rangefilter_due_dt_default(self, request):
        return (date.today(), date.today())

    # If you would like to change a title range filter
    # method pattern "get_rangefilter_{field_name}_title"
    def get_rangefilter_check_dt_title(self, request, field_path):
        return '소산일'
    def get_rangefilter_due_dt_title(self, request, field_path):
        return '만료일'