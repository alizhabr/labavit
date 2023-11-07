create table dep
(id serial primary key,
title varchar(60) not null,
decanat varchar(150) not null);
create table grupa
(id serial primary key,
title varchar(80) not null,
dep varchar(150) not null,
fk_grupa_dep int references dep(id));
create table students
(id serial primary key,
title varchar(150) not null,
 passport int not null,
 grupa varchar(150) not null,
fk_students_grupa int references grupa(id));


insert into dep(title,decanat) values('информатика','информационная безопасность');
insert into dep(title,decanat) values('сети связи и системы комутации','сети и системы связи');

insert into grupa(title,dep,fk_grupa_dep) values('бик2390','информацонная безопасность',3);
insert into grupa(title,dep,fk_grupa_dep) values('биp1102','информацонная безопасность',3);
insert into grupa(title,dep,fk_grupa_dep) values('сисс2302','сети и системы связи',4);
insert into grupa(title,dep,fk_grupa_dep) values('сисс2390','сети и системы связи',4);

insert into students(title,passport,grupa,fk_students_grupa)
values('фильчуговa т.ф.','23456','бик2390','1');
insert into students(title,passport,grupa,fk_students_grupa)
values('филатов д.ф.','25545','бик2390','1');
insert into students(title,passport,grupa,fk_students_grupa)
values('хапланова а.а.','63456','бик2390','1');
insert into students(title,passport,grupa,fk_students_grupa)
values('чмонин в.ю.','09988','бик2390','1');
insert into students(title,passport,grupa,fk_students_grupa)
values('тимофеев и.а.','46832','бик2390','1');
insert into students(title,passport,grupa,fk_students_grupa)
values('миркуянова а.в.','26546','бир1102','2');
insert into students(title,passport,grupa,fk_students_grupa)
values('пашкова р.ф.','54633','бир1102','2');
insert into students(title,passport,grupa,fk_students_grupa)
values('сизикова а.в.','78493','бир1102','2');
insert into students(title,passport,grupa,fk_students_grupa)
values('ротанов н.а.','77484','бир1102','2');
insert into students(title,passport,grupa,fk_students_grupa)
values('никофоров в.с.','84895','бир1102','2');
insert into students(title,passport,grupa,fk_students_grupa)
values('краев л.в.','67845','сисс2302','3');
insert into students(title,passport,grupa,fk_students_grupa)
values('волков л.м.','67545','сисс2302','3');
insert into students(title,passport,grupa,fk_students_grupa)
values('путин в.а.','00345','сисс2302','3');
insert into students(title,passport,grupa,fk_students_grupa)
values('неритов к.в.','67845','сисс2302','3');
insert into students(title,passport,grupa,fk_students_grupa)
values('кроликова а.е.','60095','сисс2302','3');
insert into students(title,passport,grupa,fk_students_grupa)
values('ирушникова д.д.','34578','сисс2390','4');
insert into students(title,passport,grupa,fk_students_grupa)
values('горловов н.о.','34448','сисс2390','4');
insert into students(title,passport,grupa,fk_students_grupa)
values('запупин о.е.','56778','сисс2390','4');
insert into students(title,passport,grupa,fk_students_grupa)
values('дерден т.е.','00009','сисс2390','4');
insert into students(title,passport,grupa,fk_students_grupa)
values('ортоева м.д.','39999','сисс2390','4');



