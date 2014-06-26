from pyswip import Functor, Variable, Query, call

def question_finder(question, ans):
  assertz = Functor("assertz", 1)
  if question == "What is the highest level of education you've completed?":
    education = Functor("education", 1)
    if ans == "High School":
      print "before call"
      call(assertz(education("highschool")))
      X = Variable()
      print "before query"
      q = Query(education(X))
      print "before solution"
      while q.nextSolution():
        print "The survey's education is ", X.value
      print "close"
      q.closeQuery()
