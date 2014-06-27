%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                     knowledgebase.pl                     %
%                                                          %
% Prolog file containing the knowledge to be utilized      %
% by the application.                                      %
%                                                          %
% Consulted by:                                            %
%               pfunctions.py                              %
%                                                          %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

:- use_module(library('clp/bounds')).

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

% Issues to fix:
% ability to allow 'extensive' experienced users to get classes for intermediate learners (codechef)

