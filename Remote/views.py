from django.db.models.query import _QuerySet
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from Remote.models import Keep

class KeepLV(ListView):
    model = Keep
    template_name = 'Remote/keep_list.html'
    context_object_name = 'keeps'

    def get_queryset(self):
        checkin = Keep.objects.order_by('-check_dt')
#        checkout = Keep.objects.filter(check_dt='2021-09-16')
        return checkin

    def get_context_data(self, **kwargs):
        context = super(KeepLV, self).get_context_data(**kwargs)
        context['bar_list'] = context['keeps_list'].filter(due_dt='2021-09-30')
        return context

    def __str__ (self):
        return self
