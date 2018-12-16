from django.core.serializers import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from . models import *
from django.views.generic import ListView,DetailView
from django.shortcuts import redirect
from . import models
from . import forms
import datetime


def index(request, t_id):
	cards = models.Card.objects.all().filter(top = t_id)
	topic = models.Topic.objects.all().filter(id = t_id)
	topic.dateView =datetime.date.today()
	return render(request, "mainApp/study.html", {'cards': cards})


def topic_new(request):
	if request.method == "POST":
		form = forms.TopicForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('index', t_id=post.id)
	else:
		form = forms.TopicForm()
	return render(request, 'mainApp/top_edit.html', {'form': form})


def delet(request, pk):
    top = get_object_or_404(models.Topic, pk=pk)
    if request.method == 'POST':  # If method is POST,
        top.delete()  # delete the card.
        return redirect('/')
    return render(request, "index")


def add_know(request, card_id):

    statistic = models.Statistic.objects.get(card_id= models.Card.objects.get(id=card_id))
    statistic.statistic_success += 1 # Прибавляет единицу
    statistic.save() # сохраняет
    return HttpResponse()