from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'blog/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blog/detail.html', { 'question': question })

def results(request, question_id):
    response = "You were looking at results of question  %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You were voting on question %s." % question_id)