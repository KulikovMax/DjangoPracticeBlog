from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import *


def index(request):
    questions_list = Question.objects.all()
    paginator = Paginator(questions_list, 10)

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render(request, 'polls/index.html', {'questions': questions})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You did not select a choice"
        })
    else:
        choice.votes += 1
        choice.save()

    return HttpResponseRedirect(reverse('polls_results', args=(question.id,)))


def add_poll(request):
    question = Question()
    question.save()
    return render(request, 'polls/add_poll.html', {'question': question})


def save_poll(request, question_id):
    question = Question.objects.get(pk=question_id)
    question.text = request.POST['question_text']
    question.save()
    Choice(question=question, text=request.POST['choice_1']).save()
    Choice(question=question, text=request.POST['choice_2']).save()

    return HttpResponseRedirect(reverse('polls_detail', args=(question.id,)))




