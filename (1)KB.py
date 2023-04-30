# imports
from pyswip import Prolog

# definition of User Variables
PATH_KB = './KB/kb.pl'

# definition of the methods
def create_KB(path):
    '''
    It creates the Knowledge Base saving it to the given path.
    '''

    # opening the file 
    file_prolog = open(path, "w")

    # defining the standard operation to write on file_prolog
    write_clauses = lambda clauses: write_clauses_on_file(clauses, file_prolog)

    # starting the creation of the Knowledge Base
    write_clauses([
        'footballer(matteo)',
        'runner(nicola)',
        'athlete(X) :- footballer(X)',
        'athlete(X) :- runner(X)',
        'good_life(X) :- athlete(X), non_smoker(X)',
        'non_smoker(matteo)'
    ])

    # closing the file
    file_prolog.close()


def write_clauses_on_file(clauses, file):
    '''
    It writes the list of clauses on the given file.
    '''

    # appending all the clauses, adding '.' at the end.
    file.writelines('.\n'.join(clauses) + '.\n')


# start of the script
create_KB(PATH_KB)
pl = Prolog()

pl.consult(PATH_KB)

boolean_answer = lambda my_query: bool(list(pl.query(my_query)))
list_answer = lambda my_query: list(pl.query(my_query))

print('E\' nicola un atleta?')
print(boolean_answer('athlete(nicola)'))

print('E\' nicola un footballer?')
print(boolean_answer('footballer(nicola)'))

print('E\' nicola un runnner?')
print(boolean_answer('runner(nicola)'))

print('Ha nicola una vita sana?')
print(boolean_answer('good_life(nicola)'))

print('E\' matteo un atleta?')
print(boolean_answer('athlete(matteo)'))

print('E\' matteo un footballer?')
print(boolean_answer('footballer(matteo)'))

print('E\' matteo un runnner?')
print(boolean_answer('runner(matteo)'))

print('Ha matteo una vita sana?')
print(boolean_answer('good_life(matteo)'))


