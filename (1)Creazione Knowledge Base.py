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
    Creazione statica della Knowledge Base salvata nel path.
    '''

    # creazione degli individui

    smoke_areas = [

        ['smoke_area_0',15,0,0,[
            'hallway_ingresso'
        ]],
        ['smoke_area_4',15,11,4,[
            'hallway_4_11_11'
        ]]

    ]

    office_rooms = [

        # piano terra

        ['office_0_21_25',21,25,0,[      # [nome, x, y, floor, [lista_neighbors] ]
            'hallway_0_21_21',
        ]],
        ['office_0_11_15',11,15,0,[      
            'hallway_0_11_11',
        ]],
        ['office_0_5_7',5,7,0,[      
            'hallway_0_5_11',
        ]],

        # primo piano

        ['office_1_5_17',5,17,1,[      
            'res_hallway_1_9_17',
        ]],
        ['office_1_21_25',21,25,1,[      
            'hallway_1_21_21',
        ]],
        ['office_1_21_5',21,5,1,[      
            'hallway_1_21_1',
        ]],

        # secondo piano

    ]

    lesson_rooms = [

        # piano terra

        ['lesson_0_3_25',3,25,0,[      # [nome, x, y, floor, [lista_neighbors] ]
            'hallway_0_3_21',
        ]],
        ['lesson_0_9_25',9,25,0,[     
            'hallway_0_9_21',
        ]],
        ['lesson_0_17_17',17,17,0,[      
            'hallway_0_21_17',
        ]],
        ['lesson_0_11_7',11,7,0,[      
            'hallway_0_11_11',
        ]],

        # primo piano

        ['lesson_1_9_25',9,25,1,[      
            'hallway_1_9_21',
        ]],
        ['lesson_1_27_25',27,25,1,[      
            'hallway_1_27_21',
        ]],
        ['lesson_1_25_15',25,15,1,[      
            'hallway_1_25_11',
        ]],

        # secondo piano
        

    ]

    bath_rooms = [

        # piano terra

        ['bath_0_27_25',27,25,0,[      # [nome, x, y, floor, [lista_neighbors] ]
            'hallway_0_27_21'
        ]],

        # primo piano

        ['bath_1_13_15',13,15,1,[      # [nome, x, y, floor, [lista_neighbors] ]
            'hallway_1_13_11'
        ]],

        # secondo piano

    ]

    study_rooms = [

        # piano terra

        ['study_0_5_17',5,17,0,[      # [nome, x, y, floor, [lista_neighbors] ]
            'hallway_0_1_17'
        ]],
        ['study_0_25_11',25,11,0,[      
            'hallway_0_29_11'
        ]],

        # primo piano

        ['study_1_5_5',5,5,1,[      
            'hallway_1_1_5'
        ]],
        ['study_1_21_17',21,17,1,[      
            'hallway_1_21_21'
        ]],

        # secondo piano

    ]

    normal_hallways = [

        # piano terra

        ['hallway_0_3_21',3,21,0,[
            'hallway_0_9_21',
            'hallway_0_1_17',
            'lesson_0_3_25'
        ]],
        ['hallway_0_9_21',9,21,0,[
            'hallway_0_3_21',
            'hallway_0_15_21',
            'lesson_0_9_25'
        ]],
        ['hallway_0_15_21',15,21,0,[
            'hallway_0_9_21',
            'hallway_0_21_21',
            'stairs_0_15_25'
        ]],
        ['hallway_0_21_21',21,21,0,[
            'hallway_0_15_21',
            'hallway_0_27_21',
            'office_0_21_25',
            'hallway_0_21_17'
        ]],
        ['hallway_0_27_21',27,21,0,[
            'hallway_0_21_21',
            'hallway_0_29_17',
            'bath_0_27_25',
            'elev_0_33_22'
        ]],
        ['hallway_0_1_17',1,17,0,[
            'hallway_0_3_21',
            'hallway_0_1_11',
            'study_0_5_17'
        ]],
        ['hallway_0_21_17',21,17,0,[
            'hallway_0_21_21',
            'hallway_0_21_11',
            'lesson_0_17_17'
        ]],
        ['hallway_0_29_17',29,17,0,[
            'hallway_0_27_21',
            'hallway_0_29_11'
        ]],
        ['hallway_0_1_11',1,11,0,[
            'hallway_0_1_17',
            'hallway_0_5_11',
            'hallway_0_1_5'
        ]],
        ['hallway_0_5_11',5,11,0,[
            'hallway_0_1_11',
            'hallway_0_11_11',
            'office_0_5_7'
        ]],
        ['hallway_0_11_11',11,11,0,[
            'hallway_0_5_11',
            'hallway_0_17_11',
            'office_0_11_15',
            'lesson_0_11_7'
        ]],
        ['hallway_0_17_11',17,11,0,[
            'hallway_0_11_11',
            'hallway_0_21_11',
        ]],
        ['hallway_0_21_11',21,11,0,[
            'hallway_0_17_11',
            'hallway_0_21_17',
            'hallway_0_21_5'
        ]],
        ['hallway_0_29_11',29,11,0,[
            'hallway_0_29_17',
            'hallway_0_29_5',
            'study_0_25_11'
        ]],
        ['hallway_0_1_5',1,5,0,[
            'hallway_0_1_11',
            'hallway_0_3_1'
        ]],
        ['hallway_0_21_5',21,5,0,[
            'hallway_0_21_11',
            'hallway_0_21_1',
            'elev_0_17_5'
        ]],
        ['hallway_0_29_5',29,5,0,[
            'hallway_0_29_11',
            'hallway_0_27_1'
        ]],
        ['hallway_0_3_1',3,1,0,[
            'hallway_0_9_1',
            'hallway_0_1_5'
        ]],
        ['hallway_0_9_1',9,1,0,[
            'hallway_0_3_1',
            'hallway_ingresso'
        ]],
        ['hallway_ingresso',15,1,0,[
            'hallway_0_9_1',
            'hallway_0_21_1',
            'smoke_area_0'
        ]],
        ['hallway_0_21_1',21,1,0,[
            'hallway_ingresso',
            'hallway_0_27_1',
            'hallway_0_21_5'
        ]],
        ['hallway_0_27_1',27,1,0,[
            'hallway_0_21_1',
            'hallway_0_29_5'
        ]],

        # primo piano

        ['hallway_1_3_21',3,21,1,[
            'hallway_1_9_21',
            'hallway_1_1_17'
        ]],
        ['hallway_1_9_21',9,21,1,[
            'hallway_1_3_21',
            'hallway_1_15_21',
            'lesson_1_9_25',
            'res_hallway_1_9_17'
        ]],
        ['hallway_1_15_21',15,21,1,[
            'hallway_1_9_21',
            'hallway_1_21_21',
            'stairs_1_15_25'
        ]],
        ['hallway_1_21_21',21,21,1,[
            'hallway_1_15_21',
            'hallway_1_27_21',
            'office_1_21_25',
            'study_1_21_17'
        ]],
        ['hallway_1_27_21',27,21,1,[
            'hallway_1_21_21',
            'hallway_1_29_17',
            'lesson_1_27_25',
            'elev_1_33_22'
        ]],
        ['hallway_1_1_17',1,17,1,[
            'hallway_1_3_21',
            'hallway_1_1_11'
        ]],
        ['hallway_1_29_17',29,17,1,[
            'hallway_1_27_21',
            'hallway_1_29_11'
        ]],
        ['hallway_1_1_11',1,11,1,[
            'hallway_1_1_17',
            'stairs_1_5_11',
            'hallway_1_1_5'
        ]],
        ['hallway_1_13_11',13,11,1,[
            'hallway_1_19_11',
            'bath_1_13_15',
            'res_hallway_1_9_11'
        ]],
        ['hallway_1_19_11',19,11,1,[
            'hallway_1_13_11',
            'hallway_1_25_11'
        ]],
        ['hallway_1_25_11',25,11,1,[
            'hallway_1_29_11',
            'hallway_1_19_11',
            'lesson_1_25_15'
        ]],
        ['hallway_1_29_11',29,11,1,[
            'hallway_1_25_11',
            'hallway_1_29_17',
            'lesson_1_29_5'
        ]],
        ['hallway_1_1_5',1,5,1,[
            'hallway_1_1_11',
            'hallway_1_3_1',
            'study_1_5_5'
        ]],
        ['hallway_1_29_5',29,5,1,[
            'hallway_1_29_11',
            'hallway_1_27_1'
        ]],
        ['hallway_1_3_1',3,1,1,[
            'hallway_1_9_1',
            'hallway_1_1_5'
        ]],
        ['hallway_1_9_1',9,1,1,[
            'hallway_1_3_1',
            'res_hallway_1_9_5',
            'hallway_1_15_1'
        ]],
        ['hallway_1_15_1',15,1,1,[
            'hallway_1_9_1',
            'hallway_1_21_1',
            'elev_1_17_5'
        ]],
        ['hallway_1_21_1',21,1,1,[
            'hallway_1_15_1',
            'hallway_1_27_1',
            'office_1_21_5'
        ]],
        ['hallway_1_27_1',27,1,1,[
            'hallway_1_21_1',
            'hallway_1_29_5'
        ]]

        # secondo piano


    ]

    reserved_hallways = [

        # primo piano

        ['res_hallway_1_9_17',9,17,1,[
            'hallway_1_9_21',
            'res_hallway_1_9_11',
            'office_1_5_17'
        ]],
        ['res_hallway_1_9_11',9,11,1,[
            'hallway_1_13_11',
            'res_hallway_1_9_17',
            'res_hallway_1_9_5'
        ]],
        ['res_hallway_1_9_5',9,5,1,[
            'hallway_1_9_1',
            'res_hallway_1_9_11'
        ]],

        # secondo piano


    ]

    elevators = [

        # piano terra

        ['elev_0_17_5',17,5,0,[
            'elev_1_17_5'
        ], [True,False]],
        ['elev_0_33_22',33,22,0,[
            'elev_1_33_22'
        ], [True,False]]

        # primo piano

        ['elev_1_17_5',17,5,1,[
            'elev_0_17_5'
        ], [False,True]],
        ['elev_1_33_22',33,22,1,[
            'elev_0_33_22',
            'elev_2_33_22'
        ], [True,True]],

        # secondo piano

    ]

    stairs = [

        # piano terra

        ['stairs_0_15_25',15,25,0,[
            'stairs_1_15_25'
        ], [True,False]],

        # primo piano
        
        ['stairs_1_15_25',15,25,1,[
            'stairs_0_15_25'
        ], [False,True]],
        ['stairs_1_5_11',5,11,1,[
            'stairs_2_5_11'
        ], [True,False]],

        # secondo piano

    ]


    # Mancano le scale e gli ascensori:
    #       Come fare per indicare quando salgono e scendono? 
    #       Per esempio creare un altro elemento della lista con coppia true false
    #       Ma rimane il problema che dovremmo poi mettere il nome del nodo arrivo.





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

    places = office_rooms + study_rooms + bath_rooms + lesson_rooms + hallways

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

    for hallway in hallways:
        clauses_list.append(f'is_hallway({hallway[0]})')

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
    clauses_list.append('there_is_a_problem_in(study_0_25_11)')
    clauses_list.append('has_wet_floor(lesson_0_17_17)')
    clauses_list.append('is_only_with_permission(no_hallway)')

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

    # facendo l'append di tutte le clausole, aggiungendo un punto finale e andando a capo.
    file.writelines('.\n'.join(clauses) + '.\n')


#       --------------------------------------------------------------------------------------------------------------------       #
#                                                   Inizio dello Script                                                            #
#       --------------------------------------------------------------------------------------------------------------------       # 

create_KB(PATH_FACTS_KB)



