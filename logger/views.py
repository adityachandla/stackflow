from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def signin(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password"])
			if user is not None:
				login(request,user)
				messages.success(request,"Successfully logged in")
				return redirect('home')
			else:
				messages.info(request, "Invlaid username or passsword")
				return redirect('login')
		messages.danger(request,"invlid form submission")
		return redirect('login')
	else:
		form = LoginForm()
	context = {"form" : form}
	return render(request,"logger/signin.html",context)


def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("login")
	else:
		form = UserCreationForm()
	context = {"form":form}
	return render(request,"logger/signup.html",context)



def signout(request):
	logout(request)
	return redirect('login')



