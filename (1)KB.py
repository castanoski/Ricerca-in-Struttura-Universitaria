# imports
from pyswip import Prolog

# definizione delle variabili utente
PATH_FACTS_KB = './KB/fatti.pl'
PATH_RULES_KB = './KB/regole.pl'

# definition of methods to perform queries to the Knowledge Base
boolean_answer = lambda my_query: bool(list(pl.query(my_query)))
list_answer = lambda my_query: list(pl.query(my_query))

# definition of the methods
def create_KB(path):
    '''
    It creates the Knowledge Base saving it to the given path.
    '''

    # opening the file 
    file_prolog = open(path, "w")

    # defining the standard operation to write on file_prolog
    write_clauses = lambda clauses: write_clauses_on_file(clauses, file_prolog)

    # adding facts for students
    students = [
        'neri_marco',
        'azzurri_mattia',
        'rossi_mario',
        'bianchi_luigi'
    ]

    for student in students:
        write_clauses([f'student(st_{student})'])

    # adding facts for teachers
    teachers = [
        'alti_francesca',
        'bassi_nicola',
        'piccoli_ginevra',
        'grandi_massimiliano'
    ]

    for teacher in teachers:
        write_clauses([f'teacher(te_{teacher})'])

    # adding facts for classes
    days = [
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday'
    ]

    classes = [
        'ICon',
        'IUM',
        'MRI',
        'CC'
    ]

            #aggiungi casualmente due lezioni per classe in una aula X.


    # closing the file
    file_prolog.close()


def write_clauses_on_file(clauses, file):
    '''
    It writes the list of clauses on the given file.
    '''

    # appending all the clauses, adding '.' at the end.
    file.writelines('.\n'.join(clauses) + '.\n')


#       --------------------------------------------------------------------------------------------------------------------       #
#                                                   Inizio dello Script                                                            #
#       --------------------------------------------------------------------------------------------------------------------       # 

create_KB(PATH_FACTS_KB)
pl = Prolog()

pl.consult(PATH_RULES_KB)
pl.consult(PATH_FACTS_KB)



