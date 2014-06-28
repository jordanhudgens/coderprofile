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
      soln["X"] = "<span class='logoBorder'><img src='http://cdn.geekwire.com/wp-content/uploads/codementor-logo-2.png' width='100px'></span><p><a href='https://www.codementor.io/learn-python-online' target='_blank'>CodeMentor - Python Web Development</a>: Our experienced mentors can teach Python for beginners, and you have an opportunity to learn PYTHON programming quickly if you have never programmed at all or never programmed in this language before. Of course, more advanced training can provide PYTHON help for experienced programmers too.</p>"
      
    if soln["X"] == "codementorror":
      soln["X"] = "<span class='logoBorder'><img src='http://cdn.geekwire.com/wp-content/uploads/codementor-logo-2.png' width='100px'></span><p><a href='https://www.codementor.io/learn-ruby-on-rails-online' target='_blank'>CodeMentor - Ruby on Rails Web Development</a>: Codementor has top Ruby on Rails experts from all over the world to help you learn Ruby on Rails online. Our experts can help learners of all skill levels, from beginners tackling early challenges to experienced developers who need help on specific problems.</p>"
      
    if soln["X"] == "codementorios":
      soln["X"] = "<span class='logoBorder'><img src='http://cdn.geekwire.com/wp-content/uploads/codementor-logo-2.png' width='100px'></span><p><a href='https://www.codementor.io/learn-ios-development' target='_blank'>CodeMentor - iOS Mobile App Development</a>: Codementor provides iOS expert help to help you learn iOS development more effectively. Whether you're creating a brand new native app or using technologies such as PhoneGap, Codementor can help you learn iPhone app development and build projects faster with live 1:1 help.</p>"

    if soln["X"] == "codementorandroid":
      soln["X"] = "<span class='logoBorder'><img src='http://cdn.geekwire.com/wp-content/uploads/codementor-logo-2.png' width='100px'></span><p><a href='https://www.codementor.io/learn-android-development' target='_blank'>CodeMentor - Android Mobile App Development</a>: Codementor provides Android expert help to help you learn Android development more effectively: java, android layout, eclipse, listview, android intent, android fragments, android listview, and more. Learning Android Development to create native mobile apps in Java or with technologies such as PhoneGap can be challenging if you're doing this alone. Codementor helps you learn Android programming with live 1:1 help and build projects faster.</p>"
      
    if soln["X"] == "codementorfrontend":
      soln["X"] = "<span class='logoBorder'><img src='http://cdn.geekwire.com/wp-content/uploads/codementor-logo-2.png' width='100px'></span><p><a href='https://www.codementor.io/learn-html' target='_blank'>CodeMentor - Front End Development</a>: Learning HTML is the starting point for most website creators. Sure, tutorials can get you up and running, but advanced concepts are much easier to grasp with the help of a good teacher. Codementor has top HTML tutors from all over the world to help you learn HTML online.</p>"
      
    if soln["X"] == "codechef":
      soln["X"] = "<span class='logoBorder'><img src='http://www.logogalleria.com/wp-content/uploads/2009/09/codechef.jpg' width='100px'></span><p><a href='http://www.codechef.com/' target='_blank'>CodeChef - Competitive Coding Challenges</a>: Prepare your self for various kinds of programming challenges by solving practice problems of varying difficulty. Compete against other techies in our monthly programming contests, gain recognition and win cool stuff. Coding contests begin on the first of every month.</p>"
      
    if soln["X"] == "codecademyhtml":
      soln["X"] = "<span class='logoBorder'><img src='http://cdn.appstorm.net/web.appstorm.net/files/2011/10/codecademy_logo.png' width='100px'></span><p><a href='http://www.codecademy.com/tracks/web' target='_blank'>Codecademy - HTML Training Track</a>: Learn the building blocks of web development with HTML and CSS, and create your own website by the end of the course.</p>"
      
    if soln["X"] == "codecademyjquery":
      soln["X"] = "<span class='logoBorder'><img src='http://cdn.appstorm.net/web.appstorm.net/files/2011/10/codecademy_logo.png' width='100px'></span><p><a href='http://www.codecademy.com/tracks/jquery' target='_blank'>Codecademy - jQuery Training Track</a>: jQuery uses JavaScript to easily build interactive websites. Learn animation, events and DOM manipulation.</p>"

    if soln["X"] == "codecademyror":
      soln["X"] = "<span class='logoBorder'><img src='http://cdn.appstorm.net/web.appstorm.net/files/2011/10/codecademy_logo.png' width='100px'></span><p><a href='http://www.codecademy.com/tracks/ruby' target='_blank'>Codecademy - Ruby Programming Track</a>: Ruby is a powerful yet beginner-friendly language used for professional web apps all over the world. Learn the syntax and complete exercises.</p>"
      
    if soln["X"] == "codecademypython":
      soln["X"] = "<span class='logoBorder'><img src='http://cdn.appstorm.net/web.appstorm.net/files/2011/10/codecademy_logo.png' width='100px'></span><p><a href='http://www.codecademy.com/tracks/python' target='_blank'>Codecademy - Python Programming Track</a>: Learn the fundamentals of programming to build web apps and manipulate data.</p>"
      
    if soln["X"] == "codecademyphp":
      soln["X"] = "<span class='logoBorder'><img src='http://cdn.appstorm.net/web.appstorm.net/files/2011/10/codecademy_logo.png' width='100px'></span><p><a href='http://www.codecademy.com/tracks/php' target='_blank'>Codecademy - PHP Programming Track</a>: Go through PHP programming exercises and solve programming problems.</p>"
      
    if soln["X"] == "codeschoolror":
      soln["X"] = "<span class='logoBorder'><img src='https://d1tijy5l7mg5kk.cloudfront.net/assets/press_kit/logo-full-text-8f831675b0a894d991d720c532651ec6.png' width='100px'></span><p><a href='https://www.codeschool.com/paths/ruby' target='_blank'>CodeSchool - Ruby on Rails Development</a>: Master your Ruby skills and increase your Rails street cred by learning to build dynamic, sustainable applications for the web.</p>"
      
    if soln["X"] == "codeschoolfrontend":
      soln["X"] = "<span class='logoBorder'><img src='https://d1tijy5l7mg5kk.cloudfront.net/assets/press_kit/logo-full-text-8f831675b0a894d991d720c532651ec6.png' width='100px'></span><p><a href='https://www.codeschool.com/paths/html-css' target='_blank'>CodeSchool - Front End Development</a>: Learn the fundamentals of design, front-end development, and crafting user experiences that are easy on the eyes.</p>"
      
    if soln["X"] == "codeschoolios":
      soln["X"] = "<span class='logoBorder'><img src='https://d1tijy5l7mg5kk.cloudfront.net/assets/press_kit/logo-full-text-8f831675b0a894d991d720c532651ec6.png' width='100px'></span><p><a href='https://www.codeschool.com/paths/ios' target='_blank'>CodeSchool - iOS Mobile App Development</a>: Try your hand at building iOS applications for iPhone and iPad mobile devices. Learn the basics of iOS development and bring your app ideas to life.</p>"
      
    if soln["X"] == "rubymonk":
      soln["X"] = "<span class='logoBorder'><img src='https://dy0ao1dkujg1a.cloudfront.net/assets/layouts/rubymonk-menu-logo-e3705b4511769c85dcb07be28c871daa.png' width='100px'></span><p><a href='https://rubymonk.com/' target='_blank'>Ruby Monk - Ruby Programming Training</a>: Free, interactive tutorials to help you discover Ruby idioms, in your browser.</p>"
      
    if soln["X"] == "treehousefrontend":
      soln["X"] = "<span class='logoBorder'><img src='http://yourlocalamerica.com/wp-content/uploads/2013/11/Treehouse-Logo-Mark.png' width='100px'></span><p><a href='http://teamtreehouse.com/library/topic:html' target='_blank'>Team Treehouse - Front End Development</a>: HyperText Markup Language (HTML) forms the structural layer of web pages. No matter what kind of website or application you want to build, this is a language you need to understand.</p>"
      
    if soln["X"] == "treehouseror":
      soln["X"] = "<span class='logoBorder'><img src='http://yourlocalamerica.com/wp-content/uploads/2013/11/Treehouse-Logo-Mark.png' width='100px'></span><p><a href='http://teamtreehouse.com/library/topic:ruby' target='_blank'>Team Treehouse - Ruby on Rails Development</a>: Ruby is a dynamic, open source programming language with a focus on simplicity and productivity. It has an elegant syntax that is natural to read and easy to write.</p>"
      
    if soln["X"] == "treehousephp":
      soln["X"] = "<span class='logoBorder'><img src='http://yourlocalamerica.com/wp-content/uploads/2013/11/Treehouse-Logo-Mark.png' width='100px'></span><p><a href='http://teamtreehouse.com/library/topic:php' target='_blank'>Team Treehouse - PHP Web Development</a>: Learn how to build a full eCommerce shop with step by step videos and exercises. PHP is a widely-used general-purpose scripting language that is especially suited for Web Development and can be embedded into HTML.</p>"
      
    if soln["X"] == "treehouseandroid":
      soln["X"] = "<span class='logoBorder'><img src='http://yourlocalamerica.com/wp-content/uploads/2013/11/Treehouse-Logo-Mark.png' width='100px'></span><p><a href='http://teamtreehouse.com/library/topic:android' target='_blank'>Team Treehouse - Android Mobile App Development</a>: Android is the mobile operating system used on more devices around the world than any other platform. Learn how to create Android apps using Java and the powerful development tools available from Google.</p>"
      
    if soln["X"] == "treehouseios":
      soln["X"] = "<span class='logoBorder'><img src='http://yourlocalamerica.com/wp-content/uploads/2013/11/Treehouse-Logo-Mark.png' width='100px'></span><p><a href='http://teamtreehouse.com/library/topic:ios' target='_blank'>Team Treehouse - iOS Mobile App Development</a>: iOS is the powerful operating system that powers iPhones and iPads. Learn the language, tools and frameworks to build interactive apps on the iOS platform.</p>"
      
    if soln["X"] == "udacitypython1":
      soln["X"] = "<span class='logoBorder'><img src='http://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Udacity_Logo.svg/396px-Udacity_Logo.svg.png' width='100px'></span><p><a href='https://www.udacity.com/course/cs101' target='_blank'>Udacity - Intro to Python Web Development</a>: In this introductory course, you will learn and practice key computer science concepts by building your own versions of popular web applications. You will learn Python, a powerful, easy-to-learn, and widely used programming language, and you will explore fundamental computer science concepts, as you build your own search engine and social network.</p>"
      
    if soln["X"] == "udacitypython2":
      soln["X"] = "<span class='logoBorder'><img src='http://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Udacity_Logo.svg/396px-Udacity_Logo.svg.png' width='100px'></span><p><a href='https://www.udacity.com/course/cs253' target='_blank'>Udacity - Intermediate Python Web Development</a>: In this intermediate course, Steve Huffman will teach you everything he wished he knew when he started building Reddit and, more recently, Hipmunk, as a lead engineer. Starting from the basics of how the web works, this course will walk you through core web development concepts such as how internet and browsers fit together, form validations, databases, APIs, integrating with other websites, scaling issues, and more; all of which form part of the knowledge it takes to build a web application of your own.</p>"
      
    if soln["X"] == "udacityfrontend":
      soln["X"] = "<span class='logoBorder'><img src='http://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Udacity_Logo.svg/396px-Udacity_Logo.svg.png' width='100px'></span><p><a href='https://www.udacity.com/course/ud248' target='_blank'>Udacity - Front End Development</a>: Ten minutes into this class you will make your own completely personalized version of the insanely addictive game 2048. Even if you've never coded before. Pretty cool, no? You will do this by making small (but important) modifications to the source code for the original 2048 game. If this sounds intimidating, don't worry. We'll teach you the basics of HTML and CSS and how they interact with Javascript (don't worry if that sentence doesn't mean anything to you yet. It will soon).</p>"
      
    if soln["X"] == "javaposse":
      soln["X"] = "<span class='logoBorder'><img src='http://www.mindviewinc.com/Conferences/JavaPosseRoundup/JavaPosseLogoSmall.png.png' width='100px'></span><p><a href='http://javaposse.com/' target='_blank'>Java Posse - Java and Android Podcasts</a>: News, Interviews, Opinions, and General Mayhem focused on the java community.</p>"
      
    if soln["X"] == "stackexchange":
      soln["X"] = "<span class='logoBorder'><img src='http://cdn.sstatic.net/stackexchange/img/logos/se/se-logo.png' width='100px'></span><p><a href='http://blog.stackoverflow.com/category/podcasts/' target='_blank'>StackExchange - Programming Podcasts</a>: General programming discussions.</p>"
      
    if soln["X"] == "hansel":
      soln["X"] = "<span class='logoBorder'><img src='http://www.hanselminutes.com/images/logo.png' width='100px'></span><p><a href='http://www.hanselminutes.com/' target='_blank'>Hansel Minutes - Programming Podcasts</a>: I'm a teacher. I speak all over to whoever will listen. I have written code that you've used. I've been blogging for over a decade and podcasting for about half that. I speak, code, write, empower, promote, braid, learn and listen - usually not in that order.</p>"
      
    if soln["X"] == "twittv":
      soln["X"] = "<span class='logoBorder'><img src='http://twit.tv/files/imagecache/coverart-feed/coverart/sn300.jpg' width='100px'></span><p><a href='http://twit.tv/sn' target='_blank'>Team Twit.tv - Programming Podcasts</a>: Steve Gibson, the man who coined the term spyware and created the first anti-spyware program, creator of Spinrite and ShieldsUP, discusses the hot topics in security today with Leo Laporte. Records live every Tuesday at 1:00pm PT/4:00pm ET.</p>"
      
    if soln["X"] == "thechangelog":
      soln["X"] = "<span class='logoBorder'><img src='http://static.squarespace.com/static/4fb1327fe4b037aee8691be3/t/5192b877e4b05340711c3bf4/1368569977503/cover-1.jpg' width='100px'></span><p><a href='http://thechangelog.com/podcast/' target='_blank'>The Change Log - Open Source Podcasts</a>: Discussions focused on the open source code community.</p>"
      
    if soln["X"] == "phptownhall":
      soln["X"] = "<span class='logoBorder'><img src='https://www.drupal.org/files/project-images/php.png' width='100px'></span><p><a href='http://phptownhall.com/' target='_blank'>PHP Town Hall - PHP Programming Podcasts</a>: Phil, Ben and a super-star guest answer questions and talk about current events in the PHP world.</p>"
      
    if soln["X"] == "rubyrogues":
      soln["X"] = "<span class='logoBorder'><img src='https://www.drupal.org/files/project-images/php.png' width='100px'></span><p><a href='http://rubyrogues.com/' target='_blank'>Ruby Rogues - Ruby Programming Podcasts</a>: In depth coverage of the Ruby Programming language community.</p>"
      
    if soln["X"] == "udemyrorbiz":
      soln["X"] = "<span class='logoBorder'><img src='https://udemyimages-a.akamaihd.net/course/480x270/119262_c783_2.jpg' width='100px'></span><p><a href='https://www.udemy.com/comprehensive-ruby-on-rails' target='_blank'>Edutechional - Ruby on Rails Business Application Development</a>: This course that will walk you step by step through every skill you will need to become a full stack web developer, and I do it by showing you how to build an actual production application. Starting completely from scratch I explain how to setup your environment, create the application, build in advanced features and finally deploy to the web!</p>"
      
    if soln["X"] == "udemyfrontend1":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/web-development-tutorials' target='_blank'>Stone River eLearning - Front End Development</a>: The design and structure of this course follows elite college curriculum. You will begin by learning the basics of each programming language and technology web developers use, and you will be creating real life projects with every new skill you learn so you're getting the entire finished puzzle instead of just pieces that you have to put together yourself.</p>"
      
    if soln["X"] == "udemyphp1":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/become-a-certified-web-developer' target='_blank'>LearnToProgram.TV - PHP Web Development</a>: Learn What It Takes to Code Dynamic, Professional Websites and Web Apps From The Comfort of Your Own Home. Our course starts teaching basic coding principles and develops your coding skills in a variety of languages from beginner through to advanced. Here it is, once and for all, a complete guide that will take you from novice to web developer.</p>"
      
    if soln["X"] == "udemyandroid1":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/learn-by-doing-android-for-beginners' target='_blank'>Ragunath Jawahar - Android Mobile App Development</a>:  From the Developer of over 100 Android Applications and 6 Open Source Android Libraries.</p>"
      
    if soln["X"] == "udemyios1":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/iosdevelopment' target='_blank'>The App Dojo - iOS Mobile App Development</a>: I'll teach you how to make iPhone apps with this complete iOS development tutorial.  You'll learn how to create apps using the same tools and techniques used to make the top apps in The App Store.</p>"
      
    if soln["X"] == "udemyios2":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/the-complete-ios-7-course-learn-by-building-14-apps' target='_blank'>John Nichols - iOS Mobile App Development</a>: Our iOS Bootcamp teaches the tools needed to develop iPhone and iPad applications for iOS7. Along our journey, we will learn the syntax of Objective-C, the language used to develop for iOS, as well as important design patterns and best practices. By the end of the course, you should be able to understand and recreate many of the features seen on popular iOS applications and extend that knowledge to making apps of your own.</p>"
      
    if soln["X"] == "udemyios4":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/swift-learn-apples-new-programming-language-by-examples' target='_blank'>Rick Walter - iOS Mobile App Development</a>: Swift is a multi-paradigm programming language developed by Apple for use with iOS and OS X. Designed to replace Objective C, work began on Swift in 2010 and the first mobile app was debuted in June 2014 at the Worldwide Developers Conference. Despite its goal of replacing Objective C, Swift is capable of working alongside the more dated Objective C language while using the Cocoa and Cocoa Touch frameworks.</p>"
      
    if soln["X"] == "udemyios5":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/projects-in-ios' target='_blank'>Eduonix Learning Solutions - iOS Mobile App Development</a>: This is a course for all programmers who will like to build on their iOS knowledge and create actual apps for the App store. This course assumes basic iOS programming knowledge but is still ideal for beginners as we are covering the APIs in detail before using them to build the projects.</p>"
      
    if soln["X"] == "udemyrorsoc":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/create-and-deploy-a-web-app-in-3-hours' target='_blank'>Tiago Martins - Ruby on Rails Social App Development</a>: This course will teach you how to combine Ruby on Rails and Facebook Connect to create a sleek final product that harnesses the power of Facebook to attract new users.</p>"
      
    if soln["X"] == "udemyios6":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/learn-ios-programming-the-basics' target='_blank'>Eduonix Learning Solutions - Intro to iOS Mobile App Development</a>: This iOS course is aimed to provide a through and clear understanding of the iOS programming. We start with basic Hello world for iOS and cover the most important topics which will provide you a firm base to build your iOS Apps. This lecture uses the latest IOS SDK and uses an example based approach to teaching. We have kept the learning curve simple and focus is on conceptual learning rather than just teaching how to use a particular API. After completing the course you will understand the principle behind the API patterns and why a particular control behaves the way it does.</p>"
      
    if soln["X"] == "udemyfrontend2":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/webdevelopment101_html' target='_blank'>Brian Gorman - Front End Development</a>: This course is an overview of the HTML web programming standard. The course is intended for those who have never done anything with HTML or web pages and would like to build this basic knowledge for starting a career as a web developer or for learning how to program HTML for web pages. By no means will you be a world class UI developer at the end of this course, but you will have the basic understanding of building pages with HTML and HTML5, and at the end of the course you'll gain knowledge about where to go next to further your front-end web development skills.</p>"
      
    if soln["X"] == "udemygames1":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/learn-c-game-development' target='_blank'>Luka Horvat - C++ Game Development</a>: Learn C++ game development is a course I made for everyone who knows how to program, but doesn't know where to start with game development. The course teaches you how to use the SFML library for C++, to start working with graphics, events and sound to create a 2D game. Everything is done step by step with the help of videos, so it's easy to follow along and learn. At the end of the course you will know what you need for game programming and will be able to start making your own games.</p>"
      
    if soln["X"] == "udemygames2":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/responsive-html5-theme-development' target='_blank'>Lamin Sanneh - HTML5 Game Development</a>: In this course, using direct approaches, I will teach how to build such websites. This is a very focussed course and I intentionally removed unnecessary material which I believe only distracts students from what they need to know. I know this from experience, and hence the reason the course is not that long. So lean back , relax and come along this exciting journey which is responsive web design.</p>"
      
    if soln["X"] == "udemyphp2":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/php-programming-basics' target='_blank'>Stone River eLearning - PHP Web Application Development</a>:  In this course we cover the very basics of PHP programming, then move on to more complex topics while still making sure the course is easy to understand for those who have never programmed before.</p>"
      
    if soln["X"] == "udemyfrontend3":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/learn-to-build-beautiful-html5-and-css3-websites-in-1-month' target='_blank'>Ryan Bonhardt - Front End Development</a>: You will learn how to build your first website within 1 week with all the basics of HTML and CSS. Then we expand and add upon that knowledge with more advanced HTML and CSS as we build our second site together. To top it off we repeat this process with smaller lessons and within one month you will have a complete knowledge and ability to build startup quality websites FAST.</p>"
      
    if soln["X"] == "udemyfrontend4":
      soln["X"] = "<span class='logoBorder'><img src='https://www-udemy-com.global.ssl.fastly.net/static/images/v4/logo.jpg' width='100px'></span><p><a href='https://www.udemy.com/android-programming-for-beginners' target='_blank'>Mark Lassoff - Android Mobile App Development</a>: While this is a course for beginners, to be successful you need to know the basics of Java.  The course will review the more complex Java used in the Android ecosystem, but you should understand Java Basics-- Variables, Loops, Functions, Conditionals should be enough.</p>"
      
    if soln["X"] == "khangames1":
      soln["X"] = "<span class='logoBorder'><img src='https://www.intellectualrevolution.tv/wp-content/uploads/Khan-Academy-Logo.jpg' width='100px'></span><p><a href='https://www.khanacademy.org/computing/cs/programming' target='_blank'>Khan Academy - Intro to Game Development</a>: In these tutorials, you'll learn how to use the JavaScript language and the ProcessingJS library to create fun drawings and animations. If you've never programmed before, start here to learn how!</p>"
      
    if soln["X"] == "khangames2":
      soln["X"] = "<span class='logoBorder'><img src='https://www.intellectualrevolution.tv/wp-content/uploads/Khan-Academy-Logo.jpg' width='100px'></span><p><a href='https://www.khanacademy.org/computing/cs/programming-games-visualizations' target='_blank'>Khan Academy - Game Development</a>: Now that you know how to program in JavaScript and make basic drawings and animations, how could you use that knowledge to make games and visualizations?</p>"
      
    if soln["X"] == "khangames3":
      soln["X"] = "<span class='logoBorder'><img src='https://www.intellectualrevolution.tv/wp-content/uploads/Khan-Academy-Logo.jpg' width='100px'></span><p><a href='https://www.khanacademy.org/computing/cs/programming-natural-simulations' target='_blank'>Khan Academy - Intermediate Game Development</a>: Learn how to use JavaScript, ProcessingJS, and mathematical concepts to simulate nature in your programs. These tutorials are a derivative of 'The Nature of Code' book by Daniel Shiffman (natureofcode.com)</p>"
      
    if soln["X"] == "codeplayer":
      soln["X"] = "<span class='logoBorder'><img src='http://auroraiannino.be/wp-content/uploads/2014/01/thecodeplayer0.jpg' width='100px'></span><p><a href='http://thecodeplayer.com/' target='_blank'>CodePlayer - Front End Development</a>: Video style walkthroughs showing cool stuff being created from scratch.</p>"
      
    if soln["X"] == "hardwaypython1":
      soln["X"] = "<span class='logoBorder'><img src='http://auroraiannino.be/wp-content/uploads/2014/01/thecodeplayer0.jpg' width='100px'></span><p><a href='http://learnpythonthehardway.org' target='_blank'>Learn Python the Hard Way - Python Programming Manual</a>: Read by 1.5 million people a year to learn the basics of programming, Learn Python The Hard Way is the most successful beginner programming book on the market.</p>"
      
    if soln["X"] == "hardwaypython1":
      soln["X"] = "<span class='logoBorder'><img src='http://auroraiannino.be/wp-content/uploads/2014/01/thecodeplayer0.jpg' width='100px'></span><p><a href='http://learnpythonthehardway.org' target='_blank'>Learn Python the Hard Way - Python Programming Video Series</a>: Read by 1.5 million people a year to learn the basics of programming, Learn Python The Hard Way is the most successful beginner programming book on the market. For $29.95 you get a complete beginner programming course with 1.7GB of Video, a PDF and ePub, and no ads on the web site."
      
    if soln["X"] == "railscasts":
      soln["X"] = "<span class='logoBorder'><img src='http://geekhmer.github.io/images/logo_rails_casts.png' width='100px'></span><p><a href='http://railscasts.com/' target='_blank'>Railscasts - Ruby on Rails Web Development</a>: The topics target the intermediate Rails developer, but beginners and experts will get something out of it as well. A Pro option is also available containing more screencasts each week.</p>"

    
    ## *************************** END *************************** ##
    classSuggested.append(soln["X"])
  
  email = settings.support_email
  return render(request, 'confirm.html', {'uuid':uuid, "email": email, 'projectdesired':projectdesired, 'educationlevel':educationlevel, 'programmingexperience':programmingexperience, 'learningpriority':learningpriority, 'employmentstatus':employmentstatus, 'featuredriven':featuredriven, 'mentordriven':mentordriven, 'audience':audience, 'competitive':competitive, 'internetstatus':internetstatus, 'motivation':motivation, 'machine':machine, 'budget':budget, 'hoursfree':hoursfree, 'timeframe':timeframe, 'classSuggested':classSuggested, 'classURL':classURL})

def privacy(request):
  return render(request, 'privacy.html')


