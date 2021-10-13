from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from Event.models import Log

from datetime import date, timedelta
import locale

## 날짜
locale.setlocale(locale.LC_ALL,'')
YESTER = date.today() - timedelta(1)
YESTERDAY = YESTER.strftime('%Y-%m-%d')
YEAR = YESTER.strftime('%Y')
MONTH = YESTER.strftime('%m')

class LogLV(ListView):
    model = Log
    template_name = 'Event/log_list.html'
    context_object_name = 'logs'

    def get_context_data(self, **kwargs):
        context = super(LogLV, self).get_context_data(**kwargs)
        context['daylist'] = Log.objects.filter(backup_dt=YESTERDAY)
        context['monthlist'] = Log.objects.filter(backup_dt__year=YEAR, backup_dt__month=MONTH)
        context['months'] = Log.objects.dates('backup_dt', 'month')
        return context

    def __str__ (self):
        return self

class LogAV(ArchiveIndexView):
    model = Log
    date_field = 'backup_dt'

class LogYAV(YearArchiveView):
    model = Log
    date_field = 'backup_dt'
#    make_object_list = True

class LogMAV(MonthArchiveView):
    model = Log
    date_field = 'backup_dt'
    make_object_list = True

class LogDAV(DayArchiveView):
    model = Log
    date_field = 'backup_dt'

class LogTAV(TodayArchiveView):
    model = Log
    date_field = 'backup_dt'