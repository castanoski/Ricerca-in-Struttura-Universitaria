footballer(matteo).
runner(nicola).
athlete(X) :- footballer(X).
athlete(X) :- runner(X).
good_life(X) :- athlete(X), non_smoker(X).
non_smoker(matteo).
