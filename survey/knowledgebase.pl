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

% Determines if the student has a college level education
graduate(X) :-  education(X), X=associates;
                education(X), X=bachelors;
                education(X), X=masters;
                education(X), X=phd.

% Determines if the student is interested in mobile development
mobiledevelopment(X) :- projectdesired(X), X=iphoneapp; projectdesired(X), X=androidapp.

% Determines if the student is interested in web development
webdevelopment(X) :- projectdesired(X), X=webapp.

%classSuggestion(codechef) :- projectdesired(frontend), competitive(iscompetitive).

classSuggestion(thinkful) :- projectdesired(frontend), mentor(mentordriven), budget(Y), Y >= 1500, hoursfree(X), X >= 10, highspeedinternet(highspeed), timeframe(quarter).

classSuggestion(secondclass) :- projectdesired(frontend), mentor(mentordriven), budget(Y), Y >= 1500, hoursfree(X), X >= 10, highspeedinternet(highspeed), timeframe(quarter).

classSuggestion(pleasedontbreak) :- projectdesired(frontend), mentor(mentordriven), budget(Y), Y >= 1500, hoursfree(X), X >= 10, highspeedinternet(highspeed), timeframe(quarter).
