from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:1]
    output = ', ' .join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)    

def results(request, question_id):
    response = "You were looking at results of question  %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You were voting on question %s." % question_id)