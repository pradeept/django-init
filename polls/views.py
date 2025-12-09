from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice

# --- Hard Way of building index, detail and result ---
# def index(request):
#     latest_questions = Question.objects.order_by("-pub_date")[:5]  # get first 5 polls
#     template = loader.get_template("polls/index.html")
#     context = {"latest_question_list":latest_questions}
#     return HttpResponse(template.render(context,request))

# def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Invalid question id.")
    # return render(request,"polls/detail.html",{"question":question})  # shortcut for rendering

    # shortcut for searching object and throwing 404 if not found
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, "polls/detail.html", {"question":question})

# def results(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, "polls/results.html", {"question": question})

# ---- Generic Views (provided by django for redundant and common cases)---
# For listing the objects based on a key
class IndexView(generic.ListView):
    # required otherwise, django will look for <app name>/<model name>_detail.html.
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
