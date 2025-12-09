from typing import override
from django.db import models

# Create your models here.

class Question(models.Model):
    """
        It’s important to add __str__() methods to your models, not only for your own convenience
        when dealing with the interactive prompt, but also because objects’ representations are used
        throughout Django’s automatically-generated admin.
    """
    def __str__(self):
        return self.question_text

    # helper function to later use in views or templates.
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date published")

class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)
