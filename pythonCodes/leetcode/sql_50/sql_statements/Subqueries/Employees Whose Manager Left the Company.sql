create table Employee5 (

	employee_id	int,
	name	varchar(255),
	manager_id	int,
	salary	int
)

insert into Employee5(employee_id, name, manager_id, salary)
values
(3,	'Mila',	9,	60301),
(12,	'Antonella',	NULL,	31000),
(13,	'Emery',	NULL,	67084),
(1,	'Kalel', 11,	21241),
(9,	'Mikaela', NULL,	50937),
(11, 'Joziah',	6,	28485);


select employee_id from Employee5 where employee_id not in

(select e1.employee_id from Employee5 e1 join Employee5 e2 
on e1.manager_id = e2.employee_id where e2.employee_id is not null) and manager_id is not null