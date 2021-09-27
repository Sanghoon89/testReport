from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from Remote.models import Keep

class KeepLV(ListView):
    model = Keep
    template_name = 'Remote/keep_list.html'
    context_object_name = 'keeps'

    def __str__ (self):
        return self
