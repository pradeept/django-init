from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from polls.models import Question
# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]  # get first 5 polls
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list":latest_questions}
    return HttpResponse(template.render(context,request))

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Invalid question id.")
    # return render(request,"polls/detail.html",{"question":question})  # shortcut for rendering

    # shortcut for searching object and throwing 404 if not found
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question":question})

def results(request, question_id):
    response = "You're looking at the results of the question %s "
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." %question_id)
