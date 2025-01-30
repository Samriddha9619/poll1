from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render

from .models import question
def index (request):
 latest_question_list = Question.objects.order_by("-pub_date")[:5]
 template= loader.get_template('index.html')
 context ={
  "Latest_question_list:":latest_question_list,
 }
 return render(template.render(context,request))
 return HttpResponse(template.render(context,request))
 output =", ".join([q.question_text for q in latest_question_list])
 return HttpResponse(output)
 return HttpResponse("Hello,this is the index page of the polls")
def detail(request,question_id):
 question = get_object_or_404(question,pk=question_id)
 return render(request,'detail.html',{'question':question})
 try:
  question = Question.objects.get(pk=question_id)
 except Question.DoesNotExist:
  raise Http404("Question does not exist")
 return render(request,'detail.html',{'question':question})
 return HttpResponse("You are looking at question %s." % question_id)
def result(request,question_id):
 response = " You're looking at the results of question %s."
 return HttpResponse(response%question_id)
def vote(request,question_id):
 return HttpResponse("You are voting on question %s."%question_id)

 
