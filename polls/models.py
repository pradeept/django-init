from django.db import models

# Create your models here.

# class Person(models.Model):
#     name = models.CharField(max_length=100, default="temp")
#     age = models.IntegerField(default=18)
#     email = models.EmailField(blank=True)
#     address = models.TextField(null=True)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
