from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.contrib import messages
import datetime
import settings

from models import Question, Survey, Category, Response
from forms import ResponseForm, InitialResponseForm
from pyswip import Prolog


def Index(request):
  survey = Survey.objects.get(id=1)  
  if request.method == 'POST':
    form = InitialResponseForm(request.POST, survey=survey)
    if form.is_valid():
      response = form.save()
      return HttpResponseRedirect("/survey/%s/%s" % (survey.id, response.id))
  else:
      form = InitialResponseForm(survey=survey)
  return render(request, 'index.html', {'response_form': form})

def SurveyDetail(request, survey_id, response_id):
  survey = Survey.objects.get(id=survey_id)
  response = Response.objects.get(id=response_id)
  category_items = Category.objects.filter(survey=survey)
  categories = [c.name for c in category_items]
  print 'categories for this survey:'
  print categories
  if request.method == 'POST':
    form = ResponseForm(request.POST, survey=survey, response=response)
    if form.is_valid():
      response = form.save()
      return HttpResponseRedirect("/confirm/%s" % response.interview_uuid)
  else:
    form = ResponseForm(survey=survey, response=response)
    #print form
    # TODO sort by category
  return render(request, 'survey.html', {'response_form': form, 'survey': survey, 'response': response, 'categories': categories})

def Confirm(request, uuid):
  p = Prolog()
  p.consult('/home/jordanhudgens/code/coderprofile/survey/knowledgebase.pl')
  
  for soln in p.query("projectdesired(X)."):
    projectdesired = soln["X"]
      
  for soln in p.query("education(X)."):
    educationlevel = soln["X"]
    
  for soln in p.query("experience(X)."):
    programmingexperience = soln["X"]
      
  for soln in p.query("priority(X)."):
    learningpriority = soln["X"]

  for soln in p.query("employment(X)."):
    employmentstatus = soln["X"]
      
  for soln in p.query("featuredriven(X)."):
    featuredriven = soln["X"]

  for soln in p.query("mentor(X)."):
    mentordriven = soln["X"]
      
  for soln in p.query("targetaudience(X)"):
    audience = soln["X"]

  for soln in p.query("competitive(X)."):
    competitive = soln["X"]
      
  for soln in p.query("highspeedinternet(X)."):
    internetstatus = soln["X"]

  for soln in p.query("motivation(X)."):
    motivation = soln["X"]

  for soln in p.query("machine(X)."):
    machine = soln["X"]
    
  for soln in p.query("budget(X)."):
    budget = soln["X"]

  for soln in p.query("hoursfree(X)."):
    hoursfree = soln["X"]

  for soln in p.query("timeframe(X)."):
    timeframe = soln["X"]
    
  # Will need to be changed to data structure that can hold multiple values
  classSuggested = []
  classURL = []

  for soln in p.query("classSuggestion(X)."):
  
    ## ************** CHANGE PROLOG TERMS TO LINKS *************** ##
    
    if soln["X"] == "thinkfulfrontend":
      soln["X"] = "<a href='http://www.thinkful.com/'>Thinkful - Front End Development</a>"
      
    if soln["X"] == "thinkfulpython":
      soln["X"] = "<a href='http://www.thinkful.com/'>Thinkful - Python Web Development</a>"

    if soln["X"] == "thinkfulruby":
      soln["X"] = "<a href='http://www.thinkful.com/'>Thinkful - Ruby on Rails Web Development</a>"



    
    ## *************************** END *************************** ##
    classSuggested.append(soln["X"])
  
  email = settings.support_email
  return render(request, 'confirm.html', {'uuid':uuid, "email": email, 'projectdesired':projectdesired, 'educationlevel':educationlevel, 'programmingexperience':programmingexperience, 'learningpriority':learningpriority, 'employmentstatus':employmentstatus, 'featuredriven':featuredriven, 'mentordriven':mentordriven, 'audience':audience, 'competitive':competitive, 'internetstatus':internetstatus, 'motivation':motivation, 'machine':machine, 'budget':budget, 'hoursfree':hoursfree, 'timeframe':timeframe, 'classSuggested':classSuggested, 'classURL':classURL})

def privacy(request):
  return render(request, 'privacy.html')


