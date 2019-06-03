from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
	asked_by = models.ForeignKey(User,on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	question = models.CharField(max_length=1024, unique=True)
	answered = models.BooleanField(default=False)

	def __str__(self):
		return self.question

	class Meta:
		ordering = ['-date_created']

class Answer(models.Model):
	answered_by = models.ForeignKey(User,on_delete=models.CASCADE)
	answer = models.CharField(max_length=1024)
	date_posted = models.DateTimeField(auto_now_add=True)
	is_correct = models.BooleanField(default=False)
	question = models.ForeignKey(Question,on_delete=models.CASCADE, default=None)
	likes = models.IntegerField(default=0)

	def __str__(self):
		return self.answer

	class Meta:
		ordering = ['likes']


class Upvote(models.Model):
	answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)


