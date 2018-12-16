from django import forms
from . import models
class TopicForm (forms.ModelForm):
    class Meta:
        model = models.Topic
        fields = ('name',)
