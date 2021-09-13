from django.shortcuts import render

# Create your views here.

from polls.models import Question

def index(request):
    latest_question_list = Question.object.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request):
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/detail.html', context)

def results(request):
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/results.html', context)