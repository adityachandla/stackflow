from django.urls import path
from . import views

urlpatterns = [
	path('home', views.home,name="home"),
	path('question/<int:qpk>',views.question, name="question"),
	path('ask',views.ask,name='ask'),
	path('like/<int:apk>',views.like,name="like"),

]