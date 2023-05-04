# Regole per il ragionamento sull'accesso all'ascensore e alle aule


    # Regola per il permesso dell'utilizzo dell'ascensore a professori
can_use_elevator(Person) :- 
    is_teacher(Person).

    # Regola per il permesso dell'utilizzo dell'ascensore a studenti


    # Regola per il permesso dell'accesso all'ufficio


    # Regola per il permesso dell'accesso all'aula
can_enter_room(Person, Class_Room, Time) :-
    takes_part_in_class(Person, Class),
    is_taking_place(Class, Class_Room, Time).

    # Regola per capire se uno studente prende parte al corso
takes_part_in_class(Person, Class) :-
    is_student(Person),
    follows_class(Person, Class).

    # Regola per capire se un docente prende parte al corso
takes_part_in_class(Person, Class) :-
    is_teacher(Person),
    teaches_class(Person, Class).

    # Regola per capire se una lezione si sta svolgendo nell'aula in un determinato tempo
is_taking_place(Class, Class_Room, Time) :-
    is_scheduled(Class, Class_Room, Start_Time, End_Time),
    is_before_time(Time, End_Time),
    is_before_time(Start_Time, Time).

    # Regole per calcolare se il primo tempo viene prima del secondo
is_before_time(get_time(Day, Hour1, Minute1), get_time(Day, Hour2, Minute2)) :-
    Hour1 < Hour2.
is_before_time(get_time(Day, Hour, Minute1), get_time(Day, Hour, Minute2)) :-   # se il giorno è diverso non è before perchè
    Minute1 <= Minute2.                                                         # si intende before nello stesso giorno




# Regole per i vincoli di integrità

falso :-
    is_teacher(Person),
    is_student(Person).

