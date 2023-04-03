from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('data published')

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    is_true = models.BooleanField(default=False)

    def fun(self):
        if self.is_true == True:
            return "To'g'ri Javob "
        else:
            return "No'to'gri Javob"

    def __str__(self):

        return f'{self.question}-{self.text}-{self.fun()} '
