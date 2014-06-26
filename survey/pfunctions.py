from pyswip import Functor, Variable, Query, call

def question_finder(question, ans):
  assertz = Functor("assertz", 1)
  if question == "What is the highest level of education you've completed?":
    education = Functor("education", 1)
    if ans == "High School":
      call(assertz(education("highschool")))
      X = Variable()
      q = Query(education(X))
      while q.nextSolution():
        print "The survey's education is ", X.value
      q.closeQuery()
