from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.
"""
This is the initial index view:
def index(request):
    return HttpResponse("Hello world. You are at the polls index.")
In the tutorial, a new index view is created. This also entails changing
the code because the PAGE DESIGN IS HARD-CODED IN THE VIEW.
The new index should display the latest 5 poll questions in the system,
separated by commas and according to publication date (see code def index).
The tutorial uses a Django template to SEPARATE THE DESIGN from Python by
creating a template that the view can use:
"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %x."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
