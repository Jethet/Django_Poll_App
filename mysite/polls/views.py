from django.http import HttpResponse,, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You are looking at the results of question %x."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question,, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You did not select a choice.'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with
        #   POST data. This prevents data from being posted twice if a user
        #   hits the Back button:
        return HttpResponseRedirect(reverse('polls:results', args=(question_id)))
