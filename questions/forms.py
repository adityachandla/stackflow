from django import forms


class QuestionForm(forms.Form):
	question = forms.CharField(max_length=1024)


class AnswerForm(forms.Form):
	answer = forms.CharField(max_length=1024)
