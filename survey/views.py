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
      soln["X"] = "<span class='logoBorder'><img src='http://columbus.startupweekend.org/files/2013/07/Thinkful-Logo-Medium-300x60.png' width='100px'></span><p><a href='http://www.thinkful.com/' target='_blank'>Thinkful - Front End Development</a>: Build eight sleek and interactive websites with HTML, CSS, and JavaScript. Learn web development and apply UX design principles to create user-friendly products. Learn faster from expert developers through one-on-one online sessions.</p>"
      
    if soln["X"] == "thinkfulpython":
      soln["X"] = "<span class='logoBorder'><img src='http://columbus.startupweekend.org/files/2013/07/Thinkful-Logo-Medium-300x60.png' width='100px'></span><p><a href='http://www.thinkful.com/' target='_blank'>Thinkful - Python Web Development</a>: Program back-end web applications with Flask and deploy to Heroku. Learn object-oriented programming and use test driven development to produce reliable, maintainable code. Learn faster from expert developers through one-on-one online sessions."

    if soln["X"] == "thinkfulruby":
      soln["X"] = "<span class='logoBorder'><img src='http://columbus.startupweekend.org/files/2013/07/Thinkful-Logo-Medium-300x60.png' width='100px'></span><p><a href='http://www.thinkful.com/' target='_blank'>Thinkful - Ruby on Rails Web Development</a>: Build full-stack web apps using the popular framework Ruby on Rails - the quickest and most powerful way to build web apps. Launch a clone of Wikipedia from scratch and dive into the Twitter codebase. Learn faster from expert developers through one-on-one online sessions."
      
    if soln["X"] == "thinkfulios":
      soln["X"] = "<span class='logoBorder'><img src='http://columbus.startupweekend.org/files/2013/07/Thinkful-Logo-Medium-300x60.png' width='100px'></span><p><a href='http://www.thinkful.com/' target='_blank'>Thinkful - iOS Mobile App Development</a>: Build and launch iOS 7 and iOS 8 apps from scratch. You will learn to program in Swift and to use Xcode to build apps for the iPhone and iPad. By the end of the course, you will submit your work to the Apple App Store! Learn faster from expert developers through one-on-one online sessions.</p>"
      
    if soln["X"] == "blocror":
      soln["X"] = "<span class='logoBorder'><img src='http://static.squarespace.com/static/51ca1de9e4b04a2426bf6398/t/52d89fe0e4b0281856c67553/1389928416329/205329v1-max-250x250.jpg' width='100px'></span><p><a href='https://www.bloc.io/web-development' target='_blank'>Bloc - Ruby on Rails Web Development</a>: Working with an experienced mentor three times per week you will ship real web apps including versions of Wikipedia, Google Analytics, and Digg. Build a Wiki-as-a-service (SaaS) app that uses the Stripe API for payment processing. Implement email logic and social networking functionality as you build your own Digg social bookmarking app. And strengthen client-side skills as you build an analytics app with a back-end reporting dashboard. For your last two weeks, you and your mentor will work on a capstone project of your choice. This project will tie together and showcase the skills that you have learned as part of the course.</p>"
      
    if soln["X"] == "blocfrontend":
      soln["X"] = "<span class='logoBorder'><img src='http://static.squarespace.com/static/51ca1de9e4b04a2426bf6398/t/52d89fe0e4b0281856c67553/1389928416329/205329v1-max-250x250.jpg' width='100px'></span><p><a href='https://www.bloc.io/front-end-development' target='_blank'>Bloc - Front End Development</a>: Working with an experienced mentor three times per week you will learn frontend frameworks and libraries including jQuery, AngularJS, and JavaScript testing frameworks. For your last two weeks, you and your mentor will work on a capstone project of your choice. This project will tie together and showcase the skills that you have learned as part of the course.</p>"

    if soln["X"] == "blocandroid":
      soln["X"] = "<span class='logoBorder'><img src='http://static.squarespace.com/static/51ca1de9e4b04a2426bf6398/t/52d89fe0e4b0281856c67553/1389928416329/205329v1-max-250x250.jpg' width='100px'></span><p><a href='https://www.bloc.io/android' target='_blank'>Bloc - Android Mobile App Development</a>: Working with an experienced mentor three times per week you will choose from a menu of apps to build, each one designed to reinforce and build upon your Android developer skills. Dive deeper into APIs and integrations with Flurry Analytics, in-app purchases, and Google AdMob in-app advertising. As a capstone project, you will choose an app idea of your own to build. To complete the capstone, design, develop, test, and launch this app to the Google Play store.</p>"
      
    if soln["X"] == "blocois":
      soln["X"] = "<span class='logoBorder'><img src='http://static.squarespace.com/static/51ca1de9e4b04a2426bf6398/t/52d89fe0e4b0281856c67553/1389928416329/205329v1-max-250x250.jpg' width='100px'></span><p><a href='https://www.bloc.io/ios' target='_blank'>Bloc - iOS Mobile App Development</a>: Working with an experienced mentor three times per week you will choose from a menu of apps to build, each one designed to reinforce and build upon your iOS developer skills. Build your first iPad app. Integrate Apple tools like Maps, Game Center, and Auto Layout to make your app beautiful, reliable, and fun. As a capstone project, you will choose an app idea of your own to build. To complete the capstone, design, develop, test, and submit this app to the App Store.</p>"
      
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
      soln["X"] = "<a href='http://javaposse.com/' target='_blank'>Java Posse - Android Podcasts</a>"
      
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
      
    if soln["X"] == "udemyrorbiz":
      soln["X"] = "<a href='https://www.udemy.com/comprehensive-ruby-on-rails' target='_blank'>Edutechional - Ruby on Rails Business Application Development</a>"
      
    if soln["X"] == "udemyfrontend1":
      soln["X"] = "<a href='https://www.udemy.com/web-development-tutorials' target='_blank'>Stone River eLearning - Front End Development</a>"
      
    if soln["X"] == "udemyphp1":
      soln["X"] = "<a href='https://www.udemy.com/become-a-certified-web-developer' target='_blank'>LearnToProgram.TV - PHP Web Development</a>"
      
    if soln["X"] == "udemyandroid1":
      soln["X"] = "<a href='https://www.udemy.com/learn-by-doing-android-for-beginners' target='_blank'>Ragunath Jawahar - Android Mobile App Development</a>"
      
    if soln["X"] == "udemyios1":
      soln["X"] = "<a href='https://www.udemy.com/iosdevelopment' target='_blank'>The App Dojo - iOS Mobile App Development</a>"
      
    if soln["X"] == "udemyios2":
      soln["X"] = "<a href='https://www.udemy.com/the-complete-ios-7-course-learn-by-building-14-apps' target='_blank'>John Nichols - iOS Mobile App Development</a>"
      
    if soln["X"] == "udemyios4":
      soln["X"] = "<a href='https://www.udemy.com/swift-learn-apples-new-programming-language-by-examples' target='_blank'>Rick Walter - iOS Mobile App Development</a>"
      
    if soln["X"] == "udemyios5":
      soln["X"] = "<a href='https://www.udemy.com/projects-in-ios' target='_blank'>Eduonix Learning Solutions - iOS Mobile App Development</a>"
      
    if soln["X"] == "udemyrorsoc":
      soln["X"] = "<a href='https://www.udemy.com/create-and-deploy-a-web-app-in-3-hours' target='_blank'>Tiago Martins - Ruby on Rails Social App Development</a>"
      
    if soln["X"] == "udemyios6":
      soln["X"] = "<a href='https://www.udemy.com/learn-ios-programming-the-basics' target='_blank'>Eduonix Learning Solutions - Intro to iOS Mobile App Development</a>"
      
    if soln["X"] == "udemyfrontend2":
      soln["X"] = "<a href='https://www.udemy.com/webdevelopment101_html' target='_blank'>Brian Gorman - Front End Development</a>"
      
    if soln["X"] == "udemygames1":
      soln["X"] = "<a href='https://www.udemy.com/learn-c-game-development' target='_blank'>Luka Horvat - C++ Game Development</a>"
      
    if soln["X"] == "udemygames2":
      soln["X"] = "<a href='https://www.udemy.com/responsive-html5-theme-development' target='_blank'>Lamin Sanneh - HTML5 Game Development</a>"
      
    if soln["X"] == "udemyphp2":
      soln["X"] = "<a href='https://www.udemy.com/php-programming-basics' target='_blank'>Stone River eLearning - PHP Web Application Development</a>"
      
    if soln["X"] == "udemyfrontend3":
      soln["X"] = "<a href='https://www.udemy.com/learn-to-build-beautiful-html5-and-css3-websites-in-1-month' target='_blank'>Ryan Bonhardt - Front End Development</a>"
      
    if soln["X"] == "udemyfrontend4":
      soln["X"] = "<a href='https://www.udemy.com/android-programming-for-beginners' target='_blank'>Mark Lassoff - Android Mobile App Development</a>"
      
    if soln["X"] == "khangames1":
      soln["X"] = "<a href='https://www.khanacademy.org/computing/cs/programming' target='_blank'>Khan Academy - Intro to Game Development</a>"
      
    if soln["X"] == "khangames2":
      soln["X"] = "<a href='https://www.khanacademy.org/computing/cs/programming-games-visualizations' target='_blank'>Khan Academy - Game Development</a>"
      
    if soln["X"] == "khangames3":
      soln["X"] = "<a href='https://www.khanacademy.org/computing/cs/programming-natural-simulations' target='_blank'>Khan Academy - Intermediate Game Development</a>"
      
    if soln["X"] == "codeplayer":
      soln["X"] = "<a href='http://thecodeplayer.com/' target='_blank'>CodePlayer - Front End Development</a>"
      
    if soln["X"] == "hardwaypython1":
      soln["X"] = "<a href='http://learnpythonthehardway.org' target='_blank'>Learn Python the Hard Way - Python Programming Manual</a>"
      
    if soln["X"] == "hardwaypython1":
      soln["X"] = "<a href='http://learnpythonthehardway.org' target='_blank'>Learn Python the Hard Way - Python Programming Video Series</a>"
      
    if soln["X"] == "railscasts":
      soln["X"] = "<a href='http://railscast.com' target='_blank'>Railscasts - Ruby on Rails Web Development</a>"

    
    ## *************************** END *************************** ##
    classSuggested.append(soln["X"])
  
  email = settings.support_email
  return render(request, 'confirm.html', {'uuid':uuid, "email": email, 'projectdesired':projectdesired, 'educationlevel':educationlevel, 'programmingexperience':programmingexperience, 'learningpriority':learningpriority, 'employmentstatus':employmentstatus, 'featuredriven':featuredriven, 'mentordriven':mentordriven, 'audience':audience, 'competitive':competitive, 'internetstatus':internetstatus, 'motivation':motivation, 'machine':machine, 'budget':budget, 'hoursfree':hoursfree, 'timeframe':timeframe, 'classSuggested':classSuggested, 'classURL':classURL})

def privacy(request):
  return render(request, 'privacy.html')


