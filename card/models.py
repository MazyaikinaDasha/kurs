from django.db import models, transaction
from django.db.models import signals

# Create your models here.
from mainApp.models import Card


class Statistic(models.Model):
    class Meta():
        db_table = "statictic"

    statistic_id = models.AutoField(primary_key=True)
    statistic_success = models.IntegerField(default=0)
    statistic_unsuccess = models.IntegerField(default=0)
    card_id = models.ForeignKey('Card', on_delete=models.CASCADE)

    def s(self):
        return self.statistic_success+self.statistic_unsuccess

class Card(models.Model):
    class Meta():
        db_table = "card"

    id = models.AutoField(primary_key=True)
    question = models.TextField(max_length=500)
    answer = models.TextField(max_length=500)
    top = models.ForeignKey('Topic', on_delete=models.CASCADE, )

    def save(self, *args, **kwargs):
        super(Card, self).save(*args, **kwargs)  # Call the "real" save() method.
        Statistic.objects.create(card_id =self)

    def __str__(self):
        return self.question


class Topic(models.Model):
    class Meta():
        db_table = "topic"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    time = models.TimeField(default=0)
    dateView = models.DateField(default=0)
    dateTest = models.DateField(default=0)

    def __str__(self):
        return self.name

    def __del__(self):
        del self
