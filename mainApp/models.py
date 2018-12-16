from django.db import models


# Create your models here.
#from card.models import Card


class Statistic(models.Model):
    class Meta():
        db_table = "statictic"

    statistic_id = models.AutoField(primary_key=True)
    statistic_success = models.IntegerField(default=0)
    statistic_unsuccess = models.IntegerField(default=0)
    card_id = models.ForeignKey('Card', on_delete=models.CASCADE)



class Card(models.Model):
    class Meta():
        db_table = "card"

    id = models.AutoField(primary_key=True)
    question = models.TextField(max_length=500)
    answer = models.TextField(max_length=500)
    top = models.ForeignKey('Topic', on_delete=models.CASCADE, )



    def __str__(self):
        return self.question

    def count (self):
        return Card.objects.all().count()

class Topic(models.Model):
    class Meta():
        db_table = "topic"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    time = models.TimeField
    dateView = models.DateField
    dateTest = models.DateField

    def __str__(self):
        return self.name


    def __del__(self):
        del self