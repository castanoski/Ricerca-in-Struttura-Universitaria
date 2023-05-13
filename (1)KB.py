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
        ['neri_marco',['icon','reti']],
        ['azzurri_mattia',['reti','mri']],
        ['rossi_mario',['cc','mri']],
        ['bianchi_luigi',['icon','mri']]
    ]
    
    for student in students:
        write_clauses([f'is_student({student[0]})'])
        for corso in student[1]:
            write_clauses([f'follows_class({student[0]},{corso})'])

    #offices
    offices = [
        'o101',
        'o102',
        'o202',
        'o201']
    for office in offices:
        write_clauses([f'is_office_room({office})'])


    # adding facts for teachers
    teachers = [
        ['paolo_rossi',['reti'],[1]],
        ['fabrizio_frizzi',['mri'],[2]],
        ['mauro_cioce',['cc'],[0]],
        ['massimilino_cavalcanti',['icon'],[3]]
    ]

    for teacher in teachers:
        write_clauses([f'is_teacher({teacher[0]})'])
        for corso in teacher[1]:
            write_clauses([f'teaches_class({teacher[0]},{corso})'])
        for office in teacher[2]:
            write_clauses([f'office_owner({teacher[0]},{offices[office]})'])

    # adding facts for lesson_rooms
    
    lesson_rooms = [
        'a011',
        'a012',
        'a013',
        'a014']

    for lesson_room in lesson_rooms:
        write_clauses([f'is_lesson_room({lesson_room})'])


    #adding facts for bath_rooms
    bath_rooms = [
        'b101',
        'b102',
        'b103',
        'b104',]
    
    for bathroom in bath_rooms:
        write_clauses([f'is_bathroom({bathroom})'])

    #adding facts for study_rooms
    study_rooms = [
        's101',
        's102',
        's103',
        's104',]
    
    for study_room in study_rooms:
        write_clauses([f'is_study_room({study_room})'])


    #adding facts for classes
    classes = [
        ['icon',[
            [1,'monday',8,30,10,30],
            [1,'friday',10,30,13,30],
            [1,'wednesday',9,00,11,00]
            ]],
             ['mri',[
            [0,'tuesday',10,30,12,30],
            [0,'friday',11,30,13,30],
            [0,'wednesday',15,00,17,00]
            ]],
             ['cc',[
            [2,'monday',10,30,12,00],
            [2,'friday',10,45,12,45],
            [2,'thursday',8,00,11,00]
            ]],
             ['reti',[
            [3,'monday',11,30,14,30],
            [3,'friday',10,30,13,30],
            [3,'tuesday',13,00,16,00]
            ]],
        ]
    for cl in classes:
        for schedule in cl[1]:
            write_clauses([f'is_scheduled({cl[0]},{lesson_rooms[schedule[0]]},get_time({schedule[1]},{schedule[2]},{schedule[3]}),get_time({schedule[1]},{schedule[4]},{schedule[5]}))'])



    

    

           


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



