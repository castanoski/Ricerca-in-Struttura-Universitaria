floor(bathroom_101,0).
floor(lesson_room_014,0).
floor(office_101,0).
follows_class(student_001,icon).
follows_class(student_001,reti).
follows_class(student_002,mri).
follows_class(student_002,reti).
follows_class(student_003,cc).
follows_class(student_003,mri).
follows_class(student_004,icon).
follows_class(student_004,mri).
is_bath_room(bathroom_101).
is_bath_room(bathroom_102).
is_bath_room(bathroom_103).
is_bath_room(bathroom_104).
is_lesson_room(lesson_room_011).
is_lesson_room(lesson_room_012).
is_lesson_room(lesson_room_013).
is_lesson_room(lesson_room_014).
is_office_room(office_101).
is_office_room(office_102).
is_office_room(office_201).
is_office_room(office_202).
is_scheduled(cc,lesson_room_013,get_time(friday,10,45),get_time(friday,12,45)).
is_scheduled(cc,lesson_room_013,get_time(monday,10,30),get_time(monday,12,0)).
is_scheduled(cc,lesson_room_013,get_time(thursday,8,0),get_time(thursday,11,0)).
is_scheduled(icon,lesson_room_012,get_time(friday,10,30),get_time(friday,13,30)).
is_scheduled(icon,lesson_room_012,get_time(monday,8,30),get_time(monday,10,30)).
is_scheduled(icon,lesson_room_012,get_time(wednesday,9,0),get_time(wednesday,11,0)).
is_scheduled(mri,lesson_room_011,get_time(friday,11,30),get_time(friday,13,30)).
is_scheduled(mri,lesson_room_011,get_time(tuesday,10,30),get_time(tuesday,12,30)).
is_scheduled(mri,lesson_room_011,get_time(wednesday,15,0),get_time(wednesday,17,0)).
is_scheduled(reti,lesson_room_014,get_time(friday,10,30),get_time(friday,13,30)).
is_scheduled(reti,lesson_room_014,get_time(monday,11,30),get_time(monday,14,30)).
is_scheduled(reti,lesson_room_014,get_time(tuesday,13,0),get_time(tuesday,16,0)).
is_student(student_001).
is_student(student_002).
is_student(student_003).
is_student(student_004).
is_study_room(study_room_101).
is_study_room(study_room_102).
is_study_room(study_room_103).
is_study_room(study_room_104).
is_teacher(teacher_001).
is_teacher(teacher_002).
is_teacher(teacher_003).
is_teacher(teacher_004).
office_owner(teacher_001,office_102).
office_owner(teacher_002,office_202).
office_owner(teacher_003,office_101).
office_owner(teacher_004,office_201).
position(bathroom_101,0,0).
position(lesson_room_014,1,1).
position(office_101,2,1).
teaches_class(teacher_001,reti).
teaches_class(teacher_002,mri).
teaches_class(teacher_003,cc).
teaches_class(teacher_004,icon).
