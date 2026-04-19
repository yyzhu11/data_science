select e2.employee_id, e2.name, count(distinct e1.employee_id) as reports_count, 
round(avg(e1.age),0) as average_age
from Employees3 e1  join Employees3 e2 
on e1.reports_to = e2.employee_id 

group by e2.employee_id, e2.name order by e2.employee_id


select t1.reports_to  as employee_id,t2.name as name,  reports_count, average_age from 

(select reports_to , count(distinct employee_id) as reports_count, avg(age) as average_age  
from Employees3 where reports_to is not null group by reports_to) t1 left join Employees3 t2 on t1.reports_to = t2.employee_id



create table Employees3 (

	employee_id	int,
	name	varchar(255),
	reports_to	int,
	age	int
)

insert into Employees3 (employee_id, [name], reports_to, age)
values
(1, 'Michael',	NULL,45),
(2, 'Alice',	1,	38),
(3,	'Bob',	1,	42),
(4,	'Charlie',	2,	34),
(5,	'David',	2,	40),
(6,	'Eve',	3,	37),
(7,	'Frank',	NULL,	50),
(8,	'Grace',	NULL,	48);

select t1.reports_to as employee_id, t2.name, reports_count, average_age from 
(select reports_to, count(distinct employee_id) as reports_count, avg(age) as average_age
from Employees3 where reports_to is not null group by reports_to ) t1 join Employees3 t2 
on t1.reports_to = t2.employee_id