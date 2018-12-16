from django import forms
from . import models
class CardForm (forms.ModelForm):
    class Meta:
        model = models.Card
        fields = ('question', 'answer',)

