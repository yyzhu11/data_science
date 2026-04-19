select person_name from Queue where turn =

(select max(turn) from 

(select person_name, turn, SUM(weight) OVER (ORDER BY turn) AS weight_total from Queue 
) t1 where weight_total <= 1000 )

select top 1 person_name from 

(select person_name, weight, turn, SUM(weight) OVER (ORDER BY turn
        ROWS BETWEEN UNBOUNDED PRECEDING AND 0 PRECEDING
    ) AS sum_of_previous_rows from Queue  ) t1 where t1.sum_of_previous_rows <= 1000 order by t1.turn desc

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


select top 1 person_name from (
select person_name, weight, turn, sum(weight) over (order by turn ) as total_weight from Queue) t1 where total_weight <= 1000 order by turn desc


SELECT q1.person_name
FROM Queue q1
JOIN Queue q2
  ON q2.turn <= q1.turn
GROUP BY q1.person_id, q1.person_name, q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY q1.turn DESC