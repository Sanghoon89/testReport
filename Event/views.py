from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from Event.models import Log

from datetime import date, timedelta
import locale

## 날짜
locale.setlocale(locale.LC_ALL,'')
YESTER = date.today() - timedelta(1)
YESTERDAY = YESTER.strftime('%Y-%m-%d')
YEAR = YESTER.strftime('%Y')
MONTH = YESTER.strftime('%m')

YESTERDAY='2021-09-16'
class LogLV(ListView):
    model = Log
    template_name = 'Event/log_list.html'
    context_object_name = 'logs'

    def get_context_data(self, **kwargs):
        context = super(LogLV, self).get_context_data(**kwargs)
        context['daylist'] = Log.objects.filter(backup_dt=YESTERDAY)
        context['monthlist'] = Log.objects.filter(backup_dt__year=YEAR, backup_dt__month=MONTH)
        imsi = Log.objects.dates('backup_dt', 'month')
        context['months'] = imsi.strftime('%Y-5m')
        return context

    def __str__ (self):
        return self
