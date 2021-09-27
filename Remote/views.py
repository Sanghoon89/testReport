from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from Remote.models import Keep

class KeepLV(ListView):
    model = Keep
    template_name = 'Remote/keep_list.html'
    context_object_name = 'keeps'

    def get_queryset(self):
        checkin = Keep.objects.filter(due_dt='2021-09-30')
        checkout = Keep.objects.filter(check_dt='2021-09-16')
        return checkin, checkout

    def __str__ (self):
        return self
