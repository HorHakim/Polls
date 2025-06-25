from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import F
from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # question_object = Question.objects.get(pk=question_id)
    question_object = get_object_or_404(Question, pk=question_id)
    context = {"question_object": question_object}
    return render(request, "polls/details.html", context)





def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice_id = request.POST["choice"]
        selected_choice = question.choice_set.get(pk=selected_choice_id)

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/details.html",
            {
                "question_object": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



def results(request, question_id):
    question_object = get_object_or_404(Question, pk=question_id)
    context = {"question_object": question_object}
    return render(request, "polls/results.html", context)