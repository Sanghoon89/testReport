from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from Event.models import Log

class LogLV(ListView):
    model = Log

class LogDV(DetailView):
    model = Log
