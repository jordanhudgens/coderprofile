%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                     knowledgebase.pl                     %
%                                                          %
% Prolog file containing the knowledge to be utilized      %
% by the application.                                      %
%                                                          %
% Consulted by:                                            %
%               pfunctions.py                              %
%               views.py                                    %
%                                                          %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
:- abolish(classSuggestion/1).

:- use_module(library('clp/bounds')).
:- dynamic classSuggestion/1.

classSuggestion(thinkfulfrontend) :- projectdesired(frontend), mentor(mentordriven), budget(Y), Y >= 1500, hoursfree(X), X >= 10, highspeedinternet(highspeed), timeframe(Z), Z >= 90.

classSuggestion(thinkfulpython) :- projectdesired(webapp), mentor(mentordriven), budget(Y), Y >= 1500, hoursfree(X), X > 10, highspeedinternet(highspeed), timeframe(Z), Z >= 90.

classSuggestion(thinkfulruby) :- projectdesired(webapp), mentor(mentordriven), budget(Y), Y >= 1500, hoursfree(X), X > 10, highspeedinternet(highspeed), timeframe(Z), Z >= 90.

classSuggestion(thinkfulios) :- projectdesired(iphoneapp), mentor(mentordriven), budget(Y), Y >= 1500, hoursfree(X), X > 10, highspeedinternet(highspeed), machine(mac), timeframe(Z), Z >= 90.

classSuggestion(railscasts) :- projectdesired(webapp), priority(practical), featuredriven(true), highspeedinternet(highspeed).

classSuggestion(rubyrogues) :- projectdesired(webapp), employment(fulltime).

classSuggestion(blocror) :- projectdesired(webapp), mentor(mentordriven), budget(X), X >= 1500, hoursfree(Y), Y >= 40, highspeedinternet(highspeed), timeframe(Z), Z >= 90.

classSuggestion(blocfrontend) :- projectdesired(frontend), mentor(mentordriven), budget(X), X >= 1500, hoursfree(Y), Y >= 40, highspeedinternet(highspeed), timeframe(Z), Z >= 90.

classSuggestion(blocandroid) :- projectdesired(androidapp), mentor(mentordriven), budget(X), X >= 1500, hoursfree(Y), Y >= 40, highspeedinternet(highspeed), timeframe(Z), Z >= 90.

classSuggestion(blocois) :- projectdesired(iphoneapp), mentor(mentordriven), budget(X), X >= 1500, hoursfree(Y), Y >= 40, highspeedinternet(highspeed), timeframe(Z), Z >= 90, machine(mac).

classSuggestion(codementorpython) :- projectdesired(webapp), mentor(mentordriven), budget(X), X >= 500, hoursfree(Y), Y >= 5, highspeedinternet(highspeed), timeframe(Z), Z >= 30.

classSuggestion(codementorror) :- projectdesired(webapp), mentor(mentordriven), budget(X), X >= 500, hoursfree(Y), Y >= 5, highspeedinternet(highspeed), timeframe(Z), Z >= 30.

classSuggestion(codementorios) :- projectdesired(iphoneapp), mentor(mentordriven), budget(X), X >= 500, hoursfree(Y), Y >= 5, highspeedinternet(highspeed), machine(mac), timeframe(Z), Z >= 30.

classSuggestion(codementorandroid) :- projectdesired(androidapp), mentor(mentordriven), budget(X), X >= 500, hoursfree(Y), Y >= 5, highspeedinternet(highspeed), timeframe(Z), Z >= 30.

classSuggestion(codementorfrontend) :- projectdesired(frontend), mentor(mentordriven), budget(X), X >= 500, hoursfree(Y), Y >= 5, highspeedinternet(highspeed), timeframe(Z), Z >= 30.

classSuggestion(codechef) :- projectdesired(generalprogramming), experience(intermediate), priority(theory), targetaudience(programmingtheory), competitive(iscompetitive).

classSuggestion(codechef) :- projectdesired(generalprogramming), experience(extensive), priority(theory), targetaudience(programmingtheory), competitive(iscompetitive).

classSuggestion(codecademyhtml) :- priority(theory), targetaudience(business).

classSuggestion(codecademyjquery) :- priority(theory), targetaudience(business).

classSuggestion(codecademyror) :- priority(theory), targetaudience(programmingtheory).

classSuggestion(codecademypython) :- priority(theory), targetaudience(programmingtheory).

classSuggestion(codecademyphp) :- priority(theory), targetaudience(ecommerce).

classSuggestion(codeschoolror) :- projectdesired(webapp), budget(X), X > 0, featuredriven(true), targetaudience(socialapps), highspeedinternet(highspeed).

classSuggestion(codeschoolfrontend) :- projectdesired(frontend), budget(X), X > 0, featuredriven(true), targetaudience(business), highspeedinternet(highspeed).

classSuggestion(codeschoolios) :- projectdesired(iphoneapp), budget(X), X > 0, featuredriven(true), highspeedinternet(highspeed).

classSuggestion(rubymonk) :- projectdesired(generalprogramming).

classSuggestion(treehousefrontend) :- projectdesired(frontend), budget(X), X > 0, priority(practical), highspeedinternet(highspeed), motivation(project).

classSuggestion(treehouseror) :- projectdesired(webapp), budget(X), X > 0, priority(practical), highspeedinternet(highspeed), motivation(project).

classSuggestion(treehousephp) :- projectdesired(webapp), budget(X), X > 0, priority(practical), highspeedinternet(highspeed), motivation(project), targetaudience(ecommerce).

classSuggestion(treehouseandroid) :- projectdesired(androidapp), budget(X), X > 0, priority(practical), highspeedinternet(highspeed), motivation(project).

classSuggestion(treehouseios) :- projectdesired(iphoneapp), budget(X), X > 0, priority(practical), highspeedinternet(highspeed), motivation(project).

classSuggestion(udacitypython1) :- projectdesired(generalprogramming), budget(X), X > 0, experience(low), featuredriven(true), highspeedinternet(highspeed).

classSuggestion(udacitypython2) :- projectdesired(generalprogramming), budget(X), X > 0, experience(intermediate), featuredriven(true), highspeedinternet(highspeed).

classSuggestion(udacityfrontend) :- projectdesired(frontend), experience(low), featuredriven(true), highspeedinternet(highspeed).

classSuggestion(javaposse) :- projectdesired(androidapp), employment(fulltime).

classSuggestion(stackexchange) :- projectdesired(generalprogramming), employment(fulltime).

classSuggestion(hansel) :- projectdesired(webapp), employment(fulltime).

classSuggestion(twittv) :- projectdesired(webapp), employment(fulltime).

classSuggestion(thechangelog) :- projectdesired(generalprogramming), employment(fulltime).

classSuggestion(phptownhall) :- projectdesired(webapp), employment(fulltime).

classSuggestion(udemyrorbiz) :- projectdesired(webapp), budget(X), X > 0, priority(practical), featuredriven(true), targetaudience(business), highspeedinternet(highspeed).

classSuggestion(udemyfrontend1) :- projectdesired(frontend), budget(X), X > 299, priority(practical), featuredriven(true), highspeedinternet(highspeed).

classSuggestion(udemyphp1) :- projectdesired(webapp), budget(X), X > 0, priority(practical), featuredriven(true), highspeedinternet(highspeed).

classSuggestion(udemyandroid1) :- projectdesired(androidapp), priority(practical), featuredriven(true), highspeedinternet(highspeed).

classSuggestion(udemyios1) :- projectdesired(iphoneapp), priority(practical), featuredriven(true), highspeedinternet(highspeed), machine(mac).

classSuggestion(udemyios2) :- projectdesired(iphoneapp), budget(X), X > 499, priority(practical), featuredriven(true), highspeedinternet(highspeed), machine(mac).

% classSuggestion(udemyios3) :- projectdesired(iphoneapp), budget(X), X > 199, priority(practical), featuredriven(true), highspeedinternet(highspeed), machine(mac).

classSuggestion(udemyios4) :- projectdesired(iphoneapp), budget(X), X > 199, priority(practical), featuredriven(true), highspeedinternet(highspeed), machine(mac).

classSuggestion(udemyios5) :- projectdesired(iphoneapp), budget(X), X > 199, priority(practical), featuredriven(true), highspeedinternet(highspeed), machine(mac).

classSuggestion(udemyrorsoc) :- projectdesired(webapp), budget(X), X > 59, priority(practical), featuredriven(true), highspeedinternet(highspeed), targetaudience(socialapps).

classSuggestion(udemyios6) :- projectdesired(iphoneapp), priority(practical), featuredriven(true), highspeedinternet(highspeed), machine(mac).

classSuggestion(udemyfrontend2) :- projectdesired(frontend), priority(practical), featuredriven(true), highspeedinternet(highspeed).

classSuggestion(udemygames1) :- budget(X), X > 0, priority(practical), featuredriven(true), highspeedinternet(highspeed), targetaudience(games).

classSuggestion(udemygames2) :- targetaudience(games).

classSuggestion(udemyphp2) :- projectdesired(webapp), priority(practical), highspeedinternet(highspeed).

classSuggestion(udemyfrontend3) :- projectdesired(frontend), budget(X), X > 0, featuredriven(true), highspeedinternet(highspeed).

classSuggestion(udemyfrontend4) :- projectdesired(frontend), budget(X), X > 0, featuredriven(true), highspeedinternet(highspeed).

classSuggestion(khangames1) :- projectdesired(webapp), priority(practical), targetaudience(games), highspeedinternet(highspeed).

classSuggestion(khangames2) :- projectdesired(webapp), priority(practical), targetaudience(games), highspeedinternet(highspeed), experience(low).

classSuggestion(khangames3) :- projectdesired(webapp), priority(practical), targetaudience(games), highspeedinternet(highspeed), experience(intermediate).

classSuggestion(codeplayer) :- projectdesired(frontend).

classSuggestion(hardwaypython1) :- projectdesired(generalprogramming), priority(theory).

classSuggestion(hardwaypython2) :- projectdesired(generalprogramming), priority(theory), budget(X), X > 0.


% Issues to fix:
% How should the system know who is a visual/kinetic/audio learner?

