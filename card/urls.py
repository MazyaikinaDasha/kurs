from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from . import models
from django.conf.urls import url

urlpatterns = [
    #path('', ListView.as_view(queryset=models.Card.objects.all(),template_name ="cards/cards.html" )),
    url('(?P<t_id>\d+)/$',  views.index, name='index'),
    url('new_card/',   views.card_new, name='card_new'),
    url('(?P<pk>\d+)/delet/$', views.delete, name='delete'),
    #url('delete/(?P<id>\d+)/',  views.delete, name='delete'),
    url(r'^(?P<id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<id>\d+)/stat/$', views.stat, name='stat'),
]
