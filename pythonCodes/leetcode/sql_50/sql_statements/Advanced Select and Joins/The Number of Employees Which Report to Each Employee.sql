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


select e2.employee_id, e2.name, count(distinct e1.employee_id) as reports_count, 
round(avg(e1.age),0) as average_age
from Employees3 e1  join Employees3 e2 
on e1.reports_to = e2.employee_id 

group by e2.employee_id, e2.name order by e2.employee_id
