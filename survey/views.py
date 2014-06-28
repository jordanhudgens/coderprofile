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
      soln["X"] = "<a href='http://www.thinkful.com/' target='_blank'>Thinkful - Front End Development</a>"
      
    if soln["X"] == "thinkfulpython":
      soln["X"] = "<a href='http://www.thinkful.com/' target='_blank'>Thinkful - Python Web Development</a>"

    if soln["X"] == "thinkfulruby":
      soln["X"] = "<a href='http://www.thinkful.com/' target='_blank'>Thinkful - Ruby on Rails Web Development</a>"
      
    if soln["X"] == "thinkfulios":
      soln["X"] = "<a href='http://www.thinkful.com/' target='_blank'>Thinkful - iOS Mobile App Development</a>"
      
    if soln["X"] == "blocror":
      soln["X"] = "<a href='https://www.bloc.io/web-development' target='_blank'>Bloc - Ruby on Rails Web Development</a>"
      
    if soln["X"] == "blocfrontend":
      soln["X"] = "<a href='https://www.bloc.io/front-end-development' target='_blank'>Bloc - Front End Development</a>"

    if soln["X"] == "blocandroid":
      soln["X"] = "<a href='https://www.bloc.io/android' target='_blank'>Bloc - Android Mobile App Development</a>"
      
    if soln["X"] == "blocois":
      soln["X"] = "<a href='https://www.bloc.io/ios' target='_blank'>Bloc - iOS Mobile App Development</a>"
      
    if soln["X"] == "codementorpython":
      soln["X"] = "<a href='https://www.codementor.io/learn-python-online' target='_blank'>CodeMentor - Python Web Development</a>"
      
    if soln["X"] == "codementorror":
      soln["X"] = "<a href='https://www.codementor.io/learn-ruby-on-rails-online' target='_blank'>CodeMentor - Ruby on Rails Web Development</a>"
      
    if soln["X"] == "codementorios":
      soln["X"] = "<a href='https://www.codementor.io/learn-ios-development' target='_blank'>CodeMentor - iOS Mobile App Development</a>"

    if soln["X"] == "codementorandroid":
      soln["X"] = "<a href='https://www.codementor.io/learn-android-development' target='_blank'>CodeMentor - Android Mobile App Development</a>"
      
    if soln["X"] == "codementorfrontend":
      soln["X"] = "<a href='https://www.codementor.io/learn-html' target='_blank'>CodeMentor - Front End Development</a>"
      
    if soln["X"] == "codechef":
      soln["X"] = "<a href='http://www.codechef.com/' target='_blank'>CodeChef - Competitive Coding Challenges</a>"
      
    if soln["X"] == "codecademyhtml":
      soln["X"] = "<a href='http://www.codecademy.com/tracks/web' target='_blank'>Codecademy - HTML Training Track</a>"
      
    if soln["X"] == "codecademyjquery":
      soln["X"] = "<a href='http://www.codecademy.com/tracks/jquery' target='_blank'>Codecademy - jQuery Training Track</a>"

    if soln["X"] == "codecademyror":
      soln["X"] = "<a href='http://www.codecademy.com/tracks/ruby' target='_blank'>Codecademy - Ruby Programming Track</a>"
      
    if soln["X"] == "codecademypython":
      soln["X"] = "<a href='http://www.codecademy.com/tracks/python' target='_blank'>Codecademy - Python Programming Track</a>"
      
    if soln["X"] == "codecademyphp":
      soln["X"] = "<a href='http://www.codecademy.com/tracks/php' target='_blank'>Codecademy - PHP Programming Track</a>"
      
    if soln["X"] == "codeschoolror":
      soln["X"] = "<a href='https://www.codeschool.com/paths/ruby' target='_blank'>CodeSchool - Ruby on Rails Development</a>"
      
    if soln["X"] == "codeschoolfrontend":
      soln["X"] = "<a href='https://www.codeschool.com/paths/html-css' target='_blank'>CodeSchool - Front End Development</a>"
      
    if soln["X"] == "codeschoolios":
      soln["X"] = "<a href='https://www.codeschool.com/paths/ios' target='_blank'>CodeSchool - iOS Mobile App Development</a>"
      
    if soln["X"] == "rubymonk":
      soln["X"] = "<a href='https://rubymonk.com/' target='_blank'>Ruby Monk - Ruby Programming Training</a>"
      
    if soln["X"] == "treehousefrontend":
      soln["X"] = "<a href='http://teamtreehouse.com/library/topic:html' target='_blank'>Team Treehouse - Front End Development</a>"
      
    if soln["X"] == "treehouseror":
      soln["X"] = "<a href='http://teamtreehouse.com/library/topic:ruby' target='_blank'>Team Treehouse - Ruby on Rails Development</a>"
      
    if soln["X"] == "treehousephp":
      soln["X"] = "<a href='http://teamtreehouse.com/library/topic:php' target='_blank'>Team Treehouse - PHP Web Development</a>"
      
    if soln["X"] == "treehouseandroid":
      soln["X"] = "<a href='http://teamtreehouse.com/library/topic:android' target='_blank'>Team Treehouse - Android Mobile App Development</a>"
      
    if soln["X"] == "treehouseios":
      soln["X"] = "<a href='http://teamtreehouse.com/library/topic:ios' target='_blank'>Team Treehouse - iOS Mobile App Development</a>"
      
    if soln["X"] == "udacitypython1":
      soln["X"] = "<a href='https://www.udacity.com/course/cs101' target='_blank'>Udacity - Intro to Python Web Development</a>"
      
    if soln["X"] == "udacitypython2":
      soln["X"] = "<a href='http://teamtreehouse.com/library/topic:android' target='_blank'>Udacity - Intermediate Python Web Development</a>"
      
    if soln["X"] == "udacityfrontend":
      soln["X"] = "<a href='https://www.udacity.com/course/ud248' target='_blank'>Udacity - Front End Development</a>"
      
    if soln["X"] == "javaposse":
      soln["X"] = "<a href='http://javaposse.com/' target='_blank'>Android Podcasts</a>"
      
    if soln["X"] == "stackexchange":
      soln["X"] = "<a href='http://blog.stackoverflow.com/category/podcasts/' target='_blank'>StackExchange - Programming Podcasts</a>"
      
    if soln["X"] == "hansel":
      soln["X"] = "<a href='http://www.hanselminutes.com/' target='_blank'>Hansel Minutes - Programming Podcasts</a>"
      
    if soln["X"] == "twittv":
      soln["X"] = "<a href='http://twit.tv/sn' target='_blank'>Team Twit.tv - Programming Podcasts</a>"
      
    if soln["X"] == "thechangelog":
      soln["X"] = "<a href='http://thechangelog.com/podcast/' target='_blank'>The Change Log - Open Source Podcasts</a>"
      
    if soln["X"] == "phptownhall":
      soln["X"] = "<a href='http://phptownhall.com/' target='_blank'>PHP Town Hall - PHP Programming Podcasts</a>"
      
    if soln["X"] == "rubyrogues":
      soln["X"] = "<a href='http://rubyrogues.com/' target='_blank'>Ruby Rogues - Ruby Programming Podcasts</a>"

    
    ## *************************** END *************************** ##
    classSuggested.append(soln["X"])
  
  email = settings.support_email
  return render(request, 'confirm.html', {'uuid':uuid, "email": email, 'projectdesired':projectdesired, 'educationlevel':educationlevel, 'programmingexperience':programmingexperience, 'learningpriority':learningpriority, 'employmentstatus':employmentstatus, 'featuredriven':featuredriven, 'mentordriven':mentordriven, 'audience':audience, 'competitive':competitive, 'internetstatus':internetstatus, 'motivation':motivation, 'machine':machine, 'budget':budget, 'hoursfree':hoursfree, 'timeframe':timeframe, 'classSuggested':classSuggested, 'classURL':classURL})

def privacy(request):
  return render(request, 'privacy.html')


