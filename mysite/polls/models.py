from django.db import models


class Question(models.Model):
    text = models.TextField(blank=True)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
