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

    # creating lists of individuals
    offices = [
        'office_room_101',
        'office_room_102',
        'office_room_202',
        'office_room_201'
    ]

    lesson_rooms = [
        'lesson_room_011',
        'lesson_room_012',
        'lesson_room_013',
        'lesson_room_014'
    ]

    bath_rooms = [
        'bath_room_101',
        'bath_room_102',
        'bath_room_103',
        'bath_room_104',
    ]

    study_rooms = [
        'study_room_101',
        'study_room_102',
        'study_room_103',
        'study_room_104',
    ]

    students = [                            # student = [nome_studente , lista_index_corsi]
        ['student_001',['icon','reti']],
        ['student_002',['reti','mri']],
        ['student_003',['cc','mri']],
        ['student_004',['icon','mri']]
    ]

    teachers = [                            # teacher = [nome_prof , lista_corsi, lista_index_uffici]
        ['teacher_001',['reti'],['office_room_102']],
        ['teacher_002',['mri'],['office_room_202']],
        ['teacher_003',['cc'],['office_room_101']],
        ['teacher_004',['icon'],['office_room_201']]
    ]

    classes = [                             # cl = [nome_corso, lista_schedulazioni] dove 
        ['icon',[                           # lista_schedulazioni = [index_aula, giorno, ora_inizio, minuti_inizio, ora_fine, minuti_fine]
            ['lesson_room_012','monday',8,30,10,30],
            ['lesson_room_012','friday',10,30,13,30],
            ['lesson_room_012','wednesday',9,00,11,00]
            ]
        ],
        ['mri',[
            ["lesson_room_011",'tuesday',10,30,12,30],
            ["lesson_room_011",'friday',11,30,13,30],
            ["lesson_room_011",'wednesday',15,00,17,00]
            ]
        ],
        ['cc',[
            ["lesson_room_013",'monday',10,30,12,00],
            ["lesson_room_013",'friday',10,45,12,45],
            ["lesson_room_013",'thursday',8,00,11,00]
            ]
        ],
        ['reti',[
            ["lesson_room_014",'monday',11,30,14,30],
            ["lesson_room_014",'friday',10,30,13,30],
            ["lesson_room_014",'tuesday',13,00,16,00]
            ]
        ],
    ]


    #adding definitions for places
    places=[
        ["bath_room_101",0,0,0,[
            "lesson_room_014",
             "office_room_101",
        ]],
        ["lesson_room_014",1,1,0,[
            "bath_room_101",
             "lesson_room_012",
        ]],
        ["office_room_101",2,1,0,[
            "bath_room_101",
             "lesson_room_013",
        ]]
    ]



    # opening the file 
    file_prolog = open(path, "w")

    # defining the standard operation to write on file_prolog
    write_clauses = lambda clauses: write_clauses_on_file(clauses, file_prolog)

    # creating a list of clauses to write
    clauses_list = []

    # adding facts for students 
    for student in students:
        clauses_list.append(f'is_student({student[0]})')
        for corso in student[1]:
            clauses_list.append(f'follows_class({student[0]},{corso})')

    # adding facts for offices
    for office in offices:
        clauses_list.append(f'is_office_room({office})')
    
    # adding facts for lesson_rooms
    for lesson_room in lesson_rooms:
        clauses_list.append(f'is_lesson_room({lesson_room})')

    #adding facts for bath_rooms
    for bathroom in bath_rooms:
        clauses_list.append(f'is_bath_room({bathroom})')

    #adding facts for study_rooms
    for study_room in study_rooms:
        clauses_list.append(f'is_study_room({study_room})')

    # adding facts for teachers 
    for teacher in teachers:
        clauses_list.append(f'is_teacher({teacher[0]})')
        for corso in teacher[1]:
            clauses_list.append(f'teaches_class({teacher[0]},{corso})')
        for office in teacher[2]:
            clauses_list.append(f'office_owner({teacher[0]},{office})')

    #adding facts for classes 
    for cl in classes:
        for schedule in cl[1]:
            clauses_list.append(f'is_scheduled({cl[0]},{schedule[0]},get_time({schedule[1]},{schedule[2]},{schedule[3]}),get_time({schedule[1]},{schedule[4]},{schedule[5]}))')

    #adding facts for places
    for place in places:
        clauses_list.append(f'position({place[0]},{place[1]},{place[2]})')
        clauses_list.append(f'floor({place[0]},{place[3]})')

    # sorting the list
    clauses_list.sort()

    # writing clauses on file
    write_clauses(clauses_list)

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



