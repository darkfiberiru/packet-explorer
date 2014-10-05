from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=30)
    difficulty = models.ForeignKey('Difficulty')
    pcap =  models.CharField(max_length=30)
    category = models.ForeignKey('Category')
    hint = models.CharField(max_length=200)

class Pool(models.Model):
    question = models.ForeignKey('Question')
    category = models.ForeignKey('Category')
    difficulty = models.ForeignKey('Difficulty')
    user = models.ForeignKey(User)
    correct = models.BooleanField()
    hint = models.BooleanField()

    

class Difficulty(models.Model):
   points = models.IntegerField()
   active = models.BooleanField()

class Category(models.Model):
   adjustment = models.IntegerField()
   active = models.BooleanField()
   name = models.CharField(max_length=20)

