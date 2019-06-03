from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Answer, Question, Upvote
from .forms import QuestionForm,AnswerForm
from django.contrib import messages
from django.http import JsonResponse,HttpResponseRedirect

@login_required
def home(request):
	ques_set = Question.objects.all()
	context = {"questions":ques_set}
	return render(request,"questions/home.html",context)


@login_required
def question(request,qpk):
	ques = Question.objects.get(pk=qpk)
	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			ans = Answer(answered_by=request.user,question=ques,answer=form.cleaned_data["answer"])
			ans.save()
			ques.answered = True
			ques.save()
		return redirect("home")
	else:
		form = AnswerForm()
	context = {"question":ques, "answers": ques.answer_set.all(), "form":form}
	return render(request,"questions/que.html",context)


@login_required
def ask(request):
	if request.method == "POST":
		form = QuestionForm(request.POST)
		if form.is_valid():
			q = Question(asked_by=request.user,question=form.cleaned_data["question"])
			try:
				q.save()
			except:
				messages.warning(request,"Question already asked")
				return redirect("home")
			messages.success(request,"Created your question")
			return redirect("home")
	else:
		form = QuestionForm()
	context = {"form":form}
	return render(request,"questions/ask.html",context)


@login_required
def like(request,apk):
	return JsonResponse({"likes":getlikes(apk,request)})


def getlikes(apk,request=None):
	#returns an integer
	answer = Answer.objects.get(pk=apk)
	if Upvote.objects.filter(user=request.user).filter(answer=answer).count() == 0:
		print("liking the question")
		u = Upvote(user=request.user, answer=answer)
		u.save()
		answer.likes = answer.likes + 1;
		answer.save()
	return Upvote.objects.filter(answer=answer).count()

