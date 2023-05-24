# imports
from Knowledge_Base import Knowledge_Base
import math

# definizione delle variabili utente
PATH_FACTS_KB = './KB/fatti.pl'
PATH_RULES_KB = './KB/regole.pl'
FILES_LIST = [PATH_FACTS_KB, PATH_RULES_KB]

# definizione del metodo per la creazione della KB, con codifica di tutti gli individui
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

        ['office_2_23_11',23,11,2,[      
            'hallway_2_19_11',
        ]],
        ['office_2_15_5',15,5,2,[      
            'hallway_2_11_5',
        ]],

        # terzo piano

        ['office_3_15_25',15,25,3,[      
            'hallway_3_15_21',
        ]],
        ['office_3_17_10',17,10,3,[      
            'res_hallway_3_13_10',
        ]],

        # quarto piano

        ['office_4_5_11',5,11,4,[      
            'hallway_4_11_11',
        ]]

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
        
        ['lesson_2_21_25',21,25,2,[      
            'hallway_2_21_21',
        ]],
        ['lesson_2_5_5',5,5,2,[      
            'hallway_2_1_5',
        ]],
        ['lesson_2_23_5',23,5,2,[      
            'hallway_2_19_5',
        ]],

        # terzo piano

        ['lesson_3_3_25',3,25,3,[      
            'hallway_3_3_21',
        ]],
        ['lesson_3_21_5',21,5,3,[      
            'hallway_3_21_1',
        ]],

        # quarto piano

    ]

    bath_rooms = [

        # piano terra

        ['bath_0_27_25',27,25,0,[      # [nome, x, y, floor, [lista_neighbors] ]
            'hallway_0_27_21'
        ]],

        # primo piano

        ['bath_1_13_15',13,15,1,[      
            'hallway_1_13_11'
        ]],

        # secondo piano

        ['bath_2_33_5',33,5,2,[      
            'hallway_2_29_5'
        ]],

        # terzo piano

        ['bath_3_5_9',5,9,3,[      
            'hallway_3_5_13'
        ]],

        # quarto piano

        ['bath_4_7_17',7,17,4,[      
            'hallway_4_11_17'
        ]]

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

        ['study_2_15_25',15,25,2,[      
            'hallway_2_15_21'
        ]],

        # terzo piano

        ['study_3_5_17',5,17,3,[      
            'hallway_3_5_13'
        ]],
        ['study_3_21_17',21,17,3,[      
            'hallway_3_21_21'
        ]],

        # quarto piano

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
            'hallway_1_29_5'
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
        ]],

        # secondo piano

        ['hallway_2_15_21',15,21,2,[
            'res_hallway_2_9_21',
            'hallway_2_21_21',
            'study_2_15_25'
        ]],
        ['hallway_2_21_21',21,21,2,[
            'hallway_2_15_21',
            'hallway_2_27_21',
            'lesson_2_21_25'
        ]],
        ['hallway_2_27_21',27,21,2,[
            'hallway_2_21_21',
            'elev_2_33_22',
            'hallway_2_29_17'
        ]],
        ['hallway_2_29_17',29,17,2,[
            'hallway_2_27_21',
            'hallway_2_29_11'
        ]],
        ['hallway_2_29_11',29,11,2,[
            'hallway_2_29_17',
            'hallway_2_29_5',
            'stairs_2_33_11'
        ]],
        ['hallway_2_29_5',29,5,2,[
            'hallway_2_29_11',
            'hallway_2_27_1',
            'bath_2_33_5'
        ]],
        ['hallway_2_27_1',27,1,2,[
            'hallway_2_29_5',
            'hallway_2_21_1'
        ]],
        ['hallway_2_21_1',21,1,2,[
            'hallway_2_27_1',
            'hallway_2_19_5'
        ]],
        ['hallway_2_19_5',19,5,2,[
            'hallway_2_21_1',
            'hallway_2_19_11',
            'lesson_2_23_5'
        ]],
        ['hallway_2_19_11',19,11,2,[
            'hallway_2_19_5',
            'hallway_2_15_13',
            'office_2_23_11'
        ]],
        ['hallway_2_15_13',15,13,2,[
            'hallway_2_19_11',
            'hallway_2_11_11',
            'elev_2_15_17'
        ]],
        ['hallway_2_11_11',11,11,2,[
            'hallway_2_11_5',
            'hallway_2_15_13'
        ]],
        ['hallway_2_11_5',11,5,2,[
            'hallway_2_11_11',
            'hallway_2_9_1',
            'office_2_15_5'
        ]],
        ['hallway_2_9_1',9,1,2,[
            'hallway_2_11_5',
            'hallway_2_3_1'
        ]],
        ['hallway_2_3_1',3,1,2,[
            'hallway_2_1_5',
            'hallway_2_9_1'
        ]],
        ['hallway_2_1_5',1,5,2,[
            'hallway_2_3_1',
            'hallway_2_1_11',
            'lesson_2_5_5'
        ]],
        ['hallway_2_1_11',1,11,2,[
            'hallway_2_1_5',
            'res_hallway_2_1_17',
            'stairs_2_5_11'
        ]],

        # terzo piano

        ['hallway_3_3_21',3,21,3,[
            'hallway_3_1_17',
            'hallway_3_9_21',
            'lesson_3_3_25'
        ]],
        ['hallway_3_9_21',9,21,3,[
            'hallway_3_3_21',
            'hallway_3_15_21'
        ]],
        ['hallway_3_15_21',15,21,3,[
            'hallway_3_21_21',
            'hallway_3_9_21',
            'office_3_15_25'
        ]],
        ['hallway_3_21_21',21,21,3,[
            'hallway_3_15_21',
            'hallway_3_27_21',
            'study_3_21_17'
        ]],
        ['hallway_3_27_21',27,21,3,[
            'hallway_3_29_17',
            'hallway_3_21_21'
        ]],
        ['hallway_3_1_17',1,17,3,[
            'hallway_3_1_11',
            'hallway_3_3_21'
        ]],
        ['hallway_3_29_17',29,17,3,[
            'hallway_3_29_11',
            'hallway_3_27_21'
        ]],
        ['hallway_3_1_11',1,11,3,[
            'hallway_3_1_5',
            'hallway_3_1_17',
            'hallway_3_5_13'
        ]],
        ['hallway_3_5_13',5,13,3,[
            'hallway_3_1_11',
            'hallway_3_11_13',
            'study_3_5_17',
            'bath_3_5_9'
        ]],
        ['hallway_3_11_13',11,13,3,[
            'res_hallway_3_13_10',
            'hallway_3_5_13',
            'elev_3_15_17'
        ]],
        ['hallway_3_29_11',29,11,3,[
            'hallway_3_29_17',
            'hallway_3_29_5',
            'stairs_3_33_11'
        ]],
        ['hallway_3_1_5',1,5,3,[
            'hallway_3_1_11',
            'hallway_3_3_1',
            'stairs_3_5_5'
        ]],
        ['hallway_3_29_5',29,5,3,[
            'hallway_3_29_11',
            'hallway_3_27_1'
        ]],
        ['hallway_3_3_1',3,1,3,[
            'hallway_3_1_5',
            'hallway_3_9_1'
        ]],
        ['hallway_3_9_1',9,1,3,[
            'hallway_3_3_1',
            'hallway_3_15_1'
        ]],
        ['hallway_3_15_1',15,1,3,[
            'hallway_3_9_1',
            'hallway_3_21_1',
            'res_hallway_3_13_5'
        ]],
        ['hallway_3_21_1',21,1,3,[
            'hallway_3_15_1',
            'hallway_3_27_1',
            'lesson_3_21_5'
        ]],
        ['hallway_3_27_1',27,1,3,[
            'hallway_3_21_1',
            'hallway_3_29_5'
        ]],

        # quarto piano

        ['hallway_4_3_21',3,21,4,[
            'hallway_4_1_17',
            'hallway_4_9_21'
        ]],
        ['hallway_4_9_21',9,21,4,[
            'hallway_4_11_17',
            'hallway_4_3_21'
        ]],
        ['hallway_4_1_17',1,17,4,[
            'hallway_4_1_11',
            'hallway_4_3_21'
        ]],
        ['hallway_4_11_17',11,17,4,[
            'hallway_4_9_21',
            'hallway_4_11_11',
            'bath_4_7_17'
        ]],
        ['hallway_4_1_11',1,11,4,[
            'hallway_4_1_5',
            'hallway_4_1_17',
            'office_4_5_11'
        ]],
        ['hallway_4_11_11',11,11,4,[
            'hallway_4_11_5',
            'hallway_4_11_17',
            'smoke_area_4'
        ]],
        ['hallway_4_1_5',1,5,4,[
            'hallway_4_3_1',
            'hallway_4_1_11',
            'stairs_4_5_5'
        ]],
        ['hallway_4_11_5',11,5,4,[
            'hallway_4_9_1',
            'hallway_4_11_11'
        ]],
        ['hallway_4_3_1',3,1,4,[
            'hallway_4_1_5',
            'hallway_4_9_1'
        ]],
        ['hallway_4_9_1',9,1,4,[
            'hallway_4_11_5',
            'hallway_4_3_1'
        ]]

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

        ['res_hallway_2_3_21',3,21,2,[
            'res_hallway_2_9_21',
            'res_hallway_2_1_17'
        ]],
        ['res_hallway_2_9_21',9,21,2,[
            'res_hallway_2_3_21',
            'hallway_2_15_21'
        ]],
        ['res_hallway_2_1_17',1,17,2,[
            'res_hallway_2_3_21',
            'hallway_2_1_11'
        ]],

        # terzo piano

        ['res_hallway_3_13_10',13,10,3,[
            'res_hallway_3_13_5',
            'hallway_3_11_13',
            'office_3_17_10'
        ]],
        ['res_hallway_3_13_5',13,5,3,[
            'res_hallway_3_13_10',
            'hallway_3_15_1'
        ]],

    ]

    elevators = [

        # piano terra

        ['elev_0_17_5',17,5,0,[         #[nome,x,y,flat, [lista neighbors], [Up,Down]]
            'elev_1_17_5',
            'hallway_0_21_5'
        ], [True,False]],
        ['elev_0_33_22',33,22,0,[
            'elev_1_33_22',
            'hallway_0_27_21'
        ], [True,False]],

        # primo piano

        ['elev_1_17_5',17,5,1,[
            'elev_0_17_5',
            'hallway_1_15_1'
        ], [False,True]],
        ['elev_1_33_22',33,22,1,[
            'elev_0_33_22',
            'elev_2_33_22',
            'hallway_1_27_21'
        ], [True,True]],

        # secondo piano

        ['elev_2_33_22',33,22,2,[
            'elev_1_33_22',
            'hallway_2_27_21'
        ], [False,True]],
        ['elev_2_15_17',15,17,2,[
            'elev_3_15_17',
            'hallway_2_15_13'
        ], [True,False]],

        # terzo piano

        ['elev_3_15_17',15,17,3,[
            'elev_2_15_17',
            'hallway_3_11_13'
        ], [False,True]]

    ]

    stairs = [

        # piano terra

        ['stairs_0_15_25',15,25,0,[
            'stairs_1_15_25',
            'hallway_0_15_21'
        ], [True,False]],

        # primo piano
        
        ['stairs_1_15_25',15,25,1,[
            'stairs_0_15_25',
            'hallway_1_15_21'
        ], [False,True]],
        ['stairs_1_5_11',5,11,1,[
            'stairs_2_5_11',
            'hallway_1_1_11'
        ], [True,False]],

        # secondo piano

        ['stairs_2_5_11',5,11,2,[
            'stairs_1_5_11',
            'hallway_2_1_11'
        ], [False,True]],
        ['stairs_2_33_11',33,11,2,[
            'stairs_3_33_11',
            'hallway_2_29_11'
        ], [True,False]],

        # terzo piano

        ['stairs_3_5_5',5,5,3,[
            'stairs_4_5_5',
            'hallway_3_1_5'
        ], [True,False]],
        ['stairs_3_33_11',33,11,3,[
            'stairs_2_33_11',
            'hallway_3_29_11'
        ], [False,True]],

        # quarto piano

        ['stairs_4_5_5',5,5,4,[
            'stairs_3_5_5',
            'hallway_4_1_5'
        ], [False,True]]

    ]

    students = [                            # student = [nome_studente , lista_index_corsi]
        ['student_1',['class_1','class_2']],
        ['student_2',['class_1','class_3']],
        ['student_3',['class_2','class_4']],
        ['student_4',['class_3','class_4']]
    ]

    teachers = [                            # teacher = [nome_prof , lista_corsi, lista_index_uffici]
        ['teacher_1',['class_1'],['office_0_5_7']],
        ['teacher_2',['class_2'],['office_1_21_5']],
        ['teacher_3',['class_3'],['office_4_5_11', 'office_3_15_25']],
        ['teacher_4',['class_4'],['office_2_23_11']]
    ]

    classes = [                             # cl = [nome_corso, lista_schedulazioni] dove 
        ['class_1',[                           # lista_schedulazioni = [index_aula, giorno, ora_inizio, minuti_inizio, ora_fine, minuti_fine]
            ['lesson_0_9_25','monday',8,30,10,30],
            ['lesson_0_9_25','friday',10,30,13,30],
            ['lesson_0_9_25','wednesday',9,00,11,00]
            ]
        ],
        ['class_2',[
            ["lesson_3_3_25",'tuesday',10,30,12,30],
            ["lesson_3_3_25",'friday',11,30,13,30],
            ["lesson_3_3_25",'wednesday',15,00,17,00]
            ]
        ],
        ['class_3',[
            ["lesson_2_5_5",'monday',10,30,12,00],
            ["lesson_2_5_5",'friday',10,45,12,45],
            ["lesson_2_5_5",'thursday',8,00,11,00]
            ]
        ],
        ['class_4',[
            ["lesson_1_27_25",'monday',11,30,14,30],
            ["lesson_1_27_25",'friday',10,30,13,30],
            ["lesson_1_27_25",'tuesday',13,00,16,00]
            ]
        ],
    ]

    hallways = normal_hallways + reserved_hallways
    places = smoke_areas + office_rooms + study_rooms + bath_rooms + lesson_rooms + hallways + stairs + elevators

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

    # aggiungiamo i fatti per i corridoi
    for hallway in hallways:
        clauses_list.append(f'is_hallway({hallway[0]})')

    for res_hallway in reserved_hallways:
        clauses_list.append(f'is_only_with_permission({res_hallway[0]})')

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
        for neighbor in place[4]:
            clauses_list.append(f'direct_arc({place[0]},{neighbor})')

    # aggiungiamo i fatti per gli ascensori
    for elev in elevators:
        if(elev[5][0]):
            clauses_list.append(f'is_elevator_up({elev[0]})')
        if(elev[5][1]):
            clauses_list.append(f'is_elevator_down({elev[0]})')

    # aggiungiamo i fatti per le scale
    for stair in stairs:
        if(stair[5][0]):
            clauses_list.append(f'is_stairs_up({stair[0]})')
        if(stair[5][1]):
            clauses_list.append(f'is_stairs_down({stair[0]})')

    # aggiungiamo i fatti per le aree fumatori
    for s_a in smoke_areas:
        clauses_list.append(f'is_smoke_area({s_a[0]})')

    # ordiniamo la lista per evitare ridefinizioni
    clauses_list.sort()

    # scriviamo i fatti su file
    file_prolog = open(path, "w")
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



