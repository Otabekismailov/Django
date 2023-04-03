from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from polls.models import Question, Choice


# Create your views here.
def homepage(request):
    return render(request, 'home.html')


def questions_list(request):
    question = Question.objects.all()
    context = {
        'question': question
    }
    return render(request, 'polls/questions.html', context=context)


def questions_detile(request, pk):
    question = get_object_or_404(Question, id=pk)
    # questions = Question.objects.get(id=pk)
    context = {
        'question': question,
    }
    return render(request, 'polls/questions_detile.html', context=context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/questions_detile.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # print(request.POST)
        # return render(request, 'polls/results.html', context={'choice': question})
        results(selected_choice.id)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(question_id):
    question = get_object_or_404(Choice, pk=question_id)
    print(question.text)
    # # try:
    # selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # print(selected_choice.text)

    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/questions_detile.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    return render(question_id, 'polls/results.html', context={'choice': question})
