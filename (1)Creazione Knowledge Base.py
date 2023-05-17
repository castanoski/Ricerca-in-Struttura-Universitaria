# imports
from Knowledge_Base import Knowledge_Base
import math

# definizione delle variabili utente
PATH_FACTS_KB = './KB/fatti.pl'
PATH_RULES_KB = './KB/regole.pl'
FILES_LIST = [PATH_FACTS_KB, PATH_RULES_KB]


# definizione dei metodi
def calculate_distance_from_KB(kb : Knowledge_Base, start : str, end : str, rounding=2) -> float:
    start_coord = kb.get_unique_query_result(f"position({start}, X, Y)")
    end_coord = kb.get_unique_query_result(f"position({end}, X, Y)")

    start_floor = kb.get_unique_query_result(f"floor({start}, Floor)")
    end_floor = kb.get_unique_query_result(f"floor({end}, Floor)")

    if(start_floor == end_floor):
        distance = math.sqrt(((start_coord["X"]-end_coord["X"])**2)+((start_coord["Y"]-end_coord["Y"])**2))
    else:
        # gestisci il caso in cui non si trovino sullo stesso piano
        pass

    return round(distance, rounding)


def create_KB(path):
    '''
    It creates the Knowledge Base saving it to the given path.
    '''

    # creazione degli individui
    office_rooms = [
        ['office_room_101',0,0,0,[      # [nome, x, y, floor, [lista_neighbors] ]
            'office_room_102',
        ]],
        ['office_room_102',1,0,0,[
            'office_room_101',
        ]],
        ['office_room_202',2,0,0,[

        ]],
        ['office_room_201',3,0,0,[

        ]]
    ]

    lesson_rooms = [
        ['lesson_room_011',0,1,0,[      # [nome, x, y, floor, [lista_neighbors] ]
            'lesson_room_012',
            'lesson_room_013',
            'lesson_room_014'
        ]],
        ['lesson_room_012',10,8,0,[     
            'lesson_room_011',
            'lesson_room_013',
            'lesson_room_014'
        ]],
        ['lesson_room_013',9,6,0,[     
            'lesson_room_011',
            'lesson_room_012',
            'lesson_room_014'
        ]],
        ['lesson_room_014',7,4,0,[     
            'lesson_room_011',
            'lesson_room_012',
            'lesson_room_013'
        ]],
    ]

    bath_rooms = [
        ['bath_room_101',1,1,0,[      # [nome, x, y, floor, [lista_neighbors] ]
            
        ]],
        ['bath_room_102',1,2,0,[     
            
        ]],
        ['bath_room_103',1,3,0,[     
            
        ]],
        ['bath_room_104',1,4,0,[     
            
        ]],
    ]

    study_rooms = [
        ['study_room_101',2,2,0,[      # [nome, x, y, floor, [lista_neighbors] ]
            
        ]],
        ['study_room_102',2,3,0,[     
            
        ]],
        ['study_room_103',2,4,0,[     
            
        ]],
        ['study_room_104',2,5,0,[     
            
        ]],
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

    places = office_rooms + study_rooms + bath_rooms + lesson_rooms

    # creazione di una lista di clausole da scrivere nel file
    clauses_list = []

    # aggiungiamo i fatti per gli studenti 
    for student in students:
        clauses_list.append(f'is_student({student[0]})')
        for corso in student[1]:
            clauses_list.append(f'follows_class({student[0]},{corso})')

    # aggiungiamo i fatti per gli uffici
    for office in office_rooms:
        clauses_list.append(f'is_office_room({office[0]})')
    
    # aggiungiamo i fatti per le aule di lezione
    for lesson_room in lesson_rooms:
        clauses_list.append(f'is_lesson_room({lesson_room[0]})')

    # aggiungiamo i fatti per i bagni
    for bathroom in bath_rooms:
        clauses_list.append(f'is_bath_room({bathroom[0]})')

    # aggiungiamo i fatti per le aule studio
    for study_room in study_rooms:
        clauses_list.append(f'is_study_room({study_room[0]})')

    # aggiungiamo i fatti per i docenti
    for teacher in teachers:
        clauses_list.append(f'is_teacher({teacher[0]})')
        for corso in teacher[1]:
            clauses_list.append(f'teaches_class({teacher[0]},{corso})')
        for office in teacher[2]:
            clauses_list.append(f'office_owner({teacher[0]},{office})')

    # aggiungiamo i fatti per i corsi
    for cl in classes:
        for schedule in cl[1]:
            clauses_list.append(f'is_scheduled({cl[0]},{schedule[0]},get_time({schedule[1]},{schedule[2]},{schedule[3]}),get_time({schedule[1]},{schedule[4]},{schedule[5]}))')

    # aggiungiamo i fatti per i luoghi
    for place in places:
        clauses_list.append(f'position({place[0]},{place[1]},{place[2]})')
        clauses_list.append(f'floor({place[0]},{place[3]})')

    # aggiungiamo le clausole per i pavimenti bagnati o per le stanze inutilizzabili
    clauses_list.append('there_is_a_problem_in(no_room)')
    clauses_list.append('has_wet_floor(no_place)')

    # ordiniamo la lista per evitare ridefinizioni
    clauses_list.sort()

    # scriviamo i fatti su file
    file_prolog = open(path, "w")
    write_clauses_on_file(clauses_list, file_prolog)
    file_prolog.close()

    # sfruttiamo i fatti appena scritti per interrogare la kb allo scopo di calcolarci le distanze tra punti vicini
    kb = Knowledge_Base(FILES_LIST)
    
    # creiamo una nuova lista
    clauses_list = []

    for place in places:
        for neighbor in place[4]:
            clauses_list.append(f'direct_arc({place[0]},{neighbor},{calculate_distance_from_KB(kb, place[0], neighbor)})')

    # aggiungiamo le nuove clausole a quelle precedentemente scritte 
    file_prolog = open(path, "a")
    write_clauses_on_file(clauses_list, file_prolog)
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



