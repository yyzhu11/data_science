create table Queue(
person_id	int,
person_name	varchar(255),
weight	int,
turn	int);

insert into Queue(person_id, person_name,weight, turn)
values

(5,	'Alice',	250,	1),
(4,	'Bob',	175,	5),
(3,	'Alex',	350,	2),
(6,	'John Cena',	400,	3),
(1,	'Winston',	500,	6),
(2,	'Marie',	200,	4);

select person_name from Queue where turn =

(select max(turn) from 

(select person_name, turn, SUM(weight) OVER (ORDER BY turn) AS weight_total from Queue 
) t1 where weight_total <= 1000 )