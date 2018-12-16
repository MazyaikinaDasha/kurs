from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, request
from django.views import View
from django.shortcuts import redirect
import django.contrib.sessions.middleware

from . import models
from . import forms


def index(request, t_id):
	cards = models.Card.objects.all().filter(top=t_id)
	request.session['t_id'] = t_id
	return render(request, "cards/cards.html", {'card': cards})


def card_new(request):
	if request.method == "POST":
		form = forms.CardForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.top_id = request.session.get('t_id')
			post.save()
			#statist = models.Statistic()
			#statist.card_id_id = post.id
			#statist.save()
			return redirect('index', t_id=post.top_id)
	else:
		form = forms.CardForm()
	return render(request, 'cards/new_card.html', {'form': form})

def delete(request, pk):
    card = get_object_or_404(models.Card, pk=pk)
    if request.method == 'POST':  # If method is POST,
        card.delete()  # delete the card.
        return redirect('/')
    return render(request, "index")


def edit(request, id):
	if request.method == "POST":
		#card = models.Card.objects.get(id=id)
		form = forms.CardForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.id = id
			post.top_id = request.session.get('t_id')
			post.save()
			return redirect('index', t_id=post.top_id)
	else:
		form = forms.CardForm()
	return render(request, 'cards/new_card.html', {'form': form})
def stat(request, id):
    statistic = models.Statistic.objects.filter(card_id = models.Card.objects.get(id=id))
    return render(request, "cards/stat.html",{'st': statistic})

