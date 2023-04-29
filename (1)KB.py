from pyswip import Prolog

#simple example to start

pl = Prolog()

pl.assertz('male(matteo)')
pl.assertz('female(adriana)')
pl.assertz('human(X) :- female(X)')
pl.assertz('human(Y) :- female(Y)')


print('Is Adriana a male?')
print(bool(list(pl.query('male(adriana)'))))


print('Is Adriana a human?')
print(bool(list(pl.query('human(adriana)'))))


print('Is Adriana a female?')
print(bool(list(pl.query('female(adriana)'))))