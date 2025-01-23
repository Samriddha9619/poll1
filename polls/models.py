import datetime 
from django.db import models
from django.utils import timezone

class question(models.Model):
    def was_made_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date published")
class choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)