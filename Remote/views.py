from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from Remote.models import Keep

from datetime import datetime, date, timedelta
import locale
# 날짜
Delta = 1
if datetime.today().weekday() == 0:
    Delta = 3

locale.setlocale(locale.LC_ALL, '')
TODAY = date.today().strftime('%Y-%m-%d')
YESTER = date.today() - timedelta(Delta)
YESTERDAY = YESTER.strftime('%Y-%m-%d')


class KeepLV(ListView):
    model = Keep
    template_name = 'Remote/main_2.html'
    context_object_name = 'keeps'

    def get_context_data(self, **kwargs):
        context = super(KeepLV, self).get_context_data(**kwargs)
        imsi1 = Keep.objects.filter(
            due_dt__lte=TODAY, safein_chk='o', safeout_chk='x')
        imsi2 = Keep.objects.filter(
            due_dt__lte=TODAY, safein_chk='o', safeout_chk='o', safeout_dt=TODAY)
        imsi = imsi1 | imsi2
        context['checkin'] = imsi.order_by('-cycle', 'due_dt', 'volume_nm')
        context['today'] = imsi.order_by('-due_dt')
        imsi = Keep.objects.filter(check_dt=YESTERDAY)
        context['checkout'] = imsi.order_by('-cycle', 'due_dt', 'volume_nm')
        imsi = Keep.objects.filter(pool_nm='srcpool', due_dt__gt=TODAY)
        context['srcpool'] = imsi.order_by('due_dt')

        return context

    def __str__(self):
        return self
