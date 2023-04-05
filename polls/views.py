from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView

from polls.forms import QuestionForm
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
        if selected_choice.is_true:
            messages.add_message(request, messages.SUCCESS, 'Hello world.')
            return HttpResponse(f"<h1>{selected_choice.fun()}<hr>To'g'ri! Javoblar soni: {selected_choice.votes}</h1>")
        else:
            messages.add_message(request, messages.ERROR, 'God Bye.')
            return HttpResponse(
                f"<h1>{selected_choice.fun()}<hr> Noto'g'ri! Javoblar soni: {selected_choice.votes}</h1>")
    # return redirect("polls:questions_list")


class HomeListVies(ListView):
    model = Question
    template_name = 'polls/list_of_questions.html'


def question_add(request):
    form = QuestionForm(request.POST)
    if request.method == "POST":
        success_url = reverse_lazy('polls:homepage')
        if form.is_valid():
            form.save()
            return redirect("polls:questions_list")
    return render(request, 'polls/add_question.html', {"form": form})
