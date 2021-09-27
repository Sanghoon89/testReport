from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from Remote.models import Keep

class KeepLV(ListView):
    model = Keep
    template_name = 'Remote/keep_list.html'
    context_object_name = 'keeps'

    def get_context_data(self, **kwargs):
        context = super(KeepLV, self).get_context_data(**kwargs)
        context['checkin'] = Keep.objects.filter(due_dt='2021-09-30')
        context['checkout'] = Keep.objects.filter(check_dt='2021-09-16')
        imsi = Keep.objects.filter(pool_nm='srcpool', due_dt__gte='2021-09-16')
        context['srcpool'] = imsi.order_by('-due_dt')
        return context

    def __str__ (self):
        return self
