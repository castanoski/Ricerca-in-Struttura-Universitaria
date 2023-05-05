% Regole per il ragionamento sull'accesso all'ascensore e alle aule


    % Regola per il permesso dell'utilizzo dell'ascensore a professori
can_use_elevator(Person) :- 
    is_teacher(Person).

    % Regola per il permesso dell'utilizzo dell'ascensore a studenti


    % Regola per il permesso dell'accesso all'ufficio


    % Regola per il permesso dell'accesso all'aula
can_enter_room(Person, Class_Room, Time) :-
    takes_part_in_class(Person, Class),
    is_taking_place(Class, Class_Room, Time).

    % Regola per capire se uno studente prende parte al corso
takes_part_in_class(Person, Class) :-
    is_student(Person),
    follows_class(Person, Class).

    % Regola per capire se un docente prende parte al corso
takes_part_in_class(Person, Class) :-
    is_teacher(Person),
    teaches_class(Person, Class).

    % Regole per capire se una lezione si sta svolgendo nell_aula in un determinato tempo
is_taking_place(Class, Class_Room, Time) :-
    is_scheduled(Class, Class_Room, Start_Time, End_Time),
    is_time_included_in(Time, Start_Time, End_Time).

    % Regole per capire se un certo momento è incluso tra due estremi (non strettamente incluso)
is_time_included_in(Time, Start_Time, End_Time) :-
    is_before_time(Time, End_Time),
    is_before_time(Start_Time, Time).

is_time_included_in(Time, Time, _).

is_time_included_in(Time, _, Time).

    % Regole per calcolare se il primo tempo viene prima del secondo
is_before_time(get_time(Day, Hour1, _), get_time(Day, Hour2, _)) :-
    Hour1 < Hour2.
is_before_time(get_time(Day, Hour, Minute1), get_time(Day, Hour, Minute2)) :-   
    Minute1 < Minute2.                                                         
% se il giorno è diverso non è before perchè
% si intende before nello stesso giorno

% Regole per i vincoli di integrità

    % Regola che vincola una persona a non poter essere ne docente ne studente
falso :-
    is_teacher(Person),
    is_student(Person).

    % Regola per il controllo di aule eventualmente occupate da più lezioni contemporaneamente
falso :-
    is_scheduled(Class1, Class_Room, _, End_Time1),
    is_scheduled(Class2, Class_Room, Start_Time2, End_Time2),
    is_before_time(Start_Time2, End_Time1),
    is_before_time(End_Time1, End_Time2),
    Class1 =\= Class2.

    % Regola per controllare che una lezione non sia schedulata con due date non coerenti tra di loro
falso :-
    is_scheduled(_, _, Start_Time, End_Time),
    is_before_time(End_Time, Start_Time).

falso :-
    is_scheduled(_,_,Time,Time).
