"""mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import ListView,DetailView
from . import models
urlpatterns = [
    path('', ListView.as_view(queryset=models.Topic.objects.all(),template_name ="mainApp/homePage.html")),
    url('study/(?P<t_id>\d+)/',  views.index, name='index'),
    path('test/', ListView.as_view(queryset=models.Card.objects.all(),template_name ="mainApp/test.html")),
    url('^new_topic/', views.topic_new, name='topic_new'),
    url('(?P<pk>\d+)/delete/', views.delet, name='delet'),
    path('statistic/', ListView.as_view(queryset=models.Card.objects.all(),template_name ="mainApp/statistic.html")),
    url('add_know/(?P<card_id>\d+)/',views.add_know, name='add_know')

]
#/(?P<card_id>\d+)/