
%       --------------------------------------------------------------------------------------------------------------------       %
%                               Regole per il ragionamento sui permessi di accesso ad ascensore e aule                             %
%       --------------------------------------------------------------------------------------------------------------------       % 


    % Regola per il permesso dell'utilizzo dell'ascensore a professori
can_use_elevator(Person) :- 
    is_teacher(Person).

    % Regola per il permesso dell'utilizzo dell'ascensore a studenti


    % Regola per il permesso dell'accesso all'ufficio da parte del docente proprietario e degli studenti del suo corso
can_enter_room(Person, Room, _) :-
    is_available_room(Room),
    is_office_room(Room),
    office_owner(Person, Room).

can_enter_room(Person, Room, _) :-
    is_available_room(Room),
    is_office_room(Room),
    follows_class(Person, Class),
    teaches_class(Teacher, Class),
    office_owner(Teacher, Room).

    % Regola per il permesso dell'accesso all'aula studio
can_enter_room(Person, Room, Time) :-
    is_available_room(Room),
    is_study_room(Room),
    is_student(Person),
    is_legal_time(Time).

    % Regola per il permesso dell'accesso al bagno
can_enter_room(_, Room, Time) :-
    is_available_room(Room),
    is_bath_room(Room),
    is_legal_time(Time).

    % Regola per il permesso dell'accesso all'aula di lezioni
can_enter_room(Person, Class_Room, Time) :-
    is_available_room(Class_Room),
    is_lesson_room(Class_Room),
    takes_part_in_class(Person, Class),
    is_taking_place(Class, Class_Room, Time).   % non serve che sia legale perchè implicito in is_taking_place

    % Regola per capire se uno studente prende parte al corso
takes_part_in_class(Person, Class) :-
    follows_class(Person, Class).

    % Regola per capire se un docente prende parte al corso
takes_part_in_class(Person, Class) :-
    teaches_class(Person, Class).

    % Regole per capire se una lezione si sta svolgendo nell_aula in un determinato tempo
is_taking_place(Class, Class_Room, Time) :-
    is_scheduled(Class, Class_Room, Start_Time, End_Time),
    is_time_included_in(Time, Start_Time, End_Time).    % non serve che sia legale perche incluso in is_time_included_ina

    % Regole per capire se un certo momento è incluso tra due estremi (non strettamente incluso)
is_time_included_in(Time, Start_Time, End_Time) :-
    is_before_time(Time, End_Time),
    is_before_time(Start_Time, Time),
    is_legal_time(Time).

is_time_included_in(Time, Time, _) :-
    is_legal_time(Time).

is_time_included_in(Time, _, Time) :-
    is_legal_time(Time).

    % Regole per valutare se un tempo ha un formato accettabile
is_legal_time(get_time(Day, Hour, Minute)) :-
    Minute =< 59,
    Minute >= 0,
    Hour =< 23,
    Hour >= 0,
    is_legal_day(Day).

    % Fatti per definire il giorno della settimana accettabile
is_legal_day(monday).
is_legal_day(tuesday).
is_legal_day(wednesday).
is_legal_day(thurday).
is_legal_day(friday).
is_legal_day(saturday).
is_legal_day(sunday).

    % Regole per calcolare se il primo tempo viene prima del secondo
is_before_time(get_time(Day, Hour1, _), get_time(Day, Hour2, _)) :-
    Hour1 < Hour2.

is_before_time(get_time(Day, Hour, Minute1), get_time(Day, Hour, Minute2)) :-   % se il giorno è diverso non è before perchè
    Minute1 < Minute2.                                                          % si intende before nello stesso giorno

    % Regole per capire se una stanza è disponibile o meno
is_available_room(Room) :-
    \+there_is_a_problem_in(Room).



%       --------------------------------------------------------------------------------------------------------------------       %
%                                               Regole per i vincoli di integrità                                                  %
%       --------------------------------------------------------------------------------------------------------------------       % 

    % Regola che vincola una persona a non poter essere ne docente ne studente
falso :-
    is_teacher(Person),
    is_student(Person).     % aggiungi nel caso ci siano altri ruoli da aggiungere

    % Regola per il controllo di aule eventualmente occupate da più lezioni contemporaneamente
falso :-
    is_scheduled(Class1, Class_Room, _, End_Time1),
    is_scheduled(Class2, Class_Room, Start_Time2, End_Time2),
    is_before_time(Start_Time2, End_Time1),
    is_before_time(End_Time1, End_Time2),
    Class1 =\= Class2.                                              % controlla che effettivamente due lezioni con orario identico vadano in conflitto

    % Regole per controllare che una lezione non sia schedulata con due date non coerenti tra di loro
falso :-
    is_scheduled(_, _, Start_Time, End_Time),
    is_before_time(End_Time, Start_Time).

falso :-
    is_scheduled(_,_,Time,Time).

    % Regole per controllare la presenza di aule che siano di due tipi diversi 
falso :-
    is_bath_room(Room),
    is_lesson_room(Room).

falso :-
    is_bath_room(Room),
    is_study_room(Room).

falso :-
    is_bath_room(Room),
    is_office_room(Room).

falso :-
    is_lesson_room(Room),
    is_study_room(Room).

falso :-
    is_lesson_room(Room),
    is_office_room(Room).

falso :-
    is_study_room(Room),
    is_office_room(Room).

    % Regole per controllare che nessuno studente insegni e nessun professore segua dei corsi
falso :-
    teaches_class(Student,_),
    is_student(Student).

falso :-
    follows_class(Teacher,_),
    is_teacher(Teacher).

    % Regola per garantire che solo i professori possano avere un ufficio
falso :-
    office_owner(Non_Teacher,_),
    \+is_teacher(Non_Teacher).              % E' corretto in questo modo? Controlla quantificazione