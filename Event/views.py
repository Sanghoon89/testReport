from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from Event.models import Log

class LogLV(ListView):
    model = Log
    template_name = 'Event/log_list.html'
    context_object_name = 'logs'

    def __str__ (self):
        return self
