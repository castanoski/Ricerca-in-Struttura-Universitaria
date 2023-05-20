
%       --------------------------------------------------------------------------------------------------------------------       %
%                               Regole per il ragionamento sui permessi di accesso ad ascensore e aule                             %
%       --------------------------------------------------------------------------------------------------------------------       % 

    % Regole per capire se una persona può utilizzare il metodo per salire/scendere  
can_go_up_with(Person, Method) :-
    is_elevator_up(Method),
    can_use_elevator(Person).

can_go_up_with(Person, Method) :-
    is_stairs_up(Method),
    is_person(Person).

can_go_down_with(Person, Method) :-
    is_elevator_down(Method),
    can_use_elevator(Person).

can_go_down_with(Person, Method) :-
    is_stairs_down(Method),
    is_person(Person).

    % Regola per il permesso dell'utilizzo dell'ascensore a professori
can_use_elevator(Person) :- 
    is_teacher(Person).

    % Regola per il permesso dell'utilizzo dell'ascensore a studenti



    % Regole per il permesso sull'utilizzo di tutti i luoghi
has_access(Person, Hallway, _) :-
    can_pass_hallway(Person, Hallway).

has_access(Person, Room, Time) :-
    can_enter_room(Person, Room, Time).

has_access(Person, Method, _) :-
    can_go_up_with(Person, Method).

has_access(Person, Method, _) :-
    can_go_down_with(Person, Method).


    % Regola per il passaggio su un corridoio
can_pass_hallway(Person,Hallway) :-
    is_available_hallway(Hallway),
    has_permission_to_pass(Person,Hallway).

has_permission_to_pass(Person, Hallway) :-
    is_hallway(Hallway),
    \+is_only_with_permission(Hallway),
    is_person(Person).

    % Regole per avere il permesso esplicito a tutti i corridoi o a un corridoio specifico





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
can_enter_room(Person, Room, Time) :-
    is_available_room(Room),
    is_bath_room(Room),
    is_legal_time(Time),
    is_person(Person).

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
    is_time_included_in(Time, Start_Time, End_Time).    % non serve che sia legale perche incluso in is_time_included_in

    % Regole per capire se un certo momento è incluso tra due estremi (non strettamente incluso)
is_time_included_in(Time, Start_Time, End_Time) :-
    is_before_time(Time, End_Time),
    is_before_time(Start_Time, Time),
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
is_legal_day(thursday).
is_legal_day(friday).
is_legal_day(saturday).
is_legal_day(sunday).

    % Regole per calcolare se il primo tempo viene prima del secondo
is_before_time(get_time(Day, Hour1, _), get_time(Day, Hour2, _)) :-
    Hour1 < Hour2.

is_before_time(get_time(Day, Hour, Minute1), get_time(Day, Hour, Minute2)) :-   % se il giorno è diverso non è before perchè
    Minute1 =< Minute2.                                                          % si intende before nello stesso giorno

    % Regole per capire se una stanza è disponibile o meno
is_available_room(Room) :-
    is_room(Room),
    \+is_unavailable(Room).

is_unavailable(Place) :-
    there_is_a_problem_in(Place).

is_unavailable(Place) :-
    has_wet_floor(Place).

    % Regole per capire se un corridoio è disponibile
is_available_hallway(Hallway) :-
    is_hallway(Hallway),
    \+is_unavailable(Hallway).

    % Regole per capire se si tratta di un posto (cioè tutto ciò in cui si può andare)
is_place(Place) :-
    is_room(Place).

is_place(Place) :-
    is_elevator(Place).

is_place(Place) :-
    is_stairs(Place).

is_place(Place) :-
    is_hallway(Place).

is_place(SmokeArea) :-
    is_smoke_area(SmokeArea).

    % Regole per determinare se si tratta di una stanza
is_room(Room) :-
    is_bath_room(Room).

is_room(Room) :-
    is_lesson_room(Room).

is_room(Room) :-
    is_study_room(Room).

is_room(Room) :-
    is_office_room(Room).

    % Regole per determinare se è un ascensore
is_elevator(Method) :-
    is_elevator_down(Method).

is_elevator(Method) :-
    is_elevator_up(Method).  

    % Regole per determinare se è una scala
is_stairs(Method) :-
    is_stairs_down(Method).

is_stairs(Method) :-
    is_stairs_up(Method). 

    % Regole per determinare se si tratta di una persona
is_person(Person) :-
    is_student(Person).

is_person(Person) :-
    is_teacher(Person).



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
    Start_Time2 \= End_Time1,
    Class1 \= Class2.                                              

    % Regole per controllare che una lezione non sia schedulata con due date non coerenti tra di loro
falso :-
    is_scheduled(_, _, Start_Time, End_Time),
    is_before_time(End_Time, Start_Time).

falso :-
    is_scheduled(_,_,Time,Time).

    % Regole per controllare che una lezione non sia schedulata in un orario illegale
falso :-
    is_scheduled(_,_,Time,_),
    \+is_legal_time(Time).

falso :-
    is_scheduled(_,_,_,Time),
    \+is_legal_time(Time).

    % Regola per controllare che una lezione non sia schedulata in una stanza che non è aula di lezione
falso :-
    is_scheduled(_, Room, _, _),
    \+is_lesson_room(Room).

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

                % AGGIUNGI ANCHE LE ALTRE COPPIE DI TIPI DI STANZA


    % Regole per controllare che nessuno studente insegni e nessun professore segua dei corsi
falso :-
    teaches_class(Teacher,_),
    \+is_teacher(Teacher).

falso :-
    follows_class(Student,_),
    \+is_student(Student).

    % Regola per garantire che solo i professori possano avere un ufficio
falso :-
    office_owner(Non_Teacher,_),
    \+is_teacher(Non_Teacher).              % E' corretto in questo modo? Controlla quantificazione

    % Regola per garantire che i Professori possano possedere solo Uffici
falso :-
    office_owner(_, Room),
    \+is_office_room(Room).

    % Regole per garantire che nessun posto abbia più coordinate
falso :-
    position(Place, X1, _),
    position(Place, X2, _),
    X1 \= X2.

falso :-
    position(Place, _, Y1),
    position(Place, _, Y2),
    Y1 \= Y2.

falso :-
    floor(Place, Floor1),
    floor(Place, Floor2),
    Floor1 \= Floor2.

    % Regole per garantire che nessuna coppia di posti abbia le stesse coordinate
falso :-
    position(Place1, X, Y),
    position(Place2, X, Y),
    floor(Place1, Floor),
    floor(Place2, Floor),
    Place1 \= Place2.

    % Regole per garantire la coerenza del tipo degli individui

falso :-
    can_pass_hallway(Person, _),
    \+is_person(Person).

falso :-
    is_unavailable(Place),
    \+is_place(Place).

    % Regole per determinare se scale o ascensori sono collegati solo con elementi di stesse coordinate e piano che differisce di 1

