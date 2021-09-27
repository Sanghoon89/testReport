from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from Remote.models import Keep

from datetime import date, timedelta

## 날짜
locale.setlocale(locale.LC_ALL,'')
TODAY = date.today().strftime('%Y-%m-%d')
YESTER = date.today() - timedelta(1)
YESTERDAY = YESTER.strftime('%Y-%m-%d')

class KeepLV(ListView):
    model = Keep
    template_name = 'Remote/keep_list.html'
    context_object_name = 'keeps'

    def get_context_data(self, **kwargs):
        context = super(KeepLV, self).get_context_data(**kwargs)
        context['checkin'] = Keep.objects.filter(due_dt=TODAY)
        context['checkout'] = Keep.objects.filter(check_dt=YESTERDAY)
        imsi = Keep.objects.filter(pool_nm='srcpool', due_dt__gte=TODAY)
        context['srcpool'] = imsi.order_by('due_dt')
        return context

    def __str__ (self):
        return self
