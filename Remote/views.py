from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from Remote.models import Keep

from datetime import date, timedelta
import locale
## 날짜
locale.setlocale(locale.LC_ALL,'')
TODAY = date.today().strftime('%Y-%m-%d')
YESTER = date.today() - timedelta(1)
YESTERDAY = YESTER.strftime('%Y-%m-%d')

YESTERDAY="2021-09-08"
TODAY="2021-09-11"
class KeepLV(ListView):
    model = Keep
    template_name = 'Remote/main.html'
    context_object_name = 'keeps'

    def get_context_data(self, **kwargs):
        context = super(KeepLV, self).get_context_data(**kwargs)
        imsi = Keep.objects.filter(due_dt=TODAY)
        context['checkin'] = imsi.order_by('-cycle', 'volume_nm')
        imsi = Keep.objects.filter(check_dt=YESTERDAY)
        context['checkout'] = imsi.order_by('-cycle', 'volume_nm')
        imsi = Keep.objects.filter(pool_nm='srcpool', due_dt__gt=TODAY)
        context['srcpool'] = imsi.order_by('due_dt')
        return context

    def __str__ (self):
        return self
