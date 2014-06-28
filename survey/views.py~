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


