from pyswip import Functor, Variable, Query, call, Prolog

def question_finder(question, ans):
  p = Prolog()
  p.consult('/home/jordanhudgens/code/coderprofile/survey/knowledgebase.pl')            # When placed on server, be sure to change this path!!!!
  
  # Question 1:  Type of Projects Desired to Learn
  if question == "What type of projects do you want to learn how to build?":
    if ans == "iPhone App":
      p.assertz('projectdesired(iphoneapp)')
    if ans == "Android App":
      p.assertz('projectdesired(androidapp)')
    if ans == "Web Application":
      p.assertz('projectdesired(webapp)') 
    if ans == "Front End Website Development":
      p.assertz('projectdesired(frontend)') 
    if ans == "No project":
      p.assertz('projectdesired(noproject)')
    if ans == "just programming":
      p.assertz('projectdesired(generalprogramming)')
  
  # Question 2:  Budget
  if question == "What is your budget?":
    if ans == "$0":
      p.assertz('budget(0)')
    if ans == "$50-$250":
      p.assertz('budget(250)')
    if ans == "$251-$500":
      p.assertz('budget(500)') 
    if ans == "$501-$1000":
      p.assertz('budget(1000)')
    if ans == "$1001-$1500":
      p.assertz('budget(1500)') 
    if ans == "$1501+":
      p.assertz('budget(1000000)') 
      
  # Question 3:  Level of Education
  if question == "What is the highest level of education you've completed?":
    if ans == "High School":
      p.assertz('education(highschool)')
    if ans == "Associates":
      p.assertz('education(associates)')
    if ans == "Bachelors":
      p.assertz('education(bachelors)') 
    if ans == "Masters":
      p.assertz('education(masters)')
    if ans == "PhD":
      p.assertz('education(phd)') 
      
  # Question 4:  Programming Experience
  if question == "What programming experience do you have?":
    if ans == "None":
      p.assertz('experience(none)')
    if ans == "Low":
      p.assertz('experience(low)')
    if ans == "Intermediate":
      p.assertz('experience(intermediate)') 
    if ans == "Extensive":
      p.assertz('experience(extensive)')
  
  # Question 5:  Learning Priority
  if question == "What's more of a priority for you to learn?":
    if ans == "Theory of coding":
      p.assertz('priority(theory)')
    if ans == "Real life projects":
      p.assertz('priority(practical)')
  
  # Question 6:  Employment Status
  if question == "Are you currently employed full time?":
    if ans == "Yes":
      p.assertz('employment(fulltime)')
    if ans == "No":
      p.assertz('employment(none)')
  
  # Question 7:  Weekly Time Dedication
  if question == "How many hours can you dedicate to learning each week?":
    if ans == "5":
      p.assertz('hoursfree(5)')
    if ans == "6-10":
      p.assertz('hoursfree(10)')
    if ans == "11-20":
      p.assertz('hoursfree(20)') 
    if ans == "21-30":
      p.assertz('hoursfree(30)')
    if ans == "31-40":
      p.assertz('hoursfree(40)') 
    if ans == "40+":
      p.assertz('hoursfree(168)') 
  
  # Question 8:  Feature Driven Developer
  if question == "Do you like to see the potential features you're going to build before learning how to implement them?":
    if ans == "Yes":
      p.assertz('featuredriven(true)')
    if ans == "I prefer to watch first":
      p.assertz('featuredriven(watchfirst)')
    if ans == "No":
      p.assertz('featuredriven(false)')
    if ans == "I want to start coding right away":
      p.assertz('featuredriven(wantstocode)')
      
  # Question 9:  Mentor Driven Developer
  if question == "Do you like working out problems with experts or do you prefer working out issues on your own?":
    if ans == "I would prefer to work with an expert":
      p.assertz('mentor(mentordriven)')
    if ans == "I like working issues out on my own":
      p.assertz('mentor(notmentordriven)')
  
  # Question 10: Audience
  if question == "What type of audience do you want to develop for? I want to build: ":
    if ans == "Business applications":
      p.assertz('targetaudience(business)')
    if ans == "Games":
      p.assertz('targetaudience(games)')
    if ans == "Social apps":
      p.assertz('targetaudience(socialapps)')
    if ans == "eCommerce":
      p.assertz('targetaudience(ecommerce)')
    if ans == "No audience - just programming theory":
      p.assertz('targetaudience(programmingtheory)')
  
  # Question 11: Competitive
  if question == "Does testing your coding skills against other developers appeal to you?":
    if ans == "Yes":
      p.assertz('competitive(iscompetitive)')
    if ans == "No":
      p.assertz('competitive(notcompetitive)')
  
  # Question 12: High Speed Internet Status
  if question == "Do you have access to high speed internet?":
    if ans == "Yes":
      p.assertz('highspeedinternet(highspeed)')
    if ans == "No":
      p.assertz('highspeedinternet(lowspeed)')
  
  # Question 13: Code Motivation
  if question == "Why do you want to learn to code?":
    if ans == "Build my own project":
      p.assertz('motivation(project)')
    if ans == "Learn a new hobby":
      p.assertz('motivation(hobby)')
    if ans == "Improve for my current job":
      p.assertz('motivation(job)')
  
  # Question 14: Machine Type
  if question == "What type of computer do you have to work on?":
    if ans == "Mac":
      p.assertz('machine(mac)')
    if ans == "Windows":
      p.assertz('machine(windows)')
    if ans == "Linux":
      p.assertz('machine(linux)')
  
  # Question 15: Timeframe for Learning 
  if question == "What is your timeframe?":
    if ans == "< 30 days":
      p.assertz('timeframe(month)')
    if ans == "31-90 days":
      p.assertz('timeframe(quarter)')
    if ans == "91+ days":
      p.assertz('timeframe(year)')
            
    ###################################################  
    ##################### QUERIES #####################
    ###################################################
    
    
#    for soln in p.query("projectdesired(X)."):
#      print "1) Type of projects desired:", soln["X"]
#      
#    for soln in p.query("education(X)."):
#      print "3) Level of education:", soln["X"]
#   
#    for soln in p.query("experience(X)."):
#      print "4) Programming experience:", soln["X"]
#      
#    for soln in p.query("priority(X)."):
#      print "5) Learning priority:", soln["X"]
#
#    for soln in p.query("employment(X)."):
#      print "6) Employment status:", soln["X"]
#      
#    for soln in p.query("featuredriven(X)."):
#      print "8) Feature Driven:", soln["X"]
#
#    for soln in p.query("mentor(X)."):
#      print "9) Mentor Driven:", soln["X"]
#      
#    for soln in p.query("targetaudience(X)."):
#      print "10) Target audience:", soln["X"]
#
#    for soln in p.query("competitive(X)."):
#     print "11) Competitive:", soln["X"]
#      
#    for soln in p.query("highspeedinternet(X)."):
#      print "12) Has high speed internet:", soln["X"]
#
#    for soln in p.query("motivation(X)."):
#      print "13) Motivation:", soln["X"]
#
#    for soln in p.query("machine(X)."):
#      print "14) Development environment:", soln["X"]

