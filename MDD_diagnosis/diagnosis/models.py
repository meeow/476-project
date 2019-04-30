from django.db import models
from django.utils import timezone

class Question(models.Model):
    def __str__(self):
        category = self.question_category
        text = self.question_text
        return text + "(Category: " + category + ")"

    def new_question(question_category, question_text):
        q = Question(question_category=question_category,
                     question_text=question_text, 
                     pub_date=timezone.now()
                     )
        q.save()

    question_text = models.CharField(max_length=800)
    pub_date = models.DateTimeField('date published')
    question_category = models.CharField(max_length=100, default='None')

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)