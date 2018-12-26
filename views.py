from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import random
from django.views import generic
from .models import Question, Choice


# Create your views here.

#class IndexView(generic.ListView):
    #template_name = 'polls/index.html'
    #context_object_name = 'latest_question_list'
    #def get_queryset(self):
        #return Question.objects.all()[:]

#random.SystemRandom().randint(1000000000000000,9999999999999999)


def view(request,question_id):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    round=random.SystemRandom().randint(1000000000000000,9999999999999999)
    HttpResponse.__setitem__(round,round)
    response=render(request, 'polls/index.html', context)
    HttpResponse.set_cookie(onetimecookie, value='', max_age=None, expires=None, path='/', domain=None, secure=None,
                            httponly=False, samesite=None)
    return response



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    roundvalue=random.SystemRandom().randint(1000000000000000,9999999999999999)
    response=render(request, 'polls/detail.html', {'question': question}
    HttpResponse.__setitem__(round, roundvalue)
    HttpResponse.set_cookie(onetimecookie, value='', max_age=None, expires=None, path='/', domain=None, secure=None,
                            httponly=False, samesite=None)
    return response

#class DetailView2(generic.DetailView):
    #context_object_name = 'question'
    #model = Question
    #template_name = 'polls/detail.html'


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    response=render(request, 'polls/results.html', {'question': question})
    roundvalue=random.SystemRandom().randint(1000000000000000,9999999999999999)
    HttpResponse.__setitem__(round, roundvalue)
    HttpResponse.set_cookie(onetimecookie, value='', max_age=None, expires=None, path='/', domain=None, secure=None,
                            httponly=False, samesite=None)
    return response
#class ResultView(generic.DetailView):
    #context_object_name = 'question'
    #model = Question
    #template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        context = {'question': question, 'error_message': "You didn't select a choice."}
        render(request, 'polls\detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        roundvalue = random.SystemRandom().randint(1000000000000000, 9999999999999999)
        HttpResponse.__setitem__(round, roundvalue)
        HttpResponse.set_cookie(onetimecookie, value='', max_age=None, expires=None, path='/', domain=None, secure=None,
                                httponly=False, samesite=None)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

